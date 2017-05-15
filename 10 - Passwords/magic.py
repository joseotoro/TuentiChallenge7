from git import Git
from datetime import datetime, timedelta, date


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


g = Git('repo')
deleted_commits = dict()
with open('deleted_commits', 'r') as f:
    for line in f:
        info = g.show(line[:-1])
        commit_id = info.split()[1]
        d = ' '.join(info.split()[7:11])
        datetime = datetime.strptime(d, '%b %d %I:%M:%S %Y')
        deleted_commits[datetime.strftime('%Y-%m-%d')] = commit_id
print('Done!')

print('Getting all secret numbers...')
secrets = {}
start_date = date(2012, 3, 1)
end_date = date(2017, 1, 31)

with open('magic_numbers.txt', 'w') as out:
    for d in date_range(start_date, end_date):
        d = d.strftime('%Y-%m-%d')
        if d in deleted_commits:
            sha1 = deleted_commits[d]
        else:
            log_info = g.log('--before={} 23:59'.format(d),
                             '--all', '-n 1')
            sha1 = log_info.split()[1]
            if log_info.split()[8].zfill(2) != d[-2:]:
                print(log_info.split()[8], d, sha1)

        g.checkout(sha1)
        script = open('repo/script.php', 'r').readlines()
        secret_1 = script[6].split()[2][:-1]
        secret_2 = script[7].split()[2][:-1]
        out.write('{} {} {}\n'.format(d, secret_1, secret_2))
print('Done!')
