import redis
import json
from sys import argv
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e')
    args = parser.parse_args()
    if args.e:
        bad_guys = argv[2].split(',')
    else:
        bad_guys = []

    r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    sub = r.pubsub()
    sub.subscribe('my-channel-1')
    for message in sub.listen():
        if not isinstance(message['data'], int):
            make_json = json.loads(message['data'])
            if str(make_json['metadata']['to']) in bad_guys and \
                    int(make_json['amount']) > 0:
                make_json['metadata']['to'], make_json['metadata']['from'] = \
                    make_json['metadata']['from'], make_json['metadata']['to']
            print(json.dumps(make_json))
