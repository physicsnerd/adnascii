import string

asciilst = list(string.printable)
alphabet = dict(zip(asciilst, range(1, 101)))
addresses = []

chars = ['a','g','c','t']
start = ['a','a','a','a','a']
adnacii = {}
extra = []
initial = []

def last_char(lst):
    for i in chars:
        start[4] = i
        initial.append(start[:])

def nextlast_char(lst):
    for i in chars:
        start[3] = i
        last_char(lst)

def nnlchar(lst):
    for i in chars:
        start[2] = i
        nextlast_char(lst)

def nnnlchar(lst):
    for i in chars:
        start[1] = i
        nnlchar(lst)

def nnnnlchar(lst):
    for i in chars:
        start[0] = i
        nnnlchar(lst)

def join(lst):
    for i in lst:
        lst[lst.index(i)] = ''.join(i)

def check(lst):
    lst[:] = [x for x in lst if 'tt' not in x]
    lst[:] = [x for x in lst if 'gg' not in x]
    lst[:] = [x for x in lst if 'aa' not in x]
    lst[:] = [x for x in lst if 'cc' not in x]

nnnnlchar(start)
join(initial)
check(initial)

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

adnacii = assign(initial, asciilst)
adnacii2 = assign2(initial, asciilst)
adnacii3 = assign3(initial, asciilst)
aSearch = dict(zip(adnacii.values(), adnacii.keys()))
a2Search = dict(zip(adnacii2.values(), adnacii2.keys()))
a3Search = dict(zip(adnacii3.values(), adnacii3.keys()))

def extraassign(lst):
    x = 307
    return lst[x:]

extraassign(initial)

adnacii[' end_str '] = initial[301]
adnacii2[' end_str '] = initial[302]
adnacii3[' end_str '] = initial[303]
adnacii[' ad_b '] = initial[304]
adnacii[' ad_e '] = initial[305]
adnacii[' full_end '] = initial[306]
adnacii[' spacer1 '] = 'c'
adnacii[' spacer2 '] = 'a'

def three_con(txt, asys):
    lst = []
    for i in txt:
        lst.append(asys[i])
    x = 0
    seq = lst[x:x+5]
    lchar = ''
    return lst

def address():
    global addresses
    ad1 = ''
    rem = input("Would you like to reset the address list to empty? y or n: ")
    if rem == 'y':
        addresses = []
    if len(addresses) == 0:
        ad1 = 0
    else:
        ad1 = addresses[-1] + 1
    addresses.append(ad1)
    ad1 = adnacii[' ad_b '] + adnacii[str(ad1)] + adnacii[' ad_e ']
    return ad1

def converter():
    txt = input("What text would you like to be converted? ")
    dnatxt = three_con(txt, adnacii)
    checksum = 0
    x = 0
    seq = dnatxt[x:x+5]
    for seq in dnatxt:
        checksum = checksum + alphabet[aSearch[seq]]
        x+=6
        seq = dnatxt[x:x+5]
    checksum = list(str(checksum))
    csencode = []
    for i in checksum:
        csencode.append(adnacii[i])
    checksum = csencode
    dnatxt2 = three_con(txt, adnacii2)
    dnatxt3 = three_con(txt, adnacii3)
    endtxt = list(address()) + dnatxt + list(adnacii[' end_str ']) + dnatxt2 + list(adnacii2[' end_str ']) + dnatxt3 + list(adnacii3[' end_str ']) + checksum +  list(adnacii[' full_end '])
    endtxt = list(''.join(endtxt))
    x = 0
    seq = endtxt[x:x+5]
    print(endtxt)
    while ''.join(seq) != adnacii[' full_end ']:
        print(seq)
        lchar = seq[-1]
        if lchar == 'a' or lchar == 'g' or lchar == 't':
            endtxt[x+5:] = list(adnacii[' spacer1 ']) + endtxt[x+5:]
        else:
            endtxt[x+5:] = list(adnacii[' spacer2 ']) + endtxt[x+5:]
        x+=5
        seq = endtxt[x:x+5]
    endtxt = ''.join(endtxt)
    print(endtxt)
    return endtxt

def checkSeq(a1l, a2l, a3l, data):
    if a1l == a2l == a3l:
        return ''.join(a1l)
    else:
        cs1 = 0
        for i in a1l:
            cs1 = cs1 + alphabet[i]
        cs2 = 0
        for i in a2l:
            cs2 = cs2 + alphabet[i]
        cs3 = 0
        for i in a3l:
            cs3 = cs3 + alphabet[i]
        checksum = []
        x = data.index(adnacii3[' end_str ']) + 6
        seq = data[x:x+5]
        while seq != adnacii[' full_end ']:
            checksum.append(aSearch[seq])
            x+=6
            seq = data[x:x+5]
        checksum = sum(checksum)
        if cs1 == checksum:
            return ''.join(a1l)
        elif cs2 == checksum:
            return ''.join(a2l)
        elif cs3 == checksum:
            return ''.join(a3l)
        else:
            print("Opt. 1: " + ''.join(a1l))
            print("Opt. 2: " + ''.join(a2l))
            print("Opt. 3: " + ''.join(a3l))
            wr = input("Which one makes the most sense - opt1, opt2, or opt3? ")
            if wr == 'opt1':
                return ''.join(a1l)
            elif wr == 'opt2':
                return ''.join(a2l)
            else:
                return ''.join(a3l)

def reader(data):
    a1l = []
    x = data.index(adnacii[' ad_e ']) + 6
    seq = data[x:x+5]
    while seq != adnacii[' end_str ']:
        a1l.append(aSearch[seq])
        x+=6
        seq = data[x:x+5]
    x+=6
    seq = data[x:x+5]
    a2l = []
    while seq != adnacii2[' end_str ']:
        a2l.append(a2Search[seq])
        x+=6
        seq = data[x:x+5]
    x+=6
    seq = data[x:x+5]
    a3l = []
    while seq != adnacii3[' end_str ']:
        a3l.append(a3Search[seq])
        x+=6
        seq = data[x:x+5]
    return checkseq(a1l, a2l, a3l, data)

def openSpecial():
    file = input("Which file? ")
    try:
        with open(file, 'r') as myfile:
            data = myfile.read()
            print(reader(data))
    except FileNotFoundError:
        print("file not found")
        return None
