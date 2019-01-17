import json
import requests
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt


# get ufc fighter data via ufc api
r = requests.get("http://ufc-data-api.ufc.com/api/v3/us/fighters")
contentStr = r.content
fighters = json.loads(contentStr)


def abbreviate_weight_class( weight_class ):
	if weight_class == "Flyweight":
		return "FLW"
	elif weight_class == "Bantamweight":
		return "BW"
	elif weight_class == "Featherweight":
		return "FW"
	elif weight_class == "Lightweight":
		return "LW"
	elif weight_class == "Welterweight":
		return "WW"
	elif weight_class == "Middleweight":
		return "MW"
	elif weight_class == "Light_Heavyweight":
		return "LHW"
	elif weight_class == "Heavyweight":
		return "HW"
	elif weight_class == "Women_Strawweight":
		return "WSW"
	elif weight_class == "Women_Flyweight":
		return "WFLW"
	elif weight_class == "Women_Bantamweight":
		return "WBW"
	elif weight_class == "Women_Featherweight":
		return "WFW"
	else:
		return "Weightless"


def calculate_win_rate ( fighter ):
	win_rate = float(fighter['wins']) / (fighter['wins'] + fighter['losses'] + fighter['draws'])
	return round(win_rate, 3)
# calculate champ dominance
# calculate num_undefeated fighters


# get ranked fighters in each division
rankedFighters = []
allFighters = []
malformedFighterInfoCount = 0
for fighter in fighters:
	try:
		fighterInfo = {
			'name': fighter['first_name'] + ' ' + fighter['last_name'],
			'wins': fighter['wins'],
			'losses': fighter['losses'],
			'draws': fighter['draws'],
			'win_rate': calculate_win_rate(fighter),
			'weight_class': abbreviate_weight_class(fighter['weight_class']),
			'rank': fighter['rank']
		}

		allFighters.append(fighterInfo)
		if fighter['rank']:
			rankedFighters.append(fighterInfo)
	# ~10 listings contain bogus data from fighters, i.e. first_name = 'TBD', last_name = None
	except:
		malformedFighterInfoCount += 1


# convert to dataframe
dfRankedFighters = pd.DataFrame(rankedFighters)
dfAllFighters = pd.DataFrame(allFighters)

# increasing weight_class order for plot
weightClassOrder = ["FLW", "BW", "FW", "LW", "WW", "MW", "LHW", "HW", "WSW", "WFLW", "WBW", "WFW"]

# all fighter analysis
sea.catplot(x="weight_class", y="win_rate", data=dfAllFighters, order=weightClassOrder)
plt.title('UFC Fighter Win Rate by Weight Class')
plt.show()

dfNotCmPunk = dfAllFighters[dfAllFighters['name'] != 'CM Punk']
sea.catplot(x="weight_class", y="win_rate", data=dfNotCmPunk, order=weightClassOrder)
plt.title('UFC Fighter Win Rate by Weight Class')
plt.show()


p = sea.boxplot(x="weight_class", y="win_rate", data=dfAllFighters, order=weightClassOrder)
p.set_title("UFC Fighter Win Rate by Weight Class")

# ranked fighter analysis
sea.catplot(x="weight_class", y="win_rate", data=dfRankedFighters, order=weightClassOrder)
plt.title('UFC Ranked Fighter Win Rate by Weight Class')
plt.show()


# Champion analysis
# include name on graph
dfChampions = dfRankedFighters[dfRankedFighters['rank'] == 'C']

# HW champion Daniel Cormier is appearing as rank = 1 instead of rank = C, manually add
dfChampions = dfChampions.append(dfRankedFighters[dfRankedFighters['name'] == 'Daniel Cormier'])
# Amanda Nunes is both WFW and WBW champion, manually add a second entry
temp = dfRankedFighters[dfRankedFighters['name'] == 'Amanda Nunes']
temp['weight_class'] = 'WFW'
dfChampions = dfChampions.append(temp)


p = sea.barplot(x="weight_class", y="win_rate", data=dfChampions, order=weightClassOrder)
p.set_title("UFC Champion Win Rate by Weight Class")





plt.fi


