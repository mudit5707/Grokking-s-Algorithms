def SearchGraph(graph):
    Searched = []
    ToSearch = []
    ToSearch.extend(graph["you"])
    for person in ToSearch:
        if (person not in Searched):
            if IsMangoSeller(person):
                return f"{person} is the Mango Seller, found!"
            else:
                ToSearch.extend(graph[person])
                Searched.append(person)
    return "Not Found"

def IsMangoSeller(person):
    if person == "johnny": return True
    else : return False



graph = {
    "you" : ["bob", "claire", "alice"],
    "bob" : ["anuj", "peggy"],
    "anuj" : [],
    "peggy" : [],
    "alice" : ["peggy"],
    "claire" : ["thom", "johnny"],
    "thom" : [],
    "johnny" : []
}

print(SearchGraph(graph))