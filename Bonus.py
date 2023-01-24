from typing import List

file = open("todo.txt", 'w')

file.write("100.12")
file.close()
data = open('todo.txt','r')
data.close()
file = open('todo.txt','w')
data.append("111.23"+'\n')
file.write()

file.close()

