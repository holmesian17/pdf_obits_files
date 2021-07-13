# pdf_obits_files

pdf_quick_split calls organize.bat as part of its process, so make sure both are in the folder you want to run them in

next step is to, ideally, auto rotate the pdfs so that the text is right side up

then convert them to images and use opencv to find the bold text, extract it, OCR for names, check confidence of names 
(mark ones with certain confidence level to be checked by me), and change filename to lastname, firstname
