with open('submitInput.txt', 'r') as f:
    cases = int(f.readline())
    with open('output.txt', 'w') as out:
        for case in range(cases):
            s, c, d = map(int, f.readline().split())
            if c < 4:
                out.write('Case #{}: 0\n'.format(case + 1))
            else:
                # Apply transformations (missing some for sure)
                total = 4
                c -= 4
                side_a = 0.0
                side_b = 0.0
                used_s = 0
                c_groups = 0
                used_d = 0
                while c >= 8:
                    c -= 8
                    c_groups += 2
                    if side_a <= side_b:
                        side_a += 2
                    else:
                        side_b += 2
                    total += 8
                while s >= 2 and c >= 4:
                    s -= 2
                    c -= 4
                    c_groups += 1
                    total += 6
                    used_s += 2
                    if side_a <= side_b:
                        side_a += 2
                    else:
                        side_b += 2
                while d >= 1 and c >= 4:
                    d -= 1
                    c -= 4
                    used_d += 1
                    c_groups += 1
                    if side_a <= side_b:
                        side_a += 2
                    else:
                        side_b += 2
                    total += 5
                if d % 2 == 1 and s >= 2:
                    d -= 1
                    s -= 2
                    used_d += 1
                    used_s += 2
                    side_a += 2
                    side_b += 2
                    total += 3
                while d >= 2:
                    d -= 2
                    used_d += 2
                    side_a += 2
                    side_b += 2
                    total += 2
                while s >= 2:
                    s -= 2
                    side_b += 1
                    side_a += 1
                    used_s += 1
                    total += 2
                if c_groups >= 1 and s >= 2:
                    c_groups -= 1
                    total += 2
                    s -= 2
                if c_groups >= 1 and d >= 1:
                    c_groups -= 1
                    total += 1
                    d -= 1
                if c_groups >= 2 and s >= 2:
                    total += 2
                    c_groups -= 2
                if c >= 2 and side_a >= 1 and side_b >= 1 and used_s > 0:
                    total += 2
                    c -= 2
                if c >= 2 and used_s >= 2 and c_groups >= 1:
                    total += 2
                    c -= 2

                out.write('Case #{}: {}\n'.format(case + 1, total))


