import cloudscraper # pip install cloudscraper
import statistics
import json
import os
from collections import defaultdict

state_and_territory_codes = [
    # 50 States
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
    "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
    "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY",
    
    # 5 Territories
    "AS",  # American Samoa
    "GU",  # Guam
    "MP",  # Northern Mariana Islands
    "PR",  # Puerto Rico
    "VI"   # U.S. Virgin Islands
]

for state in state_and_territory_codes:
    # getting data
    scraper = cloudscraper.create_scraper()
    url = "https://api.covidtracking.com/v1/states/"+state.lower()+"/daily.json"
    response = scraper.get(url)
    data = response.json()

    #calculations and prints
    print("Covid confirmed cases statistics")
    #state
    print("State Name:",data[0]["state"])
    #daily average
    positive_increase = []
    date_list = []
    for observation in data:
        positive_increase.append(observation["positiveIncrease"])
        date_list.append(observation["date"])
    print("Average number of new daily confirmed cases for the entire state dataset:",statistics.mean(positive_increase))
    #highest day
    max_index = positive_increase.index(max(positive_increase))
    highest_day = date_list[max_index]
    print("Date with the highest new number of covid cases:", highest_day)
    #most recent zero day
    most_recent_zero = "none"
    for observation in data:
        if observation["positiveIncrease"] == 0:
            most_recent_zero = observation["date"]
            break
    print("Most recent date with no new covid cases:", most_recent_zero)
    #highest month
    monthly_totals = defaultdict(int)
    for observation in data:
        date_str = str(observation["date"])
        month = date_str[0:6]
        key = month
        monthly_totals[key] += observation["positiveIncrease"]   
    highest_month = max(monthly_totals, key=monthly_totals.get)
    print("Month and Year, with the highest new number of covid cases:", highest_month)
    #lowest month
    lowest_month = min(monthly_totals, key=monthly_totals.get)
    print("Month and Year, with the lowest new number of covid cases:", lowest_month)
    # print(date_list)
    # print(positive_increase)

    #put results in a dictionary
    results = {
    "State Name:": data[0]["state"],
    "Average number of new daily confirmed cases for the entire state dataset:": statistics.mean(positive_increase),
    "Date with the highest new number of covid cases:": highest_day,
    "Most recent date with no new covid cases:": most_recent_zero,
    "Month and Year, with the highest new number of covid cases:": highest_month,
    "Month and Year, with the lowest new number of covid cases:": lowest_month
    }
    folder = "/home/ubuntu/hw5500/hw5"
    filename = os.path.join(folder, data[0]["state"] + ".json")
    with open(filename, "w") as file:
        json.dump(results, file, indent=2)