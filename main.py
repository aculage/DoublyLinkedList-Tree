from tkinter import *
from tkinter import ttk
from linkedlist import *
from tree import *

mainWindow = Tk()
mainWindow.title("Task 2, Navoitsev Denis, IKBO-06-18")
mainWindow.geometry("800x600")
tab = ttk.Notebook(mainWindow)

tabList = ttk.Frame(tab)
tab.add (tabList, text = "Doubly Linked List")
tab.pack(expand=1, fill='both')

loclist = DoublyLinkedList()    
#input fields
inputFieldL = Entry(tabList, width = 40, font= ("Consolas", 18))
inputFieldL.grid(column =1, row =1)
inputFieldL.focus()

#info fields
labelL = Label(tabList, text='Input real values:', font= ("Consolas", 18))
labelL.grid(column =1, row =0)

def listInput():
    try:
        dataIn = inputFieldL.get().split()
        for i in dataIn:
            loclist.insert_at_end(i)
        labelL.configure(text ='Succesful input')
    except Exception:
        labelL.configure ('DataType exception occured', 'Check your input')

def listPrint():
    labelL.configure(text = loclist.traverse_list())

def listReverse():
    revlist = DoublyLinkedList()
    revlist = loclist
    revlist.reverser()
    labelL.configure(text = revlist.traverse_list())

inputButtonL = Button(tabList, text = "Append", font=("Consolas", 18), command = listInput)
inputButtonL.grid(column = 0, row = 2)

printButtonL = Button(tabList, text = "Print", font=("Consolas", 18), command = listPrint)
printButtonL.grid(column = 0, row = 3)

#reverse button
sumButtonL = Button(tabList, text = "Copy and Reverse", font = ("Consolas", 18), command = listReverse)
sumButtonL.grid(column = 1, row = 2)

#######################################################################################################################################################################################
 
tabTree = ttk.Frame(tab)
tab.add (tabTree, text = "Check AVL Tree")
tab.pack(expand=1, fill='both')

tree = BSTree()


labelt = Label(tabTree, text='Input array of integer values:', font= ("Consolas", 18))
labelt.pack()

#input fields
inputFieldL = Entry(tabTree, width = 40, font= ("Consolas", 18))
inputFieldL.pack()
inputFieldL.focus()

#drawblock
canvas = Canvas(tabTree, width=500, height=50, background="White")

canvas.pack()
x=250
y=20
r=10



#buttons
def treeInput():
    try:
        dataIn = inputFieldL.get().split()
        for i in dataIn:
            tree.put( int(i) )
        labelt.configure(text ='Succesful input')
    except Exception:
        labelt.configure ('DataType exception occured', 'Check your input')

inputButtonT = Button(tabTree, text = "Input", font=("Consolas", 18), command = treeInput)
inputButtonT.pack()

def drawTree():
    treetolist = tree.traverse(tree.root)
    print(treetolist)
    canvas.create_text(x,y,text = treetolist)
    print(tree.height(tree.root))
    
def checkAVL():
    
    tree.checkIfAVL(tree.root)
    if tree.AVL : canvas.create_text(x,y+10, text = 'TREE IS AVL')
    else :  canvas.create_text(x,y+10, text = 'TREE IS NOT AVL') 

def cleartree():
    tree = BSTree()

def clearcanvas():
    canvas.delete("all")

drawButtonT = Button(tabTree, text = "Draw", font=("Consolas", 18), command = drawTree )
drawButtonT.pack()

checkbuttonT = Button(tabTree, text = "Check AVL", font=("Consolas", 18), command = checkAVL)
checkbuttonT.pack()

clearcanvasT = Button(tabTree, text = "Clear canvas", font=("Consolas", 18), command = clearcanvas)
clearcanvasT.pack()

cleartreeT = Button(tabTree, text = "Clear tree", font=("Consolas", 18), command = cleartree)
cleartreeT.pack()


mainWindow.mainloop()