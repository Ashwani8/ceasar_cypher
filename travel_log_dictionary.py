travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 

def add_new_country(new_country, number_of_visits, list_cities):
   # create an empty dictionary
    visited_country = {}
    visited_country["country"] = new_country
    visited_country["visits"] = number_of_visits
    visited_country["cities"] = list_cities
    travel_log.append(visited_country)



#🚨 add a new entry
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
