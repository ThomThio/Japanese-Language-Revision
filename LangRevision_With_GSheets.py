import pygsheets
import pandas as pd
#authorization

key_file = "mindful-bivouac-268306-4273022da0d9.json"
gc = pygsheets.authorize(service_file=key_file)

# Create empty dataframe
df = pd.DataFrame()

# Create a column
# df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('PIV Sheets')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
print(wks)