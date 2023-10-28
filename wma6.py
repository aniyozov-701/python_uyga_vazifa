
def summa(*sonlar):
    """kritligan sonlar ko'paytmasini hisoblaydigan fungsiya """
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(summa(1, 2))
print(summa(1, 2, 3, 4, 5))
