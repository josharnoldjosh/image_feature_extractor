#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:27:54 2018

@author: josharnold
"""

with open('extracted_image_features.pkl', 'rb') as f:
    extracted_image_features = pickle.load(f)
    print(extracted_image_features)