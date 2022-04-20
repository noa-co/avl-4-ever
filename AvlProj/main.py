from avl_skeleton import *

def tryStuff():
    myTree = AVLTreeList()
    myTree.insert(0, 0)
    myTree.insert(1, 1)
    myTree.insert(2, 2)
    myTree.delete(1)
    printl = lambda n: print(n.getValue())
    myTree.inOrder(myTree.root, printl)



if __name__ == '__main__':
    tryStuff()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
