from sys import stdin

num_line = 1
ans = True

lines = [line.rstrip() for line in stdin.readlines()]

for line in lines:
    if len(line) != 5:
        ans = 'Error'
        break
    if num_line == 1:
        if line[0] == line[-1] == '*' and '*' not in line[1:4]:
            pass
        else:
            ans = False
    elif num_line == 2:
        if line[:2] == line[3:] == '**' and line[2] != '*':
            pass
        else:
            ans = False
    elif num_line == 3:
        if line[0] == line[2] == line[-1] == '*' and line[1] != '*' and line[3] != '*':
            pass
        else:
            ans = False
    else:
        ans = 'Error'
    num_line += 1

print(ans)
