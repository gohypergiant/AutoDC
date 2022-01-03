from logging import debug
import os
from app import app
import zipfile
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
import tempfile

# from data_processing import outlier_detection
# from data_processing import edge_case_selection
# from data_processing import data_augmentation



ALLOWED_EXTENSIONS = set(['zip'])

    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template('index.html')


@app.route('/upload/dataset', methods=['POST'])
def upload_dataset():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            outlier_data_percent = request.form.get("outlier_data_percent")
            non_outlier_data_percent = request.form.get("non_outlier_data_percent")
            augmentation_data_percent = request.form.get("augmentation_data_percent")
            
            
            tempfilename = tempfile.TemporaryDirectory(dir = app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(tempfilename.name, filename))
            zip_ref = zipfile.ZipFile(os.path.join(tempfilename.name, filename), 'r')
            zip_ref.extractall(tempfilename.name)
            
            outputtempfilename = tempfile.TemporaryDirectory(dir = tempfilename.name)
            input_path = tempfilename.name
            output_path = outputtempfilename.name

            print(tempfilename.name)
            print(outputtempfilename.name)

            # outlier_detection.outlierDetection(input_path,output_path)

            # edge_case_selection.edgeCaseSelection(input_path,output_path, non_outlier_data_percent , outlier_data_percent)

            # # noise, crop, vflip, rotate, saturation, brightness, scale
            # data_augmentation.imageAugmentation(input_path,output_path, augmentation_data_percent, "noise")

            zip_ref.close()
            return redirect(url_for('upload_file',
                                    filename=filename))
            
    # return render_template('index.html')
    resp = jsonify(success=False)
    resp.status_code = 405
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')