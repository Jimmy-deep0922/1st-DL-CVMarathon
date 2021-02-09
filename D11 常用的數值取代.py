import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline                       

dir_data="D:\Machine Learning\機器學習百日馬拉松"

f_app = os.path.join(dir_data, 'application_train.csv')
print('Path of read in data: %s' % (f_app))
app_train = pd.read_csv(f_app, engine='python')
app_train.head()

# 如果欄位中有 NA, describe 會有問題

#app_train['AMT_ANNUITY'].describe()

# Ignore NA, 計算五值

#five_num=[0,25,50,75,100]
#quantile_5s=[np.percentile(app_train[~app_train['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'],q=i) for i in five_num]   #=> ~ 是反運算，會將原本的值 True/False 顛倒。
#
#app_train[~app_train['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'].hist(bins=100)
#plt.show()

#得到 median 的另外一種方法

#np.median(app_train[~app_train['AMT_ANNUITY'].isnull]()]['AMT_ANNUITY'])

# 計算眾數 (mode)

#from scipy.stats import mode
#import time
#
#start_time=time.time()
#mode_get=mode(app_train[~app_train['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'])
#print(mode_get)
#print("Elapsed time:%.3f secs" %(time.time()-start_time))

# 計算眾數 (mode)
# 較快速的方式

from collections import defaultdict

start_time=time.time()
mode_dict=defaultdict(lambda:0)

for value in app_train[~app_train['AMT_ANNUITY'].isnull()]['AMT_ANNUITY']:
    mode_dict[value]+=1

mode_get=sorted(mode_dict.items(),key=lambda kv:kv[1],reverse=True)
print(mode_get[0])
print("Elapsed time: %.3f secs" % (time.time() - start_time))









