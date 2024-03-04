from pptx import Presentation
import json
   
def modify_pptx(type, template_path, output_path, replacements):
    if type == "1":
        replacements = {
            "Name": replacements["Name"],
        }
        
    ppt = Presentation(template_path)
    for slide in ppt.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        for key, value in replacements.items():
                            if key in run.text:
                                run.text = run.text.replace(key, value)
    ppt.save(output_path)

def create_pptx(data, template_path, output_path):
    replacements = {
        "Name": data["name"],
        "Position": data["position"],
        "Description": data["description"],
    }
    type = data["type"]
    modify_pptx(type, template_path, output_path, replacements)
    
    
    
    
