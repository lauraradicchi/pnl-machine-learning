#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:28:47 2019

@author: laura.radicchi1
"""

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#importing dataset
otdataset = pd.read_csv('Data.csv')
x = otdataset.iloc[: , :-1].values
y = otdataset.iloc[: , 3].values
