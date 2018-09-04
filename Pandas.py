
# coding: utf-8

# In[1]:


import pandas as pd


# # pandas的資料結構
# 
# #### 1.Series：用來處理時間序列相關的資料(如感測器資料等)，主要為建立索引的一維陣列。
# #### 2.DataFrame：用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV 等等。
# #### 3.Panel：用來處理有資料及索引、列索引與欄標籤的三維資料集。

# In[3]:


#Series
# input is an array

cars = ["BMW", "BENZ", "Toyota", "Nissan", "Lexus"]
select = pd.Series(cars)
print(select)


# In[11]:


# input is a dictionary

dictionaries = {  
        "factory": "Taipei",
        "sensor1": "1",
        "sensor2": "2",
        "sensor3": "3",
        "sensor4": "4",
        "sensor5": "5"
        }

select = pd.Series(dictionaries, index = dictionaries.keys()) # 排序與原 dict 相同
print(select)
print('='*20, 'use index to access values')
print(select[0])
print('='*20, 'use keys to access values')
print(select['sensor1'])
print('='*20, 'use multiple index to access key-value')
print(select[[0, 2, 4]])
print('='*20, 'use multiple keys to access values')
print(select[['factory', 'sensor1', 'sensor3']])  
print('='*20, 'use slice to select partial value')
print(select[:2])
print('='*20, 'use slice to select partial value')
print(select['sensor2':])
#%%

# input is a single data

cars = "Benz"
select = pd.Series(cars, index = range(3))
print(select)

#%%

# DataFrame
## data is dictionary
group = ["Movies", "Sports", "Coding", "Fishing",
        "Dancing", "cooking"]

num = [46, 8, 12, 12, 6, 58]

dictionary = {"groups": group,
                "num":num}

select_df = pd.DataFrame(dictionary)
select_df

#%%
## data is an array
arr = [["Movies", 46], ["Sports", 8], ["Coding", 7], ["Fishing", 12]]
df = pd.DataFrame(arr, columns = ["name", "num"])
df

#%%
print(select_df.shape)
print("===========")
print(select_df.describe())
print("===========")
print(select_df.tail(3))
print("===========")
print(select_df.columns)
print("===========")
print(select_df.index)
print("===========")
print(select_df.info)

#%%
# chose elements
# df.iloc[index of row, index of column]
print('======選第一列第二欄========')
print(select_df.iloc[0, 1])
print('======選第一到第二列的組名與人數========')
print(select_df.iloc[0:2, :])
print('======選第二欄:各組的人數========')
print(select_df.iloc[:, 1])
print('======各組人數========')
print(select_df["num"])
print('======各組人數========')
print(select_df.num)

#%%
# use boolean to filter
# df.loc[index of row, name of column]

#選出超過10人的群組
out_df = select_df[select_df.loc[:, "num"] > 10]
print(out_df)

#%%
# sort by index
select_df.sort_index(axis = 0, ascending = True)

# sort by value
select_df.sort_values(by = 'num')

#%%
# ## finding missing value
df = pd.read_csv('Pandas-Practice\shop_list2.csv')
print(df)
print("======")
# find where is missing value and return boolean
print(df[df.loc[:, "shop name"].isnull()])
print("======")
print(df[df.loc[:, "maket size"].notnull()])

# ## missing value handling
print("======")
print(df)
print("===drop this row if there is a missing value===")
drop_value = df.dropna()
print(drop_value)
print("===fill missing value with 0===")
filled_value = df.fillna(0)
print(filled_value)
print("===fill value according to columns==")
filled_value_column = df.fillna({"shop name":"Null", "maket size":0})
print(filled_value_column)