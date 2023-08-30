#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
    }

#Nesting a list in a dictionary

travel_log = {
    "France": {"cited_visited":["Paris", "Lille", "Dijon"], "total_visits":12},
    "Germany":{"cited_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits":0},

}
print(travel_log)

# Nesting dicts in a list
travel_log = [
    {
        "country":"France",
        "cited_visited":["Paris", "Lille", "Dijon"],
        "total_visits":12},
    {
        "country": "Germany",
        "cited_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5},
]