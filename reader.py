import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr
import glob
import pathlib
from Levenshtein import distance as levenshtein_distance
import fastwer



class Captcha(object):
    def __init__(self):
        self.reader = easyocr.Reader(['en'])
        
    def __call__(self, im_path, save_path):
        """
        Algo for inference
        args:
        im_path: .jpg image path to load and to infer
        save_path: output file path to save the one-line outcome
        """
        img = plt.imread(im_path)
        results = self.reader.readtext(img)
        text = results[0][1]
        save_path = pathlib.Path(save_path)
        with open(str(save_path), "w") as file1:
            file1.write(text.upper())