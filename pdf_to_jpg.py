from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import os

folder = os.getcwd()
print(folder)

for subdir, dirs, files in os.walk(folder):
    for subdir in dirs:
        print(subdir)
        for filename in os.listdir(subdir):
            part = os.path.join(folder, subdir)
            full = os.path.join(part, filename)
            
            print("Part", part)
            print("Full", full)
            print("filename", filename)
            
            image = convert_from_path(full)
            
            print(image)
            
            ready_name = filename.strip(".pdf")

            second_string = 'page'+ ready_name +'.jpg'
            right_path = os.path.join(part, second_string)
            
            print("Right path", right_path)
            for i in range(len(image)):
                
                image[i].save(right_path, 'JPEG')
