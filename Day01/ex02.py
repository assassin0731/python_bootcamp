def decoration(func):
    def wrapper(purse):
        print("SQUEAK")
        return func(purse)

    return wrapper


@decoration
def add_ingot(purse):
    new_purse = {key: val for key, val in purse.items() if key == "gold_ingots"}
    new_purse["gold_ingots"] = new_purse.get("gold_ingots", 0) + 1
    return new_purse


@decoration
def empty(purse):
    return {}


@decoration
def get_ingot(purse):
    return {key: val - 1 for key, val in purse.items() if key == "gold_ingots"
            and purse["gold_ingots"] > 0}


if __name__ == "__main__":
    purse = {"gold_ingots": 3}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
    print(get_ingot(empty(purse)))
