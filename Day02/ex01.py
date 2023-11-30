class Key:
    def __init__(self):
        self.len = 1337
        self.passphrase = "zax2rulez"
        self.number = 9000

    def __len__(self):
        return self.len

    def __getitem__(self, item):
        if item == 404:
            return 3
        else:
            return False

    def __gt__(self, other):
        return other <= self.number

    def __str__(self):
        return "GeneralTsoKeycard"

def check_key(key):
    if len(key) == 1337 and key[404] == 3 and key > 9000 \
            and key.passphrase == 'zax2rulez' and str(key) == 'GeneralTsoKeycard':
        return True
    return False

if __name__ == "__main__":
    new_key = Key()
    print(check_key(new_key))
    new_key.len = 0
    print(check_key(new_key))
    new_key.len = 1337
    print(check_key(new_key))
    new_key.passphrase = '123'
    print(check_key(new_key))