# import ufc fighter data using ufc-data-api
import json
import requests

r = requests.get("http://ufc-data-api.ufc.com/api/v3/us/fighters")
contentStr = r.content

fighters = json.loads(contentStr)

def abbreviateWeightClass( weight_class ):
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
	


# get ranked fighters in each division
rankedFighterInfo = []

for fighter in fighters:
	if fighter['rank']:
		fighterInfo = {}
		fighterInfo['name'] = fighter['first_name'] + ' ' + fighter['last_name']
		fighterInfo['wins']   = fighter['wins']
		fighterInfo['losses'] = fighter['losses']
		fighterInfo['draws']  = fighter['draws']
		fighterInfo['weight_class'] = abbreviateWeightClass(fighter['weight_class'])
		fighterInfo['rank'] = fighter['rank']

		rankedFighterInfo.append(fighterInfo)

# write to file for plotting in R
with open('../text/ranked_fighters.txt', 'w') as fout:
    json.dump(rankedFighterInfo, fout)