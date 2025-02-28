import os
import csv
from datetime import timedelta,datetime
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pprint
#from scipy import interpolate

DATE1 = '2021-08-26'
DATE2 = '2021-08-27'

## 心拍数データの補間
##  - 補間の方法：scipy モジュール
##  - 補間の間隔：100 ミリ秒

## csv ファイルから生データの形に変換（心拍数のみを取り出す）
cwd = os.getcwd()
print(cwd)

fhdata1 = pd.read_csv("./data/{0}/{0}-heart.csv".format(DATE1))
fhdata2 = pd.read_csv("./data/{0}/{0}-heart.csv".format(DATE2))
fhdata = pd.concat((fhdata1,fhdata2))
#print(fhdata)
fl = os.listdir("./data/{0}/{0}-sleep".format(DATE2))
fsdata = []
for i in fl:
    fsdata.append(pd.read_csv("./data/{0}/{0}-sleep/".format(DATE2)+i))
#print(fsdata)
fsData = fsdata[0]
#print(fsData)
start = fsData.time[0]
print(start)
end = fsData.time[len(fsData.time)-1]
ht = [pd.to_datetime(i) for i in fhdata.time]    # timestamp
hv = [int(i) for i in fhdata.heart_rate]                # HR

h_data = pd.DataFrame(hv, columns = ['HR'], index = ht)
h_data = h_data[start:end]
#print(h_data)
ht = [str(i) for i in ht if datetime.strptime(start,'%Y-%m-%d %H:%M:%S')<=i<=datetime.strptime(end,'%Y-%m-%d %H:%M:%S')]
hv = h_data.HR.values.tolist()
print("心拍数")
print(ht)
print(hv)
st = list(fsData.time)
sv = list(fsData.sleep)
print("睡眠状態")
print(st)
print(sv)
