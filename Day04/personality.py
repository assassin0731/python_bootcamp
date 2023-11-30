import random


def generete_numbers():
    start = 100
    list_of_nums = []
    for i in range(4):
        number = random.randint(0, start)
        list_of_nums.append(number)
        start -= number
    list_of_nums.append(start)
    random.shuffle(list_of_nums)
    return list_of_nums


def setattrs(self, args, numbers):
    for i in range(5):
        setattr(self, args[i], numbers[i])


def create_class(name):
    args = ['neuroticism', 'openness', 'conscientiousness', 'extraversion', 'agreeableness']
    return type(name, (object,), {
        '__init__': lambda self, numbers: setattrs(self, args, numbers),
        'shoot': lambda self: print('Shooting'),
        'search': lambda self: print('Searching'),
        'talk': lambda self: print('Talking')
    })


def turrets_generator(n):
    for i in range(n):
        print('Turret number:', i + 1)
        yield Turrets(generete_numbers())


if __name__ == "__main__":
    Turrets = create_class('Turrets')
    n = 3
    for turret in turrets_generator(n):
        print(turret.neuroticism, turret.openness,
              turret.conscientiousness, turret.extraversion, turret.agreeableness)
        turret.shoot()
        turret.search()
        turret.talk()
        print()
