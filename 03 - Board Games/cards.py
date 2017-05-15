with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()
    cases = int(lines[0])
    lines = lines[1:]


with open('output.txt', 'w') as out:
    for case in range(cases):
        number = int(lines[case])
        cards = [1]
        while sum(cards) + 1 < number:
            cards.append(sum(cards) + 1)
        total = len(cards)
        out.write('Case #{}: {}\n'.format(case + 1, total))
