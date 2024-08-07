from pprint import pprint
import requests
import numpy as np
import pandas as pn

r = requests.get('https://api.github.com/events')
r1 = r.json()
print(r.status_code)
print(r.headers)
print(r.text)
pprint(r1)


# data1 = [1, 2, 3, 4, 5]
# data2 = [6, 7, 8, 9, 10]
# arr1 = np.array(data1)
# arr2 = np.array(data2)
#
# print(arr1)
# print(np.sqrt(arr1))
# print(np.sin(arr1))
# print(np.cos(arr1))
# print(arr1 + arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 * 2)
# print(arr1 ** 2)
#
# rr = pn.read_excel('simple_files.xlsx')
# print(rr)
# print(rr.info)
# print(rr.describe())
# print(rr.shape)
# print(rr.ndim)
# print(rr.size)
# print(rr['sex'].value_counts())
# print(rr['address'].nunique())
# print(rr['weight'].unique())
