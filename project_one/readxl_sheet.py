# import pandas lib as pd
import pandas as pd


# read by default 1st sheet of an excel file
def read_excel():
    dataframe1 = pd.read_excel('C:\\Users\\veena\\Desktop\\vit-hackathon-2022\\project_one\\static\\sample.xlsx')
    print(dataframe1)

    res1=[]

    for i in range(0,dataframe1.__len__()):
        res=str(dataframe1.loc[[i],['name']])
        res=res.split('\n')
        res=res[1].replace(str(i)+" ",'')
        res1.append(res)
        print(res)
        print()


    return dataframe1.__len__(),res1