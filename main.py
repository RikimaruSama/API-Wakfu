# https://www.wakfu.com/fr/forum/467-coin-developpeurs/416776-json-mini-guide-utilisation
# https://gitlab.com/MathiusD/wakdata

urlVersion = 'https://wakfu.cdn.ankama.com/gamedata/config.json'
apiTypeList =   [ 
    "actions", "blueprints", "collectibleResources",
    "harvestLoots", "itemTypes", "itemProperties", "items",
    "jobsItems", "recipeCategories", "recipeIngredients",
    "recipeResults", "recipes", "resourceTypes", "resources", "states"
                ]

import requests

for url in [urlVersion]:
    try:
        # Pour l'url de la Version et de l'API, si nous recevons une réponse aucune exception ne sera levée.
        rep = requests.get(url)
        rep.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        
apiVersion = rep.json().get("version")
for apiType in apiTypeList:
    if apiType == "actions":
        apiUrl = "https://wakfu.cdn.ankama.com/gamedata/" + apiVersion + "/" + apiType + ".json"
        print("Search in " + apiUrl + "...\n")
        actions = requests.get(apiUrl).json()
        print(actions)