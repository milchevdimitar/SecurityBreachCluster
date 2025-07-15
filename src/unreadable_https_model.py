import tensorflow as tf
import numpy as np
import os

class UnreadableHttpsModel:
    def __init__(self, model_path='unreadable_model.h5', input_shape=8):
        self.model_path = model_path
        self.input_shape = input_shape
        self.model = self._load_or_create_model()

    def _load_or_create_model(self):
        if os.path.exists(self.model_path):
            print(f"Loading unreadable model from {self.model_path}")
            return tf.keras.models.load_model(self.model_path)
        else:
            print("Creating new unreadable model")
            model = tf.keras.Sequential([
                tf.keras.layers.Dense(64, activation='relu', input_shape=(self.input_shape,)),
                tf.keras.layers.Dropout(0.2),
                tf.keras.layers.Dense(32, activation='relu'),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
            return model

    def predict(self, features):
        features = np.array(features).reshape(1, -1)
        pred = self.model.predict(features, verbose=0)[0][0]
        return pred

    def update(self, features, label):
        features = np.array(features).reshape(1, -1)
        label = np.array([label])
        self.model.fit(features, label, epochs=1, verbose=0)
        self.model.save(self.model_path)