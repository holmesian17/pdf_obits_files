from PyPDF2 import PdfFileWriter, PdfFileReader
from subprocess import Popen
import os
import time

folder = os.getcwd()
print(folder)
org_file = folder + "\organize.bat"
print(org_file)
p = Popen(["organize.bat", org_file])
stdout, stderr = p.communicate()

time.sleep(5)

for subdir, dirs, files in os.walk(folder):
    for subdir in dirs:
        print(subdir)
        for filename in os.listdir(subdir):
            part = os.path.join(folder, subdir)
            full = os.path.join(part, filename)
            print(part)
            print(full)
            inputpdf = PdfFileReader(open(full, "rb"))
            for i in range(inputpdf.numPages):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                output_name = os.path.join(part,str(i))
                output_name = output_name + ".pdf"
                print(output_name)
                with open(output_name, "wb") as outputStream:
                    output.write(outputStream)
