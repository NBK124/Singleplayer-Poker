def is_square(values):
    for c in values:
        if values.count(c) == 4:
            return True
    return False

def is_three(values):
    for c in values:
        if values.count(c) == 3:
            return True
    return False

def is_pairs(values):
    counts = {}
    for e in values:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1
    if len(counts) == 3 and 2 in counts.values():
        return True
    return False

def is_fullhouse(hand):
    counts = {}
    for element in hand:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    if len(counts) == 2 and (3 in counts.values() or 2 in counts.values()):
        return True
    return False

def is_pair():
    for c in values:
        if values.count(c) == 2:
            return True
    return False


suit = '♠♥♦♣'
value = '234567890JQKA'
deck = ['$$', '₱₱']
print('0  1  2  3  4', end='\n\n')
for s in suit:
    for v in value:
        deck.append(v + s)
deck = list(set(deck))
player = deck[:5]
player.sort()
for _ in range(5):
    deck.pop()
print(*player)
for _ in range(int(input('сколько карт заменить? '))):
    player[int(input('введи индекс карты: '))] = deck.pop()
print(*player)
if '$$' in player:
    player[player.index('$$')] = input('джокер это: ')
    print(*player)
if '₱₱' in player:
    player[player.index('₱₱')] = input('джокер это: ')
    print(*player)
player.sort()

suits = [i[1] for i in player]
values = [i[0] for i in player]
onesuit = len(set(suits)) == 1
sorty = values == ['2', '3', '4', '5', 'A'] or values == ['2', '3', '4', '5', '6'] or values == ['3', '4', '5', '6', '7'] or values == ['4', '5', '6', '7', '8'] or values == ['5', '6', '7', '8', '9'] or values == ['0', '6', '7', '8', '9'] or values == ['0', '7', '8', '9', 'J'] or values == ['0', '8', '9', 'J', 'Q'] or values == ['0', '9', 'J', 'K', 'Q']
if onesuit and values == ['0', 'A', 'J', 'K', 'Q']:
    combination = 'флеш рояль'
elif onesuit and sorty:
    combination = 'стрит флеш'
elif is_square(values):
    combination = 'каре'
elif is_fullhouse(values):
    combination = 'фулл хаус'
elif onesuit:
    combination = 'флеш'
elif sorty or values == ['0', 'A', 'J', 'K', 'Q']:
    combination = 'стрит'
elif is_three(values):
    combination = 'сет'
elif is_pairs(values):
    combination = 'две пары'
elif is_pair():
    combination = 'пара'
else:
    combination = 'старшая карта'
print(combination, end='\n\n')
