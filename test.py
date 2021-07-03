import pyperclip

def toStr(list1):
    myStr = ''
    for i in range(len(list1)):
        if i == 0:
            myStr += str(list1[i])
        elif i != len(list1) - 1:
            myStr += ' ,' + str(list1[i])
        else:
            myStr += ' and ' + str(list1[i])
    return myStr

def displayInventory(inventory):
    count = 0
    for k, v in inventory.items():
        print(str(v),',',k)
        count += v
    print('size of inventory is', count)

def addToInventory(inventory, addedItems):
    for items in addedItems:
        inventory.setdefault(items, 0)
        inventory[items] += 1

if __name__ == "__main__":

    stuff = {'rope' : 3, 'dapper': 1, 'torch': 10}
    displayInventory(stuff)

    more = ['knife', 'rope', 'torch', 'rope', 'rope', 'torch']

    addToInventory(stuff, more)
    displayInventory(stuff)

    pyperclip.copy('It\'s a big challenge for me')
    recvBuf = pyperclip.paste()
    print(recvBuf)

    '''
    myList = ['apple', 'pear', 'banana', 123]
    myStr = toStr(myList)
    print(myStr)    
    myList = []
    myStr = toStr(myList)
    '''

    '''
    message = "It's a sunny day and nice to meet you"
    charCount = {}
    for char in message:
        charCount.setdefault(char, 0)
        charCount[char] += 1
    print(charCount)
    '''