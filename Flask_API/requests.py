# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:22:31 2023

@author: HP
"""

import requests
from data_input import data_in

URL='http://127.0.0.1:5000/predict'
headers={"Content-Type":"application/json"}
data={"input":data_in}

r=requests.get(URL,headers=headers,json=data)

r.json()