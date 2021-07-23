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
                        #print(filename)
                        image = cv2.imread(filename)
                        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        filename = "{}.png".format(os.getpid())
                        cv2.imwrite(filename, gray)

                        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

                        text = pytesseract.image_to_string(Image.open(filename))
                        os.remove(filename)
                        text_split = text.split()
                        first_ten_words = text_split[0:10]
                        print("Original ten: ", first_ten_words)
                        first_ten_words = [i.replace('"',  '~') for i in first_ten_words]
                        first_ten_words = [i.replace('”',  '~') for i in first_ten_words]
                        first_ten_words = [i.replace('“',  '~') for i in first_ten_words]
                        first_ten_words = list(set(first_ten_words))
                        print("Duplicate words removed: ", first_ten_words)

                        first_ten_copy = first_ten_words
                        
                        for item in first_ten_copy:
                                item=item.lower()
                                item=item.capitalize()
                                print("This word is: ", item)
                                if '~' in item:
                                        print("Has carots: ", item)
                                        first_ten_copy.remove(item)
                                elif item.isnumeric() == True:
                                        print("This is a number: ", item)
                                        first_ten_copy.remove(item)
                                elif any(chr.isdigit() for chr in item) == True:
                                        print("Has digits: ", item)
                                        first_ten_copy.remove(item)
                                else:
                                        pass
                        print("Final result: ", first_ten_copy)
                                
                        
                        '''
                        first_name = open("C:\\Documents\first_names.txt", "r")
                        last_name = open("C:\\Documents\last_names.txt", "r")
                        
                        first_names_list = []
                        last_names_list = []
                        fullname = []
                        
                        for item in first_ten_words:
                                if item in first_name:
                                        first_names_list.add(item)
                                elif item in last_name:
                                        last_names_list.add(item)
                                else:
                                        pass
                        if item.startswith("B") in last_names_list:
                                fullname.append[item]
                        else:
                                pass
                                     
                        except:
                                print(filename)
                                print("Couldn't get text. Manually rename.")
                        '''
# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
