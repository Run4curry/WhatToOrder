#sup niggaz
#import shit goes here
import requests #make http requests
import json #format data from the requests
import sys #importing this for now so we can exit out of the program forcibly if there is no menu
#present for that restaurant

#body
#function takes in the name_of_place and location from the POST request sent from the client-side 
def what2Order(name_of_place,location):
	#the place where they are searching for, e.g. "mcdonalds"
	#name_of_place = input("pls enter name of place: ")
	name_of_place = name_of_place
	#location, e.g. san jose, ca
	#location = input("pls enter location where the place is near(city,state) format pls: ")
	location = location 
	#api id and password
	client_id='LHYTXEOO43YCRBMY2GN2EQUFLLG4YUBGH2QKK3MYJX51WSNV'
	client_secret='S0MDLD5COOSAHHHQIZZUATRIAINJDNPX1TZ14I4A2RXMM5ZO'
	api_version ='20161226'
	#construct params for the search api call
	search_params = { 'near':location, 'query':name_of_place, 'client_id':client_id, 'client_secret':client_secret, 'v':api_version }
	#make the request now
	#search_request = requests.get('https://api.foursquare.com/v2/venues/search', params=search_params)
	#the explore request is to find the most popular venue for that restaurant, i.e. BJs has a lot of venues
	#in San Jose, so making a call to the explore API endpoint will return us the most popular venue location
	#for BJs in San Jose theoretically 
	explore_request = requests.get('https://api.foursquare.com/v2/venues/explore',params=search_params)
	#search_data = search_request.json()
	explore_data = explore_request.json()
	#print(data)
	explore_index = 0 
	food_items = []



	#at this point we will simply take the first place returned and use the id to get the menu(if there is a menu)
	#if(search_data['response']['venues'][0]['hasMenu']):
	#construct api url *****TODO****** sum1 find a more elegant way to do this plsss
	#CHANGE now we want to find a location that actually has a menu, and until we find that location we will not stop 
	while(explore_index < len(explore_data['response']['groups'][0]['items'])): 
		string1 = 'https://api.foursquare.com/v2/venues/'
		#string2 = search_data['response']['venues'][0]['id']
		string2 = explore_data['response']['groups'][0]['items'][explore_index]['venue']['id']
		address_of_venue = explore_data['response']['groups'][0]['items'][explore_index]['venue']['location']['address']
		print(string2)
		print(address_of_venue)
		string3 = '/menu'
		string_wow = string1 + string2 + string3
		menu_params = { 'client_id':client_id, 'client_secret':client_secret, 'v':api_version }
		menu_request = requests.get(string_wow, menu_params)
		menu_data = menu_request.json()
		#print(menu_data)
		#else:
		#print('There is no available menu for %s. Please try again later!' % name_of_place)
		#sys.exit()

		#now we access the foods on the menu
		#this array to hold all items on menu
		#accessing menu:
		try:
			for i in menu_data['response']['menu']['menus']['items']:
				for j in i['entries']['items']:
					for k in j['entries']['items']:
						food_items.append(k['name'].lower())
			break 
		except:
			food_items = []
			explore_index = explore_index + 1
			continue

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

	#two lists to be returned to the server so they can be rendered on client side
	returnFoodList = []
	returnCountList = []
	#loop through each menu item, for each menu item loop through each review and search for string matches
	for foods in food_items:
		for tips in tips_data['response']['tips']['items']:
			if( tips['text'].lower().find(foods) != -1 ):
				count_dict[foods] =  count_dict[foods] + 1

	for key in count_dict:
		returnFoodList.append(key)
		returnCountList.append(count_dict[key])

	print(count_dict)
	return returnFoodList , returnCountList