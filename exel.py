from csv import excel
import xlsxwriter
import pandas as pd

data=pd.read_excel('C:/Users/DELL/Desktop/20212/ĐA1/code/python/du_lieu.xlsx')
data=data.drop_duplicates(subset='ID',keep="first")
save=('C:/Users/DELL/Desktop/20212/ĐA1/dulieu.xlsx')
data.to_excel(save)