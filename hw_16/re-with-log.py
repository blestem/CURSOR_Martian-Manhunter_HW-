import re
import os

if os.path.exists('secret.log'):
    os.remove('secret.log')
with open('django_success (2).log', 'r') as logfile:
    while True:
        line = logfile.readline()
        if not line:
            break
        line = re.sub(r'\[\d*/\w*/\d*\s(\d{2}:\d{2}:\d{2})\]', '[XX/XXX/XXXX XX:XX:XX]', line)

        line = re.sub(r'\/admin\/', '/****/', line)

        with open('secret.log', 'a') as file:
            file.write(line)

