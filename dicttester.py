import string

asciilst = list(string.printable)

chars = ['a','g','c','t']
start = ['a','a','a','a','a']
initial = []
initial2 = []

def last_char(lst, initial, l):
    for i in chars:
        start[l-1] = i
        initial.append(start[:])

def nextlast_char(lst, initial, l):
    for i in chars:
        start[l-2] = i
        last_char(lst, initial, l)

def nnlchar(lst, initial, l):
    for i in chars:
        start[l-3] = i
        nextlast_char(lst, initial, l)

def nnnlchar(lst, initial, l):
    for i in chars:
        start[l-4] = i
        nnlchar(lst, initial, l)

def nnnnlchar(lst, initial, l):
    for i in chars:
        start[l-5] = i
        nnnlchar(lst, initial, l)

def join(lst):
    for i in lst:
        lst[lst.index(i)] = ''.join(i)

def check(lst):
    lst[:] = [x for x in lst if 'tt' not in x]
    lst[:] = [x for x in lst if 'gg' not in x]
    lst[:] = [x for x in lst if 'aa' not in x]
    lst[:] = [x for x in lst if 'cc' not in x]

nnnnlchar(start, initial, 5)
join(initial)
check(initial)

start = ['a','a','a']
nnlchar(start, initial2, 3)
join(initial2)
check(initial2)

threelist = []
fivelist = []

def lenAssign():
    for i in asciilst:
        print(i)
        torf = input("in 3 len or 5 len? 3 or 5: ")
        if torf == '3':
            threelist.append(i)
        else:
            fivelist.append(i)

lenAssign()

def wordAdd():
    done = 'y'
    while done == 'y':
        done = input("would you like to add a(nother) word? y or n: ")
        if done == 'y':
            word = input("what word? ")
            leng = input("in 3 len or 5 len? 3 or 5: ")
            if leng == '3':
                threelist.append(word)
            else:
                fivelist.append(word)

wordAdd()
print(threelist)
print(fivelist)

#here fully match ascii with combos, incorporate spacers
x = len(threelist)
y = len(fivelist)
adnascii3 = dict(zip(threelist, initial2))
adnascii5 = dict(zip(fivelist, initial))
extra3 = [x-1:]
extra5 = [y-1:] #this is wrong

def efficiencyTest():
    typeDict = input("What type of data would you like to test this on - text or database? ")
    if typeDict == 'text':
        import standard.textFile as textFile
    else:
        import standard.dataFile as dataFile
