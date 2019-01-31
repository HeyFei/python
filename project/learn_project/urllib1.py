import urllib.request
import urllib.parse
import urllib.error


fhand = urllib.request.urlopen('http://www.1990wedding.com/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        print(counts)
        break

        counts[word] = counts.get(word, 0) + 1
print(counts)
