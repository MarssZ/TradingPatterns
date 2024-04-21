from tradingpatterns.hard_data import generate_sample_df_with_pattern
from tradingpatterns.tradingpatterns import detect_head_shoulder
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd


def test_detect_head_shoulder():
    # Read data from a CSV file using pandas
    df = pd.read_csv('Data/BTCUSDT_D.csv')

    # Rest of the code...
    df_with_detection = detect_head_shoulder(df)
    df_with_inv_detection = detect_head_shoulder(df)
    assert "Head and Shoulder" in df_with_detection['head_shoulder_pattern'].values
    assert "Inverse Head and Shoulder" in df_with_inv_detection['head_shoulder_pattern'].values
 
    #把df的date列转化为DatetimeIndex
    df_with_detection['date'] = pd.to_datetime(df_with_detection['date'])
    df_with_detection.set_index('date', inplace=True)

    # 创建一个新的Series，长度与df_with_detection相同，但只在'head_shoulder_pattern'列不为na的位置有值
    dot_head_shoulder_pattern = df_with_detection['Close'].where(df_with_detection['head_shoulder_pattern'].notna())

    # 创建一个新的addplot参数，其中包含你想要突出显示的点
    ap = [mpf.make_addplot(dot_head_shoulder_pattern, type='scatter', markersize=10, marker='^', color='blue')]

    # 在蜡烛图上绘制头肩形态的点
    mpf.plot(df_with_detection, type='candle', style='charles',
         title='Candlestick chart',
         ylabel='Price',
         volume=True,
         addplot=ap)


test_detect_head_shoulder()


