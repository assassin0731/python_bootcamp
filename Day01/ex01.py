import ex00


def split_booty(*purse):
    first = {"gold_ingots": 0}
    second = {"gold_ingots": 0}
    third = {"gold_ingots": 0}
    counter = 1
    for p in purse:
        new_p = p.copy()
        if "gold_ingots" in new_p:
            while new_p["gold_ingots"] != 0:
                if counter % 3 == 1:
                    first = ex00.add_ingot(first)
                elif counter % 3 == 2:
                    second = ex00.add_ingot(second)
                else:
                    third = ex00.add_ingot(third)
                counter += 1
                new_p = ex00.get_ingot(new_p)
    return first, second, third


if __name__ == "__main__":
    first = {"gold_ingots": 3}
    second = {"gold_ingots": 2}
    third = {"apples": 10}
    print(split_booty(first, second, third))
