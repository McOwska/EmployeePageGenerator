from flask import Flask, request, jsonify
from flask_cors import CORS
from page_generator import create_pptx
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
CORS(app, supports_credentials=True, expose_headers=["Content-Disposition"])

# Ensure you have a folder named 'uploads' in your project directory or change this path accordingly
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/create_page', methods=["POST"])
def create_page():
    # Access form data fields
    type_ = request.form['type']
    name = request.form['name']
    position = request.form['position'] if 'position' in request.form else None
    localization = request.form['localization'] if 'localization' in request.form else None
    description = request.form['description'] if 'description' in request.form else None

    file = request.files['image'] if 'image' in request.files else None
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

    if type_ == "New Employee":
        template_path = './templates/blue_1_kopia.pptx'
    elif type_ == "Current Employee":
        template_path = './templates/green_1.pptx'
    else:
        template_path = './templates/orange_1.pptx'

    output_path = './output.pptx'
    
    data = {
        'type': type_,
        'name': name,
        'position': position,
        'localization': localization,
        'description': description,
        'image_path': file_path if file else None
    }
    create_pptx(data, template_path, output_path, file_path)
    
    return "Success", 200

if __name__ == "__main__":
    app.run(debug=True)

