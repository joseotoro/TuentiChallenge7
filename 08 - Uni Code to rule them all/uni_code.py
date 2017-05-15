import re

# Textfile previously saved with sublime text (utf-8 encoding)
# to delete other characters

r_number = re.compile('\d+')
r_alpha = re.compile('[^ \t\n\r\f\v\d]')
with open('submitInput.txt', 'r') as f:
    cases = int(f.readline())
    with open('output.txt', 'w') as out:
        for case in range(cases):
            x = f.readline().strip()
            if r_alpha.search(x) is not None or \
                    len(r_number.findall(x)) != 1:
                out.write('Case #{}: N/A\n'.format(case + 1))
            else:
                number = int(x.strip())
                out.write('Case #{}: {}\n'.format(case + 1, hex(number)[2:]))


