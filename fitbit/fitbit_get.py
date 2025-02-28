import fitbit
import datetime
import numpy as np
import pandas as pd

if __name__ == '__main__':
        print("Module to get the data")

def heart_get(DATE,authd_client):
    # 心拍数を取得（1秒単位）
    data_sec = authd_client.intraday_time_series('activities/heart', DATE, detail_level='1sec') #'1sec', '1min', or '15min'fitbitmモジュールの関数，1秒毎の心拍数のデータを取得してる
    heart_sec = data_sec["activities-heart-intraday"]["dataset"] #辞書を内包したリスト
    heart_df = pd.DataFrame.from_dict(heart_sec)    #心拍数の2次元配列
    if not heart_df.empty:
        heart_df.time = pd.to_datetime([DATE + " " + t for t in heart_df.time])  #time行をdatetime型に
        heart_df = heart_df.rename(columns={'value': 'heart_rate'}) #データ改称
    return heart_df
def sleep_get(DATE,authd_client):
    data_sleep = authd_client.sleep(date=DATE)
    sleep = data_sleep["sleep"]
    sleep_dfs = []
    for i in sleep:
        start = pd.to_datetime(i["startTime"][0:10]+" "+i["startTime"][11:19])
        end = pd.to_datetime(i["endTime"][0:10]+" "+i["endTime"][11:19])
        sleep_rdata = [{"dateTime":str(start)[11:19],"value":0}]
        idx = [start]
        DATE2 = start.date()
        sleep_rdata += i["minuteData"]
        for j,k in zip(i["minuteData"],range(len(i["minuteData"]))):
            T_now = pd.to_datetime(str(DATE2)+" "+j["dateTime"])
            if T_now.time() < idx[k].time():
                T_now+=datetime.timedelta(days=1)
                DATE2+=datetime.timedelta(days=1)
            idx.append(T_now)
        sleep_rdata.append({"dateTime":str(end)[11:19],"value":4})
        idx.append(end)
        sleep_df = (pd.DataFrame.from_dict(sleep_rdata))    #睡眠状態の2次元配列
        if not sleep_df.empty:
            sleep_df.dateTime = idx    #time行をdatetime型に
            sleep_df = sleep_df.rename(columns={'value':'sleep','dateTime':'time'}) #データ改称
        sleep_dfs.append(sleep_df)
    return sleep_dfs

def CLIENT (CLIENT_ID,CLIENT_SECRET):
    # トークン(無効になったら再発行させてここに書き直してください)
    ACCESS_TOKEN =  "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM0I1WEQiLCJzdWIiOiI5SE1LU1QiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNjMyMDYyNTI4LCJpYXQiOjE2MzIwMzM3Mjh9.RJbP6-wu0XCGBbwMo7vPR94MP4HDXR_zIAouGIl2w4k"
    REFRESH_TOKEN =  "eef9a3b75fe93fbd852b4c9c4d4c34fb8affbc2d3387c40ab148655c2e26f35e"

    # ID等の設定
    authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET
                             ,access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN) #fitbitモジュールの関数への代入
    return authd_client
