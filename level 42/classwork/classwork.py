def to_binary(x):
    arr = []
    while x > 0:
        bin = x % 2
        arr.append( str(bin) )
        x = x // 2 
        return "".join(arr[::-1])
print(to_binary(14))

#3
def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result += "0"
        else:
            result += "1"
    return result


def points(games):
    total_points = 0
    for game in games:
        x, y = game.split(':')
        x, y = int(x), int(y)
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
            return total_points