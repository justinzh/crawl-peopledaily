import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json('/Users/justin/Documents/Scraper/myfirstscrapy/peopledaily_1989.json')
data.set_index('date', inplace=True)
data['mao'] = data.content.str.count('毛泽东')
data['deng'] = data.content.str.count('邓小平')   
data['wangzhen'] = data.content.str.count('王震') 

data['jiang'] = data.content.str.count('江泽民')
data['lipeng'] = data.content.str.count('李鹏')   
data['hu'] = data.content.str.count('胡锦涛')   
data['wen'] = data.content.str.count('温家宝')   
data['xi'] = data.content.str.count('习近平')   
data['likeqiang'] = data.content.str.count('李克强')   
data['zhu'] = data.content.str.count('朱镕基')    

counts = data.drop(['location', 'tags', 'title', 'id'], axis = 1)   
counts_d = counts.resample('D').sum()

# political power switch over chart
ax = counts_d[['jiang', 'hu', 'xi']].rolling(180, win_type='gaussian', center=True).sum(std=180).plot(xlabel='time', ylabel='name occurance count')   
ax.legend(['Jiang Zemin', 'Hu Jintao', 'Xi Jinping'])

# mao / deng influence chart
ax = counts_d[['mao', 'deng']].rolling(180, win_type='gaussian', center=True).sum(std=180).plot(xlabel='time', ylabel='name occurance count')   
ax.legend(['mao', 'deng'])
marker = [pd.to_datetime('10/03/1993'), pd.to_datetime('02/19/1997'), pd.to_datetime('08/03/2004'), pd.to_datetime('12/30/2013'), pd.to_datetime('06/03/2014')]
for i, d in enumerate(marker):
    plt.axvline(d, color = 'orange', linestyle=':')
    plt.text(d, 120 - i* 20, d.strftime('%m/%d/%Y'), fontsize='8')
plt.text(pd.to_datetime('1997-2-19'), 96, 'Deng diseased on 2/19/1997', rotation=0, fontsize='8')

ax = counts_d[['jiang', 'zhu', 'hu', 'wen', 'xi', 'li']].rolling(180, win_type='gaussian', center=True).sum(std=180).plot(xlabel='time', ylabel='name occurance count')   
ax.legend(['Jiang Zemin', 'Zhu Rongji', 'Hu Jintao', 'Wen Jiabao', 'Xi Jinping', 'Li keqiang'])

count_comp = counts_d[['jiang', 'zhu', 'hu', 'wen', 'xi', 'likeqiang']].rolling(180, win_type='gaussian', center=True).sum(std=180)    
fig, ax = plt.subplots(3, sharex = True)
fig.suptitle('Comparison on the same government')
ax[2].plot(count_comp.index, count_comp['xi'], count_comp['likeqiang']); ax[2].legend(['Xi Jinping', 'Li Keqiang'])
ax[1].plot(count_comp.index, count_comp['hu'], count_comp['wen']); ax[1].legend(['Hu Jiangtao', 'Wu Jiabao'])
ax[0].plot(count_comp.index, count_comp['jiang'], count_comp['zhu']); ax[0].legend(['Jiang Zemin', 'Zhu Rongji'])

  


