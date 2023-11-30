from sys import stdin

lines = []
for line in stdin:
    if line[:5] == '00000' and line[5] != '0' and len(line.rstrip()) == 32:
        lines.append(line.rstrip())

print(*lines, sep='\n')
