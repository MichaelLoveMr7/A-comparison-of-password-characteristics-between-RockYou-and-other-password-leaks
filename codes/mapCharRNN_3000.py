#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:17:47 2020

@author: yujiedong
"""

import tensorflow as tf
import numpy as np
import os
import time
import pandas as pd
print(tf.__version__)


#/Users/yujiedong/Downloads/BreachCompilation/data/combined_Random.txt
#pswd_data = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/combined_Random.txt", 
#                         header = None, error_bad_lines = False,encoding='ISO-8859-1')
pswd_data = pd.read_csv("Rockyou_array_3000.csv")
combined_Random = pswd_data.iloc[0:2000, 0]
#print(type(pswd_data_Random))
#pswd_data_Random = pd.DataFrame(pswd_data_Random)
#pswd_data_Random = pswd_data_Random.values


#print(type(text))
np.savetxt('Rockyou_3000.txt',
           combined_Random.values, fmt='%s', header='X') 

path_to_file = 'Rockyou_3000.txt'

text = open(path_to_file,'rb').read().decode(encoding='ISO-8859-1')
print(len(text))
#pswd_data_Random.to_string()

#pswd_data_Random.to_csv('pswd_data_Random_1B4.csv')
#print(type(pswd_data1),pswd_data1)


# length of text is the number of characters in it
print ('Length of text: {} characters'.format(len(text)))
print(len(text))
print(text[:253])

# The unique characters in the file
vocab = sorted(set(text))
print ('{} unique characters'.format(len(vocab)))

# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])

print('{')
for char,_ in zip(char2idx, range(20)):
    print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
print('  ...\n}')
    
# Show how the first 13 characters from the text are mapped to integers
print ('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))    
    
# The maximum length sentence we want for a single input in characters
seq_length = 100
examples_per_epoch = len(text)//(seq_length+1)

# Create training examples / targets
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
print(char_dataset)

for i in char_dataset.take(5):
  print(idx2char[i.numpy()])

sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

for item in sequences.take(5):
  print(repr(''.join(idx2char[item.numpy()])))

def split_input_target(chunk):
  input_text = chunk[:-1]
  target_text = chunk[1:]
  return input_text, target_text

dataset = sequences.map(split_input_target)
print(dataset)

for input_example, target_example in  dataset.take(1):
  print ('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
  print ('Target data:', repr(''.join(idx2char[target_example.numpy()])))

for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
  print("Step {:4d}".format(i))
  print("  input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
  print("  expected output: {} ({:s})".format(target_idx, repr(idx2char[target_idx])))

# Batch size
BATCH_SIZE = 64

# Buffer size to shuffle the dataset
# (TF data is designed to work with possibly infinite sequences,
# so it doesn't attempt to shuffle the entire sequence in memory. Instead,
# it maintains a buffer in which it shuffles elements).
BUFFER_SIZE = 10000 #Originally BUFFER_SIZE = 10000

dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

print(dataset)

# Length of the vocabulary in chars
vocab_size = len(vocab)
print(vocab_size)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
  return model

model = build_model(
    vocab_size = len(vocab),
    embedding_dim=embedding_dim,
    rnn_units=rnn_units,
    batch_size=BATCH_SIZE)
print()
print("begin:")
for input_example_batch, target_example_batch in dataset.take(1):
  example_batch_predictions = model(input_example_batch)
  print("example_batch_predictions:     ",example_batch_predictions)
  print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")
#print(example_batch_predictions)
print('done')
print()
model.summary()

sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()


print("Input: ", repr("  ".join(idx2char[input_example_batch[0]])))# Input
print()
print("Next Char Predictions: ", repr("  ".join(idx2char[sampled_indices ])))
# Output after being processed by tf.random.categorical, 
# and example-batch_predictions is processed by model and this model 
# is processed by tf.keras.layers


def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

example_batch_loss  = loss(target_example_batch, example_batch_predictions)
print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
print("scalar_loss:      ", example_batch_loss.numpy().mean())

model.compile(optimizer='adam', loss=loss)

# Directory where the checkpoints will be saved
checkpoint_dir = './training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")
print(checkpoint_prefix)

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)
print(checkpoint_callback)

EPOCHS=5000

history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])


tf.train.latest_checkpoint(checkpoint_dir)

model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.build(tf.TensorShape([64, None]))

model.summary()

def generate_text(model, start_string):
  # Evaluation step (generating text using the learned model)

  # Number of characters to generate
  num_generate = 1000

  # Converting our start string to numbers (vectorizing)
  input_eval = [char2idx[s] for s in start_string]
  #print(char2idx)
  print("input_eval", input_eval)
  input_eval = tf.expand_dims(input_eval, 0)
  print("input_eval", input_eval)
  # Empty string to store our results
  text_generated = []

  # Low temperatures results in more predictable text.
  # Higher temperatures results in more surprising text.
  # Experiment to find the best setting.
  temperature = 10.0

  # Here batch size == 1
  model.reset_states()
  for i in range(num_generate):
    predictions = model(input_eval)
    # remove the batch dimension
    predictions = tf.squeeze(predictions, 0)

    # using a categorical distribution to predict the character returned by the model
    predictions = predictions / temperature
    predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

    # We pass the predicted character as the next input to the model
    # along with the previous hidden state
    input_eval = tf.expand_dims([predicted_id], 0)

    text_generated.append(idx2char[predicted_id])

  return (start_string+ ''.join(text_generated))



array = []
array = (generate_text(model, start_string="debbie1"))
print(array)
array = array.split("\n")

np.savetxt('Rockyou_N.txt',array, fmt = "%s")
result_data2 = pd.read_csv('Rockyou_N.txt', header = None,
                           sep=" ", error_bad_lines=False,
                           encoding = "ISO-8859-1")

result_data2.to_csv('Rockyou_N.csv')



