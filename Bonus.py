# from typing import List
#
# file = open("todo.txt", 'w')
#
# file.write("100.12")
# file.close()
# data = open('todo.txt','r')
# data.close()
# file = open('todo.txt','w')
# data.append("111.23"+'\n')
# file.write()
#
# file.close()
#
# ##  Working with json

import PySimpleGUI as sg

text_label = sg.Text("Select files to compress")
input_file = sg.Input()
inputButton1 = sg.FileBrowse("choose files")
# -- second row

text_label2 = sg.Text("Choose destination folder")
destination = sg.InputText()
outputButton2 =  sg.FolderBrowse(" choose destination")

compress = sg.Button('Compress')
window = sg.Window("zipper app " ,layout=[[text_label , input_file,inputButton1],[text_label2,destination, outputButton2],[compress]])

window.read()