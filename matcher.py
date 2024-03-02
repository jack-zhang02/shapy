import pandas as pd

db = pd.read_csv('/content/db.csv')
db.columns = db.iloc[-1]
db = db[:-1]

a = db[db['Bras'] > 5]
rels = a[['Brand Name','Bra Style','Size','Fits ribcage','Stretched Band','Band length','Cup width']]


