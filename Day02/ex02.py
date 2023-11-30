from collections import Counter


class Player:
    def __init__(self):
        self.candies = 0
        self.action = True

    def check(self, other):
        return self.action == other.action


class Cheater(Player):
    def __init__(self):
        super().__init__()
        self.action = False
        self.name = 'cheater'


class Cooperator(Player):
    def __init__(self):
        super().__init__()
        self.name = 'cooper'


class Copycat(Player):
    def __init__(self):
        super().__init__()
        self.start = True
        self.name = 'copycat'

    def check(self, other):
        if self.start:
            self.start = False
            return super().check(other)
        self.action = other.action
        return True


class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.name = 'grudger'

    def check(self, other):
        if not other.action and self.action:
            self.action = False
            return False
        return super().check(other)


class Detective(Player):
    def __init__(self):
        super().__init__()
        self.start_play = [True, True, False, True]
        self.someone_cheated = False
        self.copycat = True
        self.name = 'detect'

    def check(self, other):
        if self.start_play:
            self.action = self.start_play.pop()
            if not other.action:
                self.someone_cheated = True
            return super().check(other)
        else:
            if not self.someone_cheated:
                self.action = False
                return super().check(other)
            if self.copycat and self.someone_cheated:
                self.action = True
                self.copycat = False
        return True


class AntiDetective(Player):
    def __init__(self):
        super().__init__()
        self.first_game = None
        self.second_game = None
        self.cheat_detect = [False, False]
        self.name = 'anti_detective'

    def check(self, other):
        if self.first_game is None:
            self.first_game = other.action
        elif self.second_game is None:
            self.second_game = other.action
        if self.first_game == True and self.second_game == False:
            if self.cheat_detect:
                self.action = self.cheat_detect.pop()
            else:
                self.action = other.action
        else:
            self.action = other.action
        return self.action == other.action


class CopyFromStart(Player):
    def __init__(self):
        super().__init__()
        self.name = 'copystart'

    def check(self, other):
        self.action = other.action
        return self.action == other.action


class Game:
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for i in range(self.matches):
            if isinstance(player1, Detective):
                first_check = player1.check(player2)
                second_check = player2.check(player1)
            elif isinstance(player2, Detective):
                first_check = player2.check(player1)
                second_check = player1.check(player2)
            else:
                first_check = player1.check(player2)
                second_check = player2.check(player1)
            if first_check or second_check:
                if not player1.action or not player2.action:
                    pass
                else:
                    player1.candies += 2
                    player2.candies += 2
            else:
                if not player1.action:
                    player1.candies += 3
                    player2.candies -= 1
                else:
                    player1.candies -= 1
                    player2.candies += 3

        self.registry[player1.name] = self.registry.get(player1.name, 0) + player1.candies
        self.registry[player2.name] = self.registry.get(player2.name, 0) + player2.candies

    def top3(self):
        i = 0
        for key, val in sorted(self.registry.items(), key=lambda item: item[1], reverse=True):
            print(key, val)
            i += 1
            if i == 3:
                break


if __name__ == '__main__':
    game = Game()

    game.play(Cheater(), Cooperator())
    game.play(Cheater(), Detective())
    game.play(Cheater(), Grudger())
    game.play(Cheater(), Copycat())
    game.play(Cooperator(), Detective())
    game.play(Cooperator(), Grudger())
    game.play(Cooperator(), Copycat())
    game.play(Detective(), Grudger())
    game.play(Detective(), Copycat())
    game.play(Copycat(), Grudger())

    game.top3()

    print()

    game = Game()

    game.play(Cheater(), Cooperator())
    game.play(Cheater(), Detective())
    game.play(Cheater(), Grudger())
    game.play(Cheater(), Copycat())
    game.play(Cooperator(), Detective())
    game.play(Cooperator(), Grudger())
    game.play(Cooperator(), Copycat())
    game.play(Detective(), Grudger())
    game.play(Detective(), Copycat())
    game.play(Copycat(), Grudger())
    game.play(AntiDetective(), Cheater())
    game.play(AntiDetective(), Cooperator())
    game.play(AntiDetective(), Copycat())
    game.play(AntiDetective(), Detective())
    game.play(AntiDetective(), Grudger())

    game.play(CopyFromStart(), Cheater())
    game.play(CopyFromStart(), Cooperator())
    game.play(CopyFromStart(), Copycat())
    game.play(CopyFromStart(), Detective())
    game.play(CopyFromStart(), Grudger())
    game.play(CopyFromStart(), AntiDetective())

    game.top3()
