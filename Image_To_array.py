import cv2
import numpy as np

class ImageToArray():
    def __init__(self,img):
        self.img = img
        self.extension_list = ['png','jpg','jpeg','tiff','bmp']
    def convert_to_rgb(self):
        name,ext = self.img.split('.')
        if ext in self.extension_list:
            try:
                img_array = cv2.imread(self.img)
                return img_array
            except Exception as e:
                print(e)
                return [[]]
        else:
            print("Invalid Format")
            return [[]]
        
    def convert_to_greyscale(self):
        name,ext = self.img.split('.')
        if ext in self.extension_list:
            try:
                img_array = cv2.imread(self.img,0)
                return img_array
            except Exception as e:
                print(e)
                return [[]]
        else:
            print("Invalid Format")
            return [[]]

if __name__ == "__main__":
    file_name = str(input())
    img = ImageToArray(file_name)
    data = img.convert_to_greyscale()
    print(data)