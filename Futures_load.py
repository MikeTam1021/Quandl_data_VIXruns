"""
Created on Mon Nov 09 18:43:32 2015

@author: MikeTam
"""

import Quandl

API_Key = 'xxxxxx'       #get your own key by signing up
MONTHS = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']
YEARS = ['15']    # in order to make more calls, we need a key. anon call limit 50/ 10 minutes. Free account 2000/ 10 min
data = []


if __name__ == "__main__":
    #call seperate parts together
    dataVIX = Quandl.get('CBOE/VIX', authtoken = API_Key)
    for year in YEARS:
        for month in MONTHS:
            data.append(Quandl.get('CBOE/VX' + month + '20' + year, authtoken = API_Key))

