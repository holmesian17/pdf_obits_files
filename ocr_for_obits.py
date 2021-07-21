from PIL import Image
import pytesseract
import cv2
import os
import argparse
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
'''
folder=os.getcwd()
for file in folder:
        for filename in os.listdir():
                if '.jpg' in filename:
                        try:
                                print(filename)
                                image = cv2.imread(filename)
                                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                                filename = "{}.png".format(os.getpid())
                                cv2.imwrite(filename, gray)

                                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

                                text = pytesseract.image_to_string(Image.open(filename))
                                os.remove(filename)
                                text_split = text.split()
                                print(text_split[0:5])
                                #print(text)
                        except:
                                print(filename)
                                print("Couldn't get name")

# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
