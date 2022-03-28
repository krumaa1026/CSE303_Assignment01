#%%
# 2018-2-60-009
# Lab Assignment -1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("dataset_lab04.csv")
df.info()

#%%
# Task1
def lab04_task1_2018_2_60_009():
    print(f'Number of rows:{df.shape[0]}')
    print(f'Number of columns: {df.shape[1]}')
    
#%%
lab04_task1_2018_2_60_009()

#%%
# Task2
def lab04_task2_2018_2_60_009():
    print(f"Summary of time: {df['Time'].describe()}")
    print(f"Summary of Amount: {df['Amount'].describe()}")
#%%
lab04_task2_2018_2_60_009()
#%%
# Task3
def lab04_task3_2018_2_60_009():
    print(f"mean of amount: {df['Amount'].mean()}\n mean of Time : {df['Time'].mean()}")
    print(f"median of amount: {df['Amount'].median()}\n median of Time : {df['Time'].median()}")
    print(f"variance of amount: {df['Amount'].var()}\n variance of Time : {df['Time'].var()}")
    print(f"Standard deviation of amount: {df['Amount'].std()}\n Standard deviation of Time : {df['Time'].std()}")
#%%
lab04_task3_2018_2_60_009()
#%%
#Task 4
def lab04_task4_2018_2_60_009():
    df.boxplot(column = ['Time','Amount'])
    Q1_T = df['Time'].quantile(0.25)
    Q1_A = df['Amount'].quantile(0.25)
    med_T = df['Time'].quantile(0.50)
    med_A = df[['Amount']].quantile(0.50)
    Q3_T = df['Time'].quantile(0.75)
    Q3_A = df[['Amount']].quantile(0.75)
    IQR_T =Q3_T - Q1_T
    IQR_A = Q3_A - Q1_A
    print(f"Q1 of Time: {Q1_T}\nQ1 of Amount: {Q1_A}")
    print(f"Median of Time: {med_T}\nMedian of Amount: {med_A}")
    print(f"Q3 of Time: {Q3_T}\nQ3 of Amount: {Q3_A}")
    print(f"IQR of Time: {IQR_T}\n IQR of Amount: {IQR_A}")
    print('Amount column have a Outlier because because it has some value outside of whisker')
    print('Time has no outlier. Because it has no value outside of the whisker')
        
#%% 
lab04_task4_2018_2_60_009()
#%%
#Task 5
def lab04_task5_2018_2_60_009():
    df.hist(column = ['Time'])
    df.hist(column = ['Amount'])
    print(f"Skewness of Time: {df['Time'].skew()}\nKurtosis of Time:{df['Time'].kurt()}")
    print(f"Skewness of Amount:{df['Amount'].skew()}\nKurtosis of Amount:{df['Amount'].kurt()}")
    print("Skewness of Time is negative Skewed Because its value is less than zero and and distribution is too flat because it is less than -1 ")
    print("Skewness of amount is Positive Skewed Because its value is greater than zero and and distribution is too peaked because it is greater than +1 ")
    
#%%
lab04_task5_2018_2_60_009()
#%%
# Task 6
def lab04_task6_2018_2_60_009():
    df1 = df.query('Class == 0')
    df2= df.query('Class == 1')

    total = len(df)
    check1 = len(df1)
    check2 = len(df2)
    n_f = (check1/total*100)
    f = (check2/total*100)
    print("Non-Fraudulent:",n_f)
    print("Fraudulent:",f)
#%%
lab04_task6_2018_2_60_009()
#%%
# Task 7
def lab04_task7_2018_2_60_009():
    df['Class'].value_counts().plot(kind='hist')
#%%
lab04_task7_2018_2_60_009()
#%%
# Task 8
def lab04_task8_2018_2_60_009():
    x1 = df.loc[df['Class']==0]
    y1 = df.loc[df['Class']==1]
    z = x1.size*100/df.size
    o = y1.size*100/df.size
    x2 = [1,2]
    y2 = [z,o]
    tick_label = ['zero', 'one']
    plt.bar(x2,y2,tick_label=tick_label,width= 0.4,color=['green','red'])
    plt.xlabel('Class')
    plt.ylabel('Percentage')
    plt.show()
#%%
lab04_task8_2018_2_60_009()
#%%
# Task 9
def lab04_Task9_2018_2_60_009():
    df.hist(column=['V1'], bins = 50)
    print('V1" column is negetively skeweed')
    df.hist(column=['V2'], bins = 50)
    print('"V2" column is positively skeweed')
    df.hist(column=['V3'], bins = 50)
    print('V3 column is "platykurtic".')
    df.hist(column=['V4'], bins = 50)
    print('V4 column is "leptokurtic".')
    plt.show()
#%%
lab04_Task9_2018_2_60_009()
#%% 
# Task 10
def lab04_Task10_2018_2_60_009():
    corr_matrix = df.corr().abs()
    x = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k = 1)
    .astype(np.bool))
    to_drop = [column for column in x
    .columns if any(x[column] > 0.95)]
    df.drop(to_drop, axis = 1, inplace = True)
    print(x)
#%%
lab04_Task10_2018_2_60_009()
#%%
# Task 11
def lab04_Task11_2018_2_60_009():
     df.plot.scatter(x=['Time'], y=['V2'])
 
#%%
lab04_Task11_2018_2_60_009()
#%%
# Task 12
def lab04_Task12_2018_2_60_009():
    min_value = 100000
    
    for i in df.columns:
        for j in df.columns:
            if i == j:
                continue
            else:
                correlation = df[i].corr(df[j])
                if correlation < min_value:
                    min_value = correlation
                    min_indx1 = i
                    min_indx2 = j
    print(min_indx1, min_indx2)
#%%
lab04_Task12_2018_2_60_009()
#%%
# Task 13
def lab04_Task13_2018_2_60_009():   
     df.plot.scatter(x ='V2', y ='Amount')
#%%
lab04_Task13_2018_2_60_009()
#%%
# Task 14
def lab04_Task14_2018_2_60_009():   
    df.boxplot(column=['Amount'])
#%%
lab04_Task14_2018_2_60_009()
#%%
#Task 15
def lab04_Task15_2018_2_60_009():
    class_0_V2 = df[["Amount","Class"]].query("Class==0")
    V2_0 = class_0_V2["Amount"]
    
    class_0_V2 = df[["Amount","Class"]].query("Class==1")
    V2_1 = class_0_V2["Amount"]
    
    columns = [V2_0,V2_1]
    fig,ax = plt.subplots()
    ax.boxplot(columns)
    plt.show()
#%%
lab04_Task15_2018_2_60_009()
    

    