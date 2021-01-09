# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:38:54 2021

@author: Jishnu

Decrypt pdf files
"""
import pikepdf
import os
from os import path
from glob import glob 

filepath= "G:\Developments\Decrypt pdf"
os.chdir(filepath)

# function to lIST all files in the dir
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

# List all pdf files in the dir
k=find_ext(".","pdf")

# viterate over list k to decrypt all pdf
for i in k:
    file_name=i.split(".")
    pdf = pikepdf.open("."+file_name[1]+".pdf")
    pdf.save("."+file_name[1]+"_decrypt.pdf")