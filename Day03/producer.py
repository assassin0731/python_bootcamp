import redis
import json
from sys import argv


def check_digits(argv):
    if len(argv) < 3:
        return False
    if len(argv[0]) != 10 or len(argv[1]) != 10 or not argv[0].isdigit() \
            or not argv[1].isdigit():
        return False
    if not (argv[2].isdigit() or (argv[2][1:].isdigit() and argv[2][0] == '-')):
        return False
    return True


def input_args():
    while True:
        words = ['from', 'to', 'amount']
        numbers = [input(f'{words[i]}: ') for i in range(3)]
        if not check_digits(numbers):
            print('to/from must be digits with 10 length')
        else:
            break
    print('Accepted')
    to = numbers[1]
    from_ = numbers[0]
    amount = numbers[2]

    message = dict()
    message['metadata'] = dict()
    message['amount'] = int(amount)
    message['metadata']['from'] = int(from_)
    message['metadata']['to'] = int(to)


    return message


if __name__ == '__main__':
    r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    while True:
        r.publish('my-channel-1', json.dumps(input_args()))
