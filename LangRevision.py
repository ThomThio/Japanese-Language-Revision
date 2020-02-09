import pandas as pd
import os, numpy as np
import keyboard


#read file
xls = pd.ExcelFile("Living Document.xlsm")

#access the specific worksheet
df = pd.read_excel(xls, 'Japanese')

# print(df.head())

#organize by date learnt, start from the last, or randomize
# date_grouped = df.groupby(by=['Date'])

#We have some uncompleted revisions - filter all that has a romaji and english meaning
df['Romaji'].replace('',np.nan,inplace=True)
df['English Meaning'].replace('',np.nan,inplace=True)
df.dropna(subset=['Romaji'],inplace=True)
df.dropna(subset=['English Meaning'],inplace=True)


def run_program(df):
	#randomizer	
	while True:
		print("===============================")
		key = input("Press for next revision!")
		sampled = df.sample(n=1,replace=False)
		jap_trigger = sampled[['Romaji','Hira/Kata']].iloc[0]
		eng_trigger = sampled[['English Meaning','Category','Topic']].iloc[0]

		print("Category:",eng_trigger['Category'],"Topic:",eng_trigger['Topic'])
		line_break = '-' * len(eng_trigger['English Meaning'])
		print(eng_trigger['English Meaning'])
		print(line_break)


		key = input("Press for Answer")
		print("===============================")
		print(line_break)
		print(jap_trigger['Romaji'])
		print(jap_trigger['Hira/Kata'])
		print(line_break)


#ask for mode:
	#1: Opposites, Scales
	#2: Vocab
	#3: Grammar, Sentence Forming

if keyboard.read_key() == "1":
    print("Selected #1: Adjective Opposites, Scales")

    #filter for adjective opposites only
    df = df[df['Category']=='Adj']

run_program(df)