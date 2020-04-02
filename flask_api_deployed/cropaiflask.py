# Import required libraries.
import os
import tensorflow as tf
from flask import request, render_template, Flask
from werkzeug.utils import secure_filename
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array 
import numpy as np
import keras
import time
from base64 import decodestring

# Generate timestamp.
timestr = time.strftime("%Y%m%d-%H%M%S")
print(timestr)

# Supress tensorflow logging messages.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
"""
0 = all messages are logged (default behavior)
1 = INFO messages are not printed
2 = INFO and WARNING messages are not printed
3 = INFO, WARNING, and ERROR messages are not printed
"""

# Limit Tensorflow GPU memory usage.
# Allocate 3GB VRAM and set memory growth to TRUE.
GPU = tf.config.experimental.list_physical_devices('GPU')
if GPU:
 try:
    for gpu in GPU:
        tf.config.experimental.set_memory_growth(gpu, True)
        tf.config.experimental.VirtualDeviceConfiguration(memory_limit = (1024*3))
 except RuntimeError as e:
    print(e)

# Locate saved model.
model_file = "CropAI_model_train_gen_epoch_5.h5"

# App configrations.
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xecsd]/'
app.config['UPLOAD_FOLDER'] = 'static'

# Result dictionary to be sent to HTML.
results = {'PATH': 0, 'PREDICTION': 0}

@app.route('/upload',methods=['POST'])
# Prediction function.
def predict():
    model = tf.keras.models.load_model(model_file) # Load the model.
    img_path = os.path.join('static',str(str(timestr)+'.png'))

    # The function below decoed the base64 string and saves the image to static folder.
    with open(img_path,"wb") as f: 
        f.write(decodestring(request.form['image_data'])) 

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = img_to_array(img) # Convert the images into NumPy array.
    img_array = np.expand_dims(img_array, axis=0)
    #img_array /= 255.0
    predictions = model.predict(img_array)
    print(predictions)

    index = np.argmax(predictions[0]) # Sort the predictions in descending order.
    print(index)
    number_to_label = ['Tomato Target Spot', 'Tomato Septoria leaf spot', 'Pepper bell Bacterial spot', 'Tomato healthy', 'Tomato Early blight', 'Potato Late blight', 'Potato Early blight', 'Pepper bell healthy', 'Tomato Leaf Mold', 'Tomato Bacterial spot', 
                                'Tomato mosaic virus', 'Tomato Yellow Leaf Curl Virus', 'Tomato Spider mites Two spotted spider mite', 'Tomato Late blight', 'Potato healthy']
    print(number_to_label[index])

    results = {'PATH': img_path, 'PREDICTION': number_to_label[index]}
    return results

# Define functions to be executed at endpoints.
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        try:
            image = request.files['file']   # Get the file.
            filename = timestr + secure_filename(image.filename)  # Get secured file name and add timestamp to make it unique.
            image.save(os.path.join('static', filename))
            path = os.path.join('static', filename)
            result = predict(base64file=path) # Send the image to prediction algorithm.
            return render_template('index.html', res=result)
        except:
            return render_template('index.html', res=results)

    return render_template('index.html', res=results)

# Run app.
if __name__ == '__main__':
    app.run(debug = True)