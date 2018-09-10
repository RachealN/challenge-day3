def sortlist(my_list):
    evens = []
    odds = []
    chars = []

    if isinstance(my_list, (int, str)):
        return 'Invalid Input'

    if my_list:
        for c in my_list:
            if not isinstance(c, int):
                chars.append(c)
            else:
                if c % 2 == 0:
                    evens.append(c)
                else:
                    odds.append(c)

        return dict(evens=sorted(evens), odds=sorted(odds), chars=sorted(chars))
    return dict(evens=[], odds=[], chars=[])
