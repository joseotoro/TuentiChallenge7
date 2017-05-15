from math import ceil

with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()
    cases = int(lines[0])
    lines = lines[1:]


with open('output.txt', 'w') as out:
    for case in range(cases):
        slices = lines[2 * case + 1].split()
        total = ceil(sum(map(int, slices)) / 8.0)
        out.write('Case #{}: {}\n'.format(case + 1, total))
