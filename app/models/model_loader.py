
import tensorflow as tf
print(tf.__version__)  # Should be 2.12.0

model = tf.keras.models.load_model('app/models/mole_classifier_model.keras')
model.summary()

