travel_log=[
    {
        "country":"france",
        "visits":12,
        "cities":["paris",'lille','dijon']

    },
    {
        "country":"germany",
        "visits":5,
        "cities":["berlin","hamburg","stuttgart"]
    },
]


def add_new_country(new_country,new_visit,new_cities):
    new_travel_log=[
        {
            "county":new_country,
            "visits":new_visit,
            "cities":new_cities
        }
    ]
    travel_log.append([new_travel_log])

add_new_country("India",10,["ap","bangalore","hyderabad"])
print(travel_log)
