import pandas as pd


data_files = ['data/hs_data_published.csv',
              'data/hs_data_public.csv',
              'data/hs_data.csv']

for f in data_files:
    data = pd.read_csv(f, index_col ="UUID")
    dims = data.shape
    print(f, dims)
    cnt = 0
    for index, row in data.iterrows():
        print(index, row.Title, row.Keywords, row.Abstract)
        cnt += 1
        if cnt > 5:
            break
