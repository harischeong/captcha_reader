

import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr
import glob
import pathlib
from Levenshtein import distance as levenshtein_distance
import fastwer



class Tester(object):
    def __init__(self, paths_pred, paths_gt):
        self.paths_gt = paths_gt
        self.paths_pred = paths_pred
        
    def all_metrics(self):
        """
        This function returns the
        levenshtein distance, character
        error rate and word error rate.

        Returns:
        LD(float) - levenshtein distance
        CER(float) - character error rate
        WER(float) - word error rate
        """
        sum_LD = []
        sum_wer = []
        sum_cer = []
        
        for path_pred, path_gt in zip(self.paths_pred, self.paths_gt):
            with open(path_pred) as file_pred:
                with open(path_gt) as file_gt:
                    pred = file_pred.readline()
                    gt = file_gt.readline().replace("\n","")
                    sum_LD.append(levenshtein_distance(pred, gt))
                    sum_wer.append(fastwer.score([pred], [gt]))
                    sum_cer.append(fastwer.score([pred], [gt], char_level=True))

        return np.mean(np.array(sum_LD)), np.mean(np.array(sum_wer)), np.mean(np.array(sum_cer))
                    