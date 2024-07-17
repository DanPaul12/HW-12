our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def shared_flights(routes1, routes2):
    shared_routes = routes1.intersection(routes2)
    print(f"The routes we and or coompetitors have in common are: {shared_routes}")

def unique_flights_ours(routes1, routes2):
    unique_flights = {flight for flight in routes1 if flight not in routes2}
    print(f"Our unique flights are {unique_flights}")

def unique_flights_competitors(routes1, routes2):
    unique_flights = {flight for flight in routes1 if flight not in routes2}
    print(f"Our competitor's unique flights are {unique_flights}")

shared_flights(our_routes, competitor_routes)
unique_flights_ours(our_routes, competitor_routes)
unique_flights_competitors(competitor_routes, our_routes)