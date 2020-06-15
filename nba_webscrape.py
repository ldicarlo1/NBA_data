```
import requests
from bs4 import BeautifulSoup
import pandas as pd 

#URL to open live database of NBA players
url = "https://www.nbastuffer.com/2019-2020-nba-player-stats/"

#initilize reponse and use beautiful soup to parse the url
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#define empty array
df = pd.DataFrame({'Player Name':[],'Team':[],'Position':[]})


for num in range(2,572):
    #Player data is separated into rows, each column designated to a statistic
    #HTML code oscillates between "odd" and "even" for each row, which is specified below in the code

    if num % 2 ==0:
        row = soup.find(class_ = "row-{} even".format(num))  
    elif num % 2 !=0:
        row = soup.find(class_ = "row-{} odd".format(num))

    #there are 28 columns for all 28 statistics
    data_raw={}
    for i in range(0,28):
        data_raw['column{0}'.format(i)] = row.find_all('td')[i].get_text()

    #create a list of the raw data
    data = list(data_raw.values())
    #create and append the dictionary of each row to a dataframe
    df = df.append({'Player Name':data[1],'Team':data[2],'Position':data[3],'Age':data[4],'GP':data[5],
    'MPG':data[6],'Minutes %':data[7],'Usage Rate %':data[8],'Turnover Rate %':data[9],'FTA':data[10],
    'FT %':data[11],'2PA':data[12],'2P %':data[13],'3PA':data[14],'3P %':data[15],'Effective Shooting %':data[16],
    'True Shooting %':data[17],'PPG':data[18],'RBG':data[19],'Total Rebound %':data[20],'Assists PG':data[21],    
    'Assists %':data[22],'Steals PG':data[23],'Blocks PG':data[24],'TOPG':data[25],'VI':data[26]
    },ignore_index=True)

#create a dataframe and save it as a .CSV file
data_raw = pd.DataFrame(df)
data_raw.to_csv('nba_player_stats.csv') 
print(df)

```
