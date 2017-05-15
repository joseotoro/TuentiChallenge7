import subprocess

print('Loading magic numbers...')
secrets = {}
with open('magic_numbers.txt', 'r') as f:
    for line in f:
        date, secret_1, secret_2 = line.split()
        secrets[date] = (secret_1, secret_2)
print('Done!')

print('Processing input...')
with open('submitInput.txt', 'r') as f:
    cases = int(f.readline())
    with open('output.txt', 'w') as out:
        for case in range(cases):
            print('Case {}/{}'.format(case + 1, cases))
            user_id, number_dates = f.readline().split()
            number_dates = int(number_dates)
            hash = None
            for _ in range(number_dates):
                d, number_times = f.readline().split()
                number_times = int(number_times)

                secret_1, secret_2 = secrets[d]

                if hash is None:
                    command = "php script.php {} {} {} {}".format(secret_1, secret_2, number_times, user_id)
                else:
                    command = "php script.php {} {} {} {} {}".format(secret_1, secret_2, number_times, user_id, hash)

                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                response = proc.stdout.read().decode('utf-8')

                password = response.split()[0]
                hash = response.split()[1]

            out.write('Case #{}: {}\n'.format(case + 1, password))
print('Finish!')