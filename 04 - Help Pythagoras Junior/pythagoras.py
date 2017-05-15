with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()
    cases = int(lines[0])
    lines = lines[1:]


with open('output.txt', 'w') as out:
    for case in range(cases):
        sides = list(map(int, lines[case].split()[1:]))
        sides.sort()

        best = -1
        best_k = 2 ** 32 + 1
        i = 0
        while i < len(sides) - 2:
            if i >= best_k:
                break
            j = i + 1
            while j < len(sides) - 1:
                if j >= best_k:
                    break
                k = j + 1
                while k < len(sides):
                    if sides[i] + sides[j] > sides[k]:
                        if best == -1:
                            best = sides[i] + sides[j] + sides[k]
                        else:
                            best = min(best, sides[i] + sides[j] + sides[k])
                        best_k = min(k, best_k)
                    k += 1
                j += 1
            i += 1

        if best != -1:
            out.write('Case #{}: {}\n'.format(case + 1, best))
        else:
            out.write('Case #{}: IMPOSSIBLE\n'.format(case + 1))
