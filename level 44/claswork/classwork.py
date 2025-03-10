def count_by(x, n):
    result = []
    for i in range(n):
        result.append(x*(i+1))
        return result
    
def get_planet_name(id):
    planet_names = {
          1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
}
    return planet_names.get(id)

def human_years_cat_years_dog_years(human_years):
    dog = 15
    cat = 15
    if(human_years == 1):
        return [human_years , dog, cat]
    elif(human_years == 2):
        return [human_years , dog + 9, cat + 9]
    return [human_years, (dog + 9) + ((human_years-2) * 4), (cat + 9) + ((human_years-2) * 4)]


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old*2))