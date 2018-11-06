# import ufc fighter data using ufc-data-api
import json
import requests

r = requests.get("http://ufc-data-api.ufc.com/api/v3/us/fighters")
contentStr = r.content

fighters = json.loads(contentStr)

# get ranked fighters in each division
rankedFighterInfo = []

for fighter in fighters:
	if fighter['rank']:
		fighterInfo = {}
		fighterInfo['name'] = fighter['first_name'] + ' ' + fighter['last_name']
		fighterInfo['wins']   = fighter['wins']
		fighterInfo['losses'] = fighter['losses']
		fighterInfo['draws']  = fighter['draws']
		fighterInfo['weight_class'] = fighter['weight_class']
		fighterInfo['rank'] = fighter['rank']

		rankedFighterInfo.append(fighterInfo)

# write to file for plotting in R
with open('../text/ranked_fighters.txt', 'w') as fout:
    json.dump(your_list_of_dict, fout)