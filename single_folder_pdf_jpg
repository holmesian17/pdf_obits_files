from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import os

folder = os.getcwd()
print(folder)

for files in folder:
    for filename in os.listdir():
        full = os.path.join(folder, filename)
        #print("Part", part)
        print("Full", full)

        images = convert_from_path(full)
 
        for i in range(len(images)):
   
            images[i].save('page'+ str(i) +'.jpg', 'JPEG')
            
