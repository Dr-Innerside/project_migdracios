from flask import Flask, render_template, request
from datetime import datetime


# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Dropout
# from tensorflow.keras.optimizers import Adam, SGD
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.models import load_model
# # from keras.applications import ResNet50
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import OneHotEncoder


app = Flask(__name__)


@app.route('/')
def home():
    return render_template({'index.html'})


@app.route('/upload', methods=["POST"])
def upload_image():
    file = request.files['file_give']
    extension = file.filename.split('.')[-1]
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d_$H$M$S')
    filename = f'{timestamp}.{extension}'
    save_to = f'img/{filename}'
    file.save(save_to)
    return save_to


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
