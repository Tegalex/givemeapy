from urllib.request import urlopen
with urlopen('http://mailup.com') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)