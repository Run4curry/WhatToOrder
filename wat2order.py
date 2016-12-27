#sup niggaz
#import shit goes here
import requests #make http requests
import json #format data from the requests

#body

#the place where they are searching for, e.g. "mcdonalds"
name_of_place = input("pls enter name of place: ")
#location, e.g. san jose, ca
location = input("pls enter location where the place is near(city,state) format pls: ")
#api id and password
client_id='LHYTXEOO43YCRBMY2GN2EQUFLLG4YUBGH2QKK3MYJX51WSNV'
client_secret='S0MDLD5COOSAHHHQIZZUATRIAINJDNPX1TZ14I4A2RXMM5ZO'
api_version ='20161226'
#construct params for the search api call
search_params = { 'near':location, 'query':name_of_place, 'client_id':client_id, 'client_secret':client_secret, 'v':api_version }
#make the request now
search_request = requests.get('https://api.foursquare.com/v2/venues/search', params=search_params)
search_data = search_request.json()
#print(data)


#at this point we will simply take the first place returned and use the id to get the menu(if there is a menu)
if(search_data['response']['venues'][0]['hasMenu']):
	#construct api url *****TODO****** sum1 find a more elegant way to do this plsss
	string1 = 'https://api.foursquare.com/v2/venues/'
	string2 = search_data['response']['venues'][0]['id']
	string3 = '/menu'
	string_wow = string1 + string2 + string3
	menu_params = { 'client_id':client_id, 'client_secret':client_secret, 'v':api_version }
	menu_request = requests.get(string_wow, menu_params)
	menu_data = menu_request.json()
	#print(menu_data)

#now we access the foods on the menu
#this array to hold all items on menu
food_items = []
#accessing menu:
for i in menu_data['response']['menu']['menus']['items']:
	for j in i['entries']['items']:
		for k in j['entries']['items']:
			food_items.append(k['name'].lower())

#print(food_items)

#now that we have a menu for the place, we make another api call to get the reviews
string3 = '/tips'
string_ggg =  string1 + string2 + string3
#make a dict that will hold the counts of each dish
count_dict = {}
for i in food_items:
	count_dict[i] = 0
#this line is uneccessary but for the sake of style, simply making a new tips params var, but its identical to menu params
tips_params = menu_params
tips_request = requests.get(string_ggg, tips_params)
tips_data = tips_request.json()
#loop through each menu item, for each menu item loop through each review and search for string matches
for foods in food_items:
	for tips in tips_data['response']['tips']['items']:
		if( tips['text'].lower().find(foods) != -1 ):
			count_dict[foods] =  count_dict[foods] + 1

print(count_dict)