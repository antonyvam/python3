import pandas as pd
import pylab as pl
pd.set_option('display.precision', 1)
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)

def main(): 
    df = pd.read_csv("data/sample_data.csv", index_col=0)
    # some standard dataframe methods
    print(df)
    print(df.index)
    print(type(df.index))

    print(df.columns)
    print(type(df.columns))
    
    print(df.values)
    print(type(df.values))
    print()

    # extracting a single column can create a new dataframe or a series
    a = df[['state']]    # list parameter => returns a dataset
    print(f"df[['state']] returns: \n\t{type(a)}")
    
    b = df['state']      # column parameter => returns a series
    print(f"df['state'] returns: \n\t{type(b)}")
    print()
    
    
    # using .loc
    # loc uses the index of the dataset.  A lot of datasets have an index of
    # integers, but the index can be any data type, often str
    
    # print 1 row
    print(df.loc['Niko'])   # loc uses index
    print()
    # print several rows
    print(df.loc['Niko':'Dean'])
    print()

    # selecting rows and columns
    print(df.loc[['Dean', 'Cornelia'], ['age', 'state', 'score']])
    print()
    print(df.loc[:, ['food', 'color']]) # all rows, some columns
    print()

    # using iloc
    print(df.iloc[3])   # select row 3 as series
    print()
    print(df.iloc[[3, 6, 2, 4]])   # select multiple rows
    print()
    print(df.iloc[3, 2])    # select row and column
    print()
main()
