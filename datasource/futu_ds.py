from utils import futuUtils as fu
from futu import *
import pandas as pd


# 获取15分钟数据并保存
def get_week_and_save(code='', start='2021-01-01', end='2023-03-11'):
    ret, data, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_WEEK, start=start, end=end)
    if ret == RET_OK:
        print(data)
        print(type(data))
    else:
        print('error:', data)

    while page_req_key is not None:  # 请求后面的所有结果
        print('*************************************')
        ret, data1, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_WEEK, start=start,
                                                                          end=end,
                                                                          page_req_key=page_req_key)
        if ret == RET_OK:
            print(data1)
            data = pd.concat([data, data1], axis=0, ignore_index=True)
        else:
            print('error:', data)

    data.to_csv('../data/' + code + '_week.csv', encoding='utf-8-sig')


# 获取15分钟数据并保存
def get_day_and_save(code='', start='2020-01-01', end='2023-03-11'):
    ret, data, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_DAY, start=start, end=end)
    if ret == RET_OK:
        print(data)
        print(type(data))
    else:
        print('error:', data)

    while page_req_key is not None:  # 请求后面的所有结果
        print('*************************************')
        ret, data1, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_DAY, start=start,
                                                                          end=end,
                                                                          page_req_key=page_req_key)
        if ret == RET_OK:
            print(data1)
            data = pd.concat([data, data1], axis=0, ignore_index=True)
        else:
            print('error:', data)

    data.to_csv('../data/' + code + '_day.csv', encoding='utf-8-sig')


# 获取15分钟数据并保存
def get_15m_and_save(code='', start='2021-01-01', end='2023-03-11'):
    ret, data, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_15M, start=start, end=end)
    if ret == RET_OK:
        print(data)
        print(type(data))
    else:
        print('error:', data)

    while page_req_key is not None:  # 请求后面的所有结果
        print('*************************************')
        ret, data1, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_15M, start=start,
                                                                          end=end,
                                                                          page_req_key=page_req_key)
        if ret == RET_OK:
            print(data1)
            data = pd.concat([data, data1], axis=0, ignore_index=True)
        else:
            print('error:', data)

    data.to_csv('../data/' + code + '_15m.csv', encoding='utf-8-sig')


# 获取3分钟数据并保存
def get_3m_and_save(code='', start='2021-01-01', end='2023-03-11'):
    ret, data, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_3M, start=start, end=end)
    if ret == RET_OK:
        print(data)
        print(type(data))
    else:
        print('error:', data)

    while page_req_key is not None:  # 请求后面的所有结果
        print('*************************************')
        ret, data1, page_req_key = fu.quote_context.request_history_kline(code, ktype=KLType.K_3M, start=start,
                                                                          end=end,
                                                                          page_req_key=page_req_key)
        if ret == RET_OK:
            print(data1)
            data = pd.concat([data, data1], axis=0, ignore_index=True)
        else:
            print('error:', data)

    data.to_csv('../data/' + code + '_3m.csv', encoding='utf-8-sig')


# get_15m_and_save('HK.07226')  # 两倍看多恒生科技
# get_day_and_save('HK.07226')
# get_week_and_save('HK.07226')
# get_15m_and_save('HK.07552')  # 两倍看空恒生科技
# get_15m_and_save('SZ.300759')  # 康龙化成
# get_15m_and_save('SH.600702')  # 舍得酒业
# get_3m_and_save('HK.07552')
# get_day_and_save('SZ.300759')
get_day_and_save('SH.000300', start='2005-01-01')
get_15m_and_save('HK.03032')
