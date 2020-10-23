#Variables.
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
attractions = [[] for x in destinations]

#Test Traveler.
test_traveler = ['Erin Wikes', 'Shanghai, China', 'historical site', 'art']

#Logic Functions.
# 1- Find the destination index.
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# 2- Adding attractions to destinations.
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = [[], []]
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
        return
    except ValueError:
        print('Error Caught!')
        return

#Adding attractions.
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# 3- Finding destination attractions that match the traveler's interests.
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attractions in attractions_in_city:
        attraction_tags = possible_attractions[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attractions[0])
    return attractions_with_interest

# 4- Sending attractions to traveler:
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = 'Hi, ' + traveler[0] + ', we think you would like this place around, ' + traveler_destination + ': '
    for attraction in traveler_attractions:
        interests_string += 'The ' + attraction + ','
        return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)



