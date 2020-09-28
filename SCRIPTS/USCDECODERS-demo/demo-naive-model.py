import os,sys,time
import config

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

print(f'Reading from -> {config.PROCESSED}')
time.sleep(1)


train_ds=tf.keras.preprocessing.image_dataset_from_directory(config.PROCESSED,
	seed=100,validation_split=0.8,subset='training',color_mode='grayscale')

validation_ds=tf.keras.preprocessing.image_dataset_from_directory(config.PROCESSED,
	seed=100,validation_split=0.2,subset='validation',color_mode='grayscale')

class_names = train_ds.class_names
print(class_names)



### CACHE AND PREFETCH FOR OVERCOMING DISK I/O 

AUTOTUNE = tf.data.experimental.AUTOTUNE
train_ds = train_ds.cache().shuffle(700).prefetch(buffer_size=AUTOTUNE)
val_ds = validation_ds.cache().prefetch(buffer_size=AUTOTUNE)

#### Main Modeling ####

batch_size = 16
img_height = 256
img_width = 256
img_channels=1 # grayscale

num_classes = len(class_names)

model = Sequential([
  layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, img_channels)),
  layers.Conv2D(16, 4, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 4, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 16, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(32, activation='relu'),
  layers.Dense(num_classes)
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

epochs=10
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs,
  batch_size=batch_size,
)

