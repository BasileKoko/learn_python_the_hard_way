filename = 'file.txt'
e = open(filename, 'w')
e.write("First text line\nSecond text line\nThird text line")
e.close()

g = open(filename, 'a')
g.write(' appending new line!')
g.close()

f = open(filename, 'r')
f.read()
f.close()
