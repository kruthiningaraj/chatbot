import random
import json
import numpy as np
import tensorflow as tf
from preprocess import bag_of_words, tokenize

model = tf.keras.models.load_model("models/chatbot_model.h5")
with open("data/intents.json") as file:
    intents = json.load(file)

words = []
classes = [intent['tag'] for intent in intents['intents']]
for intent in intents['intents']:
    for pattern in intent['patterns']:
        words.extend(tokenize(pattern))

def get_response(msg):
    bow = bag_of_words(tokenize(msg), words)
    res = model.predict(np.array([bow]))[0]
    idx = np.argmax(res)
    tag = classes[idx]
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that."
