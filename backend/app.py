from flask import Flask, request, jsonify
from flask_cors import CORS
from page_generator import create_pptx
import os

app = Flask(__name__)
CORS(app, supports_credentials=True, expose_headers=["Content-Disposition"])

@app.route('/create_pptx', methods=["POST"])
def create_page():
    data = request.json
    
    if data['type'] == "New Employee":
        template_path = './templates/blue_1.pptx'
    elif data['type'] == "Current Employee":
        template_path = './templates/green_1.pptx'
    else:
        template_path = './templates/orange_1.pptx'
    
    output_path = './output.pptx'
    
    create_pptx(data, template_path, output_path)
    
    return "Success", 200
