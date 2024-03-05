import sys
import os
import comtypes.client

def convert_to_pdf(pptx_path, pdf_path):
    input_file_path = pptx_path
    output_file_path = pdf_path
    
    input_file_path = os.path.abspath(input_file_path)
    output_file_path = os.path.abspath(output_file_path)
    
    comtypes.CoInitialize()
    
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    slides = powerpoint.Presentations.Open(input_file_path)
    
    slides.SaveAs(output_file_path, 32)
    
    slides.Close()
    os.remove(pptx_path)

    
    

