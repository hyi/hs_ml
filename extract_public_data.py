import pandas as pd


all_file = 'data/hs_data.csv'
public_file = 'data/hs_data_public.csv'
uuids = []
titles = []
keywords_list = []
abstracts = []

all_data = pd.read_csv(all_file, index_col ="UUID")
dims = all_data.shape
cnt = 0
for index, row in all_data.iterrows():
    if row.Status == 'public':
        uuids.append(index)
        titles.append(row.Title)
        keywords_list.append(row.Keywords)
        abstracts.append(row.Abstract)
        cnt += 1

print('total public resources: ', cnt)

df = pd.DataFrame({'UUID': uuids,
                   'Title': titles,
                   'Keywords': keywords_list,
                   'Abstract': abstracts})

header_list = ['UUID', 'Title', 'Keywords', 'Abstract']
df[header_list].to_csv(public_file, index=False)
