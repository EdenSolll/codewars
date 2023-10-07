def score(dice):
    rolls = {}
    total = 0
    for val in dice:
        if val in rolls:
            rolls[val] += 1
        else:
            rolls[val] = 1
    for val in rolls:
        if rolls[val] >= 3:
            if val == 1:
                total += 10 * 100 
            else:
                total += val * 100
            rolls[val] -= 3
        if val == 1:
            total += 100 * rolls[val]
        if val == 5:
            total += 50 * rolls[val]
    return total

