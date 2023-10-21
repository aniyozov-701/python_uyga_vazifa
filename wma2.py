def kankuliotor(kvadrot, kub):
    """Soni kubi va kvadrotini hisoblovchi dastur"""
    print(kankuliotor.__doc__)
    print(f"Soni kvadroti : {kvadrot ** 2}\n"
          f"Soni kubi : {kub ** 3}")


kankuliotor(5, 6)


def toqson_juftson(toq, juft):
    """Soni juft yoki toqligini aniqlovchi fungsiya"""
    print(toqson_juftson.__doc__)
    print(f"toq son : {toq % 2 == 1}  \n"
          f"juft son : {juft % 2 == 0}")


toqson_juftson(8, 9)
