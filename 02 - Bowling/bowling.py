with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()
    cases = int(lines[0])
    lines = lines[1:]


with open('output.txt', 'w') as out:
    for case in range(cases):
        num_rolls = int(lines[2 * case])
        rolls = list(map(int, lines[2 * case + 1].split()))
        score = [0 for _ in range(10)]
        current = 0
        current_score = 0
        first = True
        while current_score < 10:
            if first:
                if rolls[current] == 10:
                    score[current_score] = sum(rolls[current:current+3])
                    current_score += 1
                else:
                    first = False
            else:
                total = rolls[current - 1] + rolls[current]
                if total == 10:
                    score[current_score] = total + rolls[current + 1]
                else:
                    score[current_score] = total
                first = True
                current_score += 1
            current += 1

        for index in reversed(range(10)):
            score[index] = sum(score[:index+1])

        out.write('Case #{}: {}\n'.format(case + 1, ' '.join(map(str, score))))
