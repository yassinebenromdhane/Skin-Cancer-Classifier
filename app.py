from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from main import getPrediction
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Save images to the 'static' folder as Flask serves images from this directory
UPLOAD_FOLDER = '/app/static/images/'

#Create an app object using the Flask class. 
app = Flask(__name__, static_folder="static")


app.secret_key = "kunal"

#Define the upload folder to save images uploaded by the user. 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMPLATES_FOLDER'] = 'templates/'

@app.route('/')
def index():
    return render_template('index.html')

#Add Post method to the decorator to allow for form submission. 
@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)  #Use this werkzeug method to secure filename. 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            label = getPrediction(filename)
            flash(label)
            print(label)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0')