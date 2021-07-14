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
            #print("Part", part)
            print("Full", full)

            images = convert_from_path(full)
 
            for i in range(len(images)):
   
            # Save pages as images in the pdf
                images[i].save('page'+ str(i) +'.jpg', 'JPEG')
            
