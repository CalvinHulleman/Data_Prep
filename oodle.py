import re
import urllib.request
hand = urllib.request.urlopen('https://www.gutenberg.org/cache/epub/1023/pg1023-images.html')
oodles = set()
for line in hand:
    line = line.decode().strip()
    oodle_result = re.findall('[A-Z]+oodle', line)
    if oodle_result != []:
        oodles.update(oodle_result)
print(sorted(oodles))
