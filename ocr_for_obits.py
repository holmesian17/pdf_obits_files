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

import glob
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_trf

folder=os.getcwd()
people = {}

def get_name():
        number_of_files = len(glob.glob1('.',"*.jpg"))
        i = 0

        for file in os.walk('.'):
                for filename in os.listdir():
                        if '.jpg' in filename:
                                if i <= number_of_files:
                                        #print(filename)
                                        jpg_name = filename
                                        image = cv2.imread(filename)
                                        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                                        filename = "{}.png".format(os.getpid())
                                        cv2.imwrite(filename, gray)

                                        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

                                        text = pytesseract.image_to_string(Image.open(filename))
                                        os.remove(filename)
                                        text= text.replace('\n', ' ')                        
                                        
                                        nlp = en_core_web_trf.load()

                                        doc=nlp(text)

                                        
                                        
                                        for X in doc.ents:
                 
                                                if X.label_ == "PERSON":
                                                        print(jpg_name, X.text)
                                                        people[jpg_name] = X.text
                                                        
                                                        break
                                        i += 1
                                        print(i)
                                        
                                        

        
def check_dict():
        for k, v in people.items():
                i = 1
                if v.isupper == True:
                        people[k] = "Manual rename" + i

                        i = i + 1
                elif len(v) <= 1:
                        people[k] = "Manual rename" + i

                        i = i + 1
                vlist = v.split()
                v = vlist[-1:] + vlist[:-1]
                str1 = " "
                v = str1.join(v)
                people[k] = v


                
def check_results():
        print(people)

get_name()
check_dict()
check_results()
'''

                        text_split = text.split()
                        first_ten_words = text_split[0:10]
                        print("Original ten: ", first_ten_words)
                        first_ten_words = [i.replace('"',  '') for i in first_ten_words]
                        first_ten_words = [i.replace('???',  '') for i in first_ten_words]
                        first_ten_words = [i.replace('???',  '') for i in first_ten_words]
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
