# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('sample.xlsx')
print(dataframe1)

for i in range(0,dataframe1.__len__()):
    res=str(dataframe1.loc[[i],['name']])
    res=res.split('\n')
    print(res[1].replace(str(i)+" ",''))
    print()