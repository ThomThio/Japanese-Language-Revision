import pandas as pd
import os, numpy as np
import keyboard
import traceback


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


def sample(df):
	#randomizer	
	while True:
		print("===============================")
		input("Press for revision")
		sampled = df.sample(n=1,replace=False)
		jap_trigger = sampled[['Romaji','Hira/Kata']].iloc[0]
		eng_trigger = sampled[['English Meaning','Category','Topic']].iloc[0]

		print("Category:",eng_trigger['Category'],"Topic:",eng_trigger['Topic'])
		line_break = '-' * len(eng_trigger['English Meaning'])
		print(eng_trigger['English Meaning'])
		print(line_break)


		input("Press for Answer")
		print("===============================")
		print(line_break)
		print(jap_trigger['Romaji'])
		print(jap_trigger['Hira/Kata'])
		print(line_break)

def run_program(df):
	while True:
		#ask for mode:
		print('---------------------------------------------------')
		print("Select a mode:")
		print("1: Opposites, Scales")
		print("#2: Vocab")
		print("#3: Grammar & Sentence Forming")
		mode_input = int(input("Select Mode:"))
		try:
			if mode_input == 1:
				print("Selected #1: Adjective Opposites, Scales")
				#filter for adjective opposites only
				df = df[df['Category']=='Adj']
			elif mode_input == 2:
				print("Selected #2: Vocabulary")
				#filter for adjective opposites only
				df = df[df['Category']!='Adj']

			elif mode_input == 3:
				print("Selected #3: Grammar & Sentence Forming")
			    #todo: TBC
			sample(df)
		except ValueError:
			print("ERROR. Please input a number")
		except:
			traceback.print_exc()


run_program(df)