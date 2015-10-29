#  Wzorowane na przykładzie Rona Zacharskiego


from math import sqrt
from operator import itemgetter


users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""

    # TODO: wpisz kod
    e = 0
    for i in users:
        for j in users:
            for group1, rat1 in users[i].items():
                for group2, rat2 in users[j].items():
                    if group1 == group2 and i != j and i == rating1 and j == rating2: #where rating1, rating2 are usernames
                        #print("Zespoły takie same")
                        e = e + abs(rat1 - rat2)
                        # print( e )
    if e != 0:
        return e
    else:
        return -1
    pass

def computeNearestNeighbor(username, users):
    """dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""
    # TODO: wpisz kod
    e = 0
    distances = []
    nearestNeighbor = []
    nameOfNearestNeighbor = []
    for i in users:
        for j in users:
            if i == username and i !=j:
                for group1, rat1 in users[i].items():
                    for group2, rat2 in users[j].items():
                        if group1 == group2:
                            #print("Zespoły takie same")
                            e = e + abs(rat1 - rat2)
                distances.append([j, e])
                e=0
    distances.sort(key=itemgetter(1))
    nearestNeighbor.extend(distances[0])

    #Jeśli najbliższych sąsiadów jest więcej niż 1...
    for i, j in distances:
        if j == nearestNeighbor[1] and i != nearestNeighbor[0]:
            nearestNeighbor.extend([i, j])
    nameOfNearestNeighbor.append(nearestNeighbor[0])

    for i in range(0, nearestNeighbor.__len__(), 2):
        if nearestNeighbor[i] != nearestNeighbor[0]:
            nameOfNearestNeighbor.append(nearestNeighbor[i])

    return nameOfNearestNeighbor

def recommend(username, users):
    # """Zwróć listę rekomendacji dla użytkownika"""
    # # znajdź preferencje najbliższego sąsiada
    nearest = computeNearestNeighbor(username, users)
    # print("Najblizszy:", nearest)
    #
    recommendations = []
    # # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad
    # # TODO: wpisz kod

    for name1 in users:
        for name2 in nearest:
            if name1 == name2:
                for group, value in users[name1].items():
                    recommendations.append([group, value])
    #print(nearest,recommendations)

    userRecom = []
    for name3 in users:
        if name3 == username:
            for group, value in users[name3].items():
                userRecom.append([group, value])
    #print(username,userRecom)

    same=[]
    for group1 in userRecom:
        for group2 in recommendations:
            if group1[0] == group2[0]:
                same.append(group2)

    #print(recommendations)
    for i in same:
        for j in recommendations:
            if i == j:
                recommendations.remove(j)
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)

# przykłady
print("Odległość w metryce taksówkowej dla użytkowników Gosia i Ela:", manhattan('Gosia', 'Ela'))
print("Użytkownik o najbliższych preferencjach dla użytkownika Celina to:", computeNearestNeighbor("Celina", users))
print("Rekomendacje:", recommend('Celina',users))

