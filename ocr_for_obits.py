from PIL import Image
import pytesseract
import cv2
import os
import argparse
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint


import spacy
from spacy import displacy
from collections import Counter
import en_core_web_trf

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
                        print(filename)
                        image = cv2.imread(filename)
                        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        filename = "{}.png".format(os.getpid())
                        cv2.imwrite(filename, gray)

                        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

                        text = pytesseract.image_to_string(Image.open(filename))
                        os.remove(filename)
                        text= text.strip('\n')                        
                        
                        nlp = en_core_web_trf.load()

                        doc=nlp(text)

                        people = []
                        
                        for X in doc.ents:
                                for word in X.text:
                                        if word.upper() == True:
                                                pass
                                if X.label_ == "PERSON":
                                      print(X.text, X.label_)
                                      break  
                        
                        #pprint([(X.text, X.label_) for X in doc.ents])

                        '''

                        text_split = text.split()
                        first_ten_words = text_split[0:10]
                        print("Original ten: ", first_ten_words)
                        first_ten_words = [i.replace('"',  '') for i in first_ten_words]
                        first_ten_words = [i.replace('”',  '') for i in first_ten_words]
                        first_ten_words = [i.replace('“',  '') for i in first_ten_words]
                        first_ten_words = [i.replace(',',  '') for i in first_ten_words]
                        first_ten_words = list(set(first_ten_words))
                        print("Duplicate words removed: ", first_ten_words)


                        first_ten_words = [item.capitalize() for item in first_ten_words]
                        first_ten_words = [item for item in first_ten_words if '~' not in item]
                        #print("No tildes: ", first_ten_words)
                        first_ten_words = [item for item in first_ten_words if item.isnumeric() == False]
                        #print("NaN: ", first_ten_words)
                        first_ten_words = [item for item in first_ten_words if any(chr.isdigit() for chr in item) == False]
                        #print("Na(ny)N: ", first_ten_words)
                        first_ten_words = [item for item in first_ten_words if 'of' not in item]
                        first_ten_words = [item for item in first_ten_words if 'and' not in item]
                        first_ten_words = [item for item in first_ten_words if 'the' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Fort' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Saturday' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Sunday' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Monday' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Tuesday' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Wednesday' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Thursday' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Friday' not in item]
                        first_ten_words = [item for item in first_ten_words if 'Collins' not in item]

                        first_names_list = []
                        last_names_list = []
                        middle_initial_list = []
                        fullname = []

                        for item in first_ten_words:
                                m = re.search('[A-Z][.]', item)
                                if item == m:
                                        middle_initial_list.append(item)
                                        print("Middle", item)
                                #regex single character not working yet 

                        for item in first_ten_words:
                                with open ('first_names.txt') as first_search:
                                        for line in first_search:
                                                line = line.rstrip()
                                                if item == line:
                                                        first_names_list.append(item)

                                with open ('last_names.txt') as last_search:
                                        for line in last_search:
                                                line = line.rstrip()
                                                if item == line and item.startswith("B")==True:
                                                        last_names_list.append(item)
                                                
                                
                        print("Last name: ", last_names_list)
                        print("First name: ", first_names_list)

                        for item in last_names_list:                                        
                                if item.startswith("B")==True:
                                        fullname.append(item)
                                else: pass
                                
                        for item in first_names_list:                                        
                                fullname.append(item) 
                        else: pass
                        
                        fullname = list(set(fullname))

                        print("Full name: ", fullname)
                        
                         
                        except:
                                print(filename)
                                print("Couldn't get text. Manually rename.")
                        
# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
'''
