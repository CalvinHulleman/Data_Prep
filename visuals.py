import re
import urllib.request
import matplotlib.pyplot as plt

hand = urllib.request.urlopen('https://www.gutenberg.org/cache/epub/1023/pg1023-images.html')

chapter = 0
chapter_list = [0]
counts_esther = [0]
counts_guppy = [0]
for line in hand:
    line = line.decode().strip()
    new_chapter = re.search('CHAPTER',line)
    if new_chapter:
        chapter += 1
        chapter_list.append(chapter)
        counts_esther.append(0)
        counts_guppy.append(0)
    count_e = len(re.findall('Esther', line))
    count_g = len(re.findall('Guppy', line))
    counts_esther[chapter] += count_e
    counts_guppy[chapter] += count_g

print(counts_esther)

plt.plot(chapter_list,counts_esther,color='red')
plt.plot(chapter_list,counts_guppy,color='blue')
plt.xlabel('Chapter')
plt.ylabel('# of Mentions')
plt.title('Character appearances in Bleak House')
plt.legend(['Esther','Mr. Guppy'])
plt.show
plt.savefig('esther.png',dpi=200)
