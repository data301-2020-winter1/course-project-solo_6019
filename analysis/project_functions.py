import numpy as np
import pandas as pd

def load_data():
    
    data = pd.read_csv(r"C:\Users\vinui\OneDrive\Desktop\Project\data\raw\NBASeasonData.csv")
    return data

def load_and_process():

    # Method Chain 1 (Load data and deal with missing data)

    df = (
          pd.read_csv(r"C:\Users\vinui\OneDrive\Desktop\Project\data\raw\NBASeasonData.csv")
          .dropna()
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df
          .filter(['Player' ,'TS%', '3PAr', 'FTr', 'AST%', 'STL%', 'BLK%' ])
      )

    # Make sure to return the latest dataframe

    return df2

def load_and_minimize():

    # Method Chain 1 (Load data and deal with missing data)

    df = (
          pd.read_csv(r"C:\Users\vinui\OneDrive\Desktop\Project\data\raw\NBASeasonData.csv")
          .dropna()
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df
          .filter(['AST%', 'STL%', 'BLK%', 'TOV%' ])
      )

    # Make sure to return the latest dataframe

    return df2 
    



    
    

    
    
    
    
    
    
def show(data):
    print ('\033[1m' + 'ROWS x COLUMNS' + '\033[0m') #the code to make the string bold and this will be used for columns and head as well
    print (' ')
    print(data.shape)   #returns the number of rows by the number of the columns
    print (' ')
    print ('\033[1m' + 'THE COLUMNS' + '\033[0m')
    print(' ')
    print(data.columns) #returns the name of all the columns
    print (' ')
    print ('\033[1m' + 'FIRST 5 ROWS OF THE 2011-2016 NBA SEASON STATS' + '\033[0m')
    print(' ')
    print(data.head())  #returns the first 5 rows of the df as it has 3000+ rows
    
    

    

