import math


def gc(string, gc):
    count_gc = string.count('G') + string.count('C')
    count_at = string.count('A') + string.count('T')

    return ((gc / 2.0) ** count_gc) * (((1 - gc) / 2.0) ** count_at)


def gc_log(string, gc):
    total = 0

    for char in string:
        if char in ['G', 'C']:
            total += math.log10(gc) - math.log10(2)
        else:
            total += math.log10(1 - gc) - math.log10(2)

    return total