# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:28:47 2019
@author: Rizli Avriananda Anshari
@title: Python Homework
"""

"""
Call the library
"""

import pandas as pd
import numpy as np

"""
Read Google Playstore Data
"""
google_play_apps=pd.read_csv("googleplaystore.csv", encoding='latin1')
google_play_apps.tail(10)


"""
1.How Many Rows & Column?
"""
print ('row: ', len(google_play_apps))
print ('column: ', len(google_play_apps.columns))

"""
2.How many unique apps categories reflected in the dataset?
"""
google_play_apps.Category.nunique(dropna = True)

"""
3. How many unique genres according to the dataset?
"""
google_play_apps.Genres.nunique(dropna = True)
"""
4. Which code is appropriate to drop duplicate values in 'App' column and remove its rows in Python? Assume dataset was loaded as a pandas data frame variable: google_play_apps.
"""
google_play_apps.drop_duplicates(subset='App', inplace=True)

"""
5.
"""
google_play_apps[google_play_apps['Installs']=='Free']
google_play_apps = google_play_apps[google_play_apps['Installs'] != 'Free']
google_play_apps.tail(10)

google_play_apps['Installs'] = google_play_apps['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
google_play_apps['Installs'] = google_play_apps['Installs'].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)

"""
6.
"""
google_play_apps['Installs']=google_play_apps['Installs'].astype(int)
google_play_apps.dtypes

"""
7.
""""
google_play_apps1 = google_play_apps[['App','Category']]
google_play_apps1[google_play_apps1['App'] == "WhatsApp Messenger"]
google_play_apps1[google_play_apps1['App'] == "FIFA Soccer"]
google_play_apps1[google_play_apps1['App'] == "DU Battery Saver - Battery Charger & Battery Life"]
google_play_apps1[google_play_apps1['App'] == "Dropbox"]
google_play_apps1[google_play_apps1['App'] == "Pinterest"]
google_play_apps1[google_play_apps1['App'] == "Flipboard: News For Our Time"]
google_play_apps1[google_play_apps1['App'] == "Subway Surfers"]
google_play_apps1[google_play_apps1['App'] == "File Commander - File Manager/Explorer"]


"""
8.
""""
google_play_apps2 = google_play_apps[['App','Installs']]
print (google_play_apps2[google_play_apps2.Installs >= 1000000000])

"""
9.
"""
google_play_apps['Reviews']=google_play_apps['Reviews'].astype(int)
google_play_apps3 = google_play_apps[google_play_apps['Category']=='COMMUNICATION']
google_play_apps3 = google_play_apps3.sort_values('Reviews',ascending=False)
google_play_apps3 = google_play_apps3[['App','Reviews']]
google_play_apps3

"""
10.
"""
google_play_apps4 = google_play_apps[google_play_apps['Category']=='GAME']
google_play_apps4 = google_play_apps4.sort_values(['Installs','Rating'],ascending=[False,False])
google_play_apps4 = google_play_apps4[['App','Installs','Rating']]
google_play_apps4



