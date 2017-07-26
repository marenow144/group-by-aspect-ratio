from PIL import Image
import os
import argparse
import shutil

def process(input,output):
    for filename in os.listdir(input):
               try:
                path = os.path.join(input, filename)
                img  = Image.open(path)
                img.verify()
                img  = Image.open(path)
                width, height = img.size
                aspect_ratio = round(width / height,2)
                if aspect_ratio == round(4 / 3,2) or aspect_ratio == round(3 / 4,2):
                  if not os.path.exists(os.path.join(output,'4x3')):
                           os.makedirs(os.path.join(output,'4x3'))
                  shutil.copy2(path, os.path.join(output,'4x3'))
                elif aspect_ratio == round(2 / 3,2) or aspect_ratio == round(3 / 2,2):
                    if not os.path.exists(os.path.join(output,'3x2')):
                           os.makedirs(os.path.join(output,'3x2'))
                    shutil.copy2(path, os.path.join(output,'3x2'))
                elif aspect_ratio == round(16 / 9,2) or aspect_ratio == round(9 / 16,2):
                    if not os.path.exists(os.path.join(output,'16x9')):
                           os.makedirs(os.path.join(output,'16x9'))
                    shutil.copy2(path, os.path.join(output,'16x9'))
                elif aspect_ratio == 1:
                     if not os.path.exists(os.path.join(output,'1x1')):
                           os.makedirs(os.path.join(output,'1x1'))
                     shutil.copy2(path, os.path.join(output,'1x1'))
                else:
                    if not os.path.exists(os.path.join(output,'other')):
                           os.makedirs(os.path.join(output,'other'))
                    shutil.copy2(path, os.path.join(output,'other'))
               except Exception as err:
                    print("filename: {} has wrong format {}" .format(filename, err))

parser = argparse.ArgumentParser(description='Process some images')
parser.add_argument('--path')
parser.add_argument('--target')

args = parser.parse_args()
if args.path:
    input_path=args.path
    output_path = args.target or input_path
    process(input_path, output_path);
else:
    print("Missing input path (use --path=xxx)")
    