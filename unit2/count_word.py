# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:58:35 2020

@author: xxt
"""
from os.path import *
file_name = "C:\\Users\\xxt\\Desktop\\SES2020spring\\unit2\\readme.md"
def count_char(f):
    try:    
        with open(f,'r') as fh:
            contents = fh.read()
    except FileNotFoundError:
        msg = "sorry, the file does not exit."
        print(msg)
    else:
        print(contents)
        #计算有多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file readme has about " + str(num_words) + ' words.')
        
count_char(file_name)