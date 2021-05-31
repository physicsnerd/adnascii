import string

asciilst = list(string.printable)
alphabet = dict(zip(asciilst, range(1, 101)))

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

def assign(lst, asciilst):
    x = 101
    zipl = lst[:x]
    return dict(zip(asciilst, zipl))

def assign2(lst, asciilst):
    x = 201
    y = 100
    zipl = lst[y:x]
    return dict(zip(asciilst, zipl))

def assign3(lst, asciilst):
    x = 301
    y = 200
    zipl = lst[y:x]
    return dict(zip(asciilst, zipl))

adnascii = assign(initial, asciilst)
adnascii2 = assign2(initial, asciilst)
adnascii3 = assign3(initial, asciilst)
aSearch = dict(zip(adnacii.values(), adnacii.keys()))
a2Search = dict(zip(adnacii2.values(), adnacii2.keys()))
a3Search = dict(zip(adnacii3.values(), adnacii3.keys()))

extraSeqs = len(initial[303:])
adnascii['txt'] = initial[301]
adnascii['dat'] = initial302]

def spacerGen():
    #what all do I need??

def lenAssign(): #add number limitations
    threelist = []
    for i in asciilst:
        print(i)
        torf = input("in 3 len? y or n: ")
        if torf == 'y':
            threelist.append(i)
    return(threelist)

threelist = lenAssign()

#add 3 'type' chars and checksum char
def assignFiveChars():
    done = 'y'
    wordlist = []
    numCheck = extraSeqs
    while done == 'y':
        done = input("would you like to add a(nother) word/control char? y or n: ")
        if numcheck == 0:
            print("Sorry, you can't add any more chars.")
        else:
            if done == 'y':
                word = input("what word/control char? ")
                wordlist.append(word)
            numCheck-=1
    return(wordlist)

wordlist = assignFiveChars()
whoKnows = dict(zip(wordlist, initial[301:])) #in three encodings???

#here fully finish adnascii system...necessary?
def adnasciiFinish():
    #magic here

def addressMake():
    #how to do this??

def checksumMake(data):
    checksum = []
    for i in data:
        checksum.append(adnascii[alphabet[i]])
    return ''.join(checksum)

def encode(char):
    #needs to handle spacers and char encoding
    return encodedChar #doesn't work...how does it tell if next char is 3-seq?

def datType(dataType):
    address = addressMake()
    encodedChars = []
    if dataType == 'text':
        metaTag = adnascii['txt']
        import standard.textFile as textFile
        checksum = checksumMake(textFile)
        for i in textFile:
            encodedChars.append(encode(i))
    else:
        metaTag = adnascii['dat']
        import standard.dataFile as dataFile
        checksum = checksumMake(dataFile)
        for i in dataFile:
            encodedChars.append(encode(i))
    return metaTag + address + ''.join(encodedChars) + checksum

def efficiencyTest():
    typeDict = input("What type of data would you like to test this on - text or database? ")
    if typeDict == 'text':
        endSeq = datType('text')
        print(endSeq)
        print(len(endSeq))
    else:
        endSeq = datType('data')
        print(endSeq)
        print(len(endSeq))

print("testing your system for efficiency...")
