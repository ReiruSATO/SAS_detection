import fitbit
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from ast import literal_eval
import datetime
from fitbit_get import CLIENT,heart_get,sleep_get
import os
import shutil
from time import sleep
#from indexdatetime import reidx
#%matplotlib inline #プロット出力が表示され、ノートブック内に保存される(静的な画像のみで描画)，環境によっては必要なし

# メモしたID等
CLIENT_ID =  "23B5XD"
CLIENT_SECRET  = "668b40e0ed516f9c1ec76382f724b1a5"

# 取得したい日付

DATE = "2021-09-12" #取り出す最初の日付

# ID等の設定
authd_client = CLIENT(CLIENT_ID,CLIENT_SECRET)

#for counter in [1]:
while datetime.datetime.strptime(DATE,"%Y-%m-%d") <= datetime.datetime.today():#今日まで繰り返す
    os.makedirs("./data/"+DATE, exist_ok=True)                                 #DATA内に/(日付)/というフォルダがなかったら追加する
#    if os.path.isdir("./data/"+DATE+"/"+DATE+"-sleep")==True:
#        print("true")
#        shutil.rmtree("./data/"+DATE+"/"+DATE+"-sleep")
    os.makedirs("./data/"+DATE+"/"+DATE+"-sleep", exist_ok=True)
    heart_df = heart_get(DATE,authd_client)                                    #心拍数ゲット(Dataframe)
    heart_df.to_csv("./data/"+DATE+"/"+DATE+"-heart.csv",index=False)          #ディレクトリ内にcsvファイルとして追加
    sleep_data = sleep_get(DATE,authd_client)                                  #睡眠データゲット(Dataframeが入ったリスト)
#    for i in [1]:
    for i in range(len(sleep_data)):
        sleep_df = sleep_data[i]
        print(DATE,"\n",i,"\n",sleep_df)
        sleep_df.to_csv("./data/"+DATE+"/"+DATE+"-sleep/"+DATE+"-sleep"+str(i)+".csv",index=False)  #睡眠毎に番号付けてファイルに
    print(DATE+"済")
    DATETIME = datetime.datetime.strptime(DATE,"%Y-%m-%d") + datetime.timedelta(days=1) #1日後
    DATE = DATETIME.strftime("%Y-%m-%d")
    sleep(3)
#        sleep_df.to_csv("./data/"+DATE+"/"+DATE+"-sleep.csv")
    #sleep_df.sleep=pd.to_numeric(sleep_df.sleep)
    #mydata_df = heart_df.merge(sleep_df,how='outer')
    #mydata_df = mydata_df.sort_index()
    #print(mydata_df)
