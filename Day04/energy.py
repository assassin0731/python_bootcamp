def check_str(x):
    return isinstance(x, str)


def fix_wiring(cab, sock, plug):
    cab = filter(check_str, cab)
    sock = filter(check_str, sock)
    plug = filter(check_str, plug)
    for c, s in zip(cab, sock):
        try:
            p = next(plug)
        except StopIteration:
            p = None
        if p:
            yield f'plug {c} into {s} using {p}'
        else:
            yield f'weld {c} to {s} without plug'


if __name__ == '__main__':
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    for c in fix_wiring(cables, sockets, plugs):
        print(c)

    print()
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
