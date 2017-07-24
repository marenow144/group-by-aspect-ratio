# improved-octo-meme

from PIL import Image
import os
import argparse
 
def process(input,output):
    for filename in os.listdir(input):
               try:
                img  = Image.open(os.path.join(input, filename))
                img.verify()
                img  = Image.open(os.path.join(input, filename))
                width, height = img.size
                aspect_ratio = width / height
                if aspect_ratio == 4 / 3 or aspect_ratio == 3 / 4:
                  if not os.path.exists(os.path.join(output,'4x3')):
                           os.makedirs(os.path.join(output,'4x3'))
                  img.save(os.path.join(output,'4x3', filename))
                elif aspect_ratio == 2 / 3 or aspect_ratio == 3 / 2:
                    if not os.path.exists(os.path.join(output,'2x3')):
                           os.makedirs(os.path.join(output,'2x3'))
                    img.save(os.path.join(output,'2x3', filename))
                elif aspect_ratio == 16 / 9 or aspect_ratio == 9 / 16:
                    if not os.path.exists(os.path.join(output,'16x9')):
                           os.makedirs(os.path.join(output,'16x9'))
                    img.save(os.path.join(output,'16x9', filename))
                elif aspect_ratio == 1:
                     if not os.path.exists(os.path.join(output,'1x1')):
                           os.makedirs(os.path.join(output,'1x1'))
                     img.save(os.path.join(output,'1x1', filename))
                else:
                    if not os.path.exists(os.path.join(output,'other')):
                           os.makedirs(os.path.join(output,'other'))
                    img.save(os.path.join(output,'other', filename))
               except Exception as err:
                    print("filename: {} has wrong format {}" .format(filename, err))


parser = argparse.ArgumentParser(description='Process some images')
parser.add_argument('--path')
args = parser.parse_args()
output=args.path
yes_or_no=input('Whould you like to use a custom output path ? (y/n)')
if yes_or_no=='n':
    output=args.path
if yes_or_no=='y':
    parser_2 = argparse.ArgumentParser(description='Process some images')
    parser_2.add_argument('--path')
    args_2 = parser_2.parse_args()
    output=args_2.path
process(input_path,output);


    #print(width)
    #print(height,'\n')
    
