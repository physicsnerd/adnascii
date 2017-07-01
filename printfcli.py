allowed = ['a', 'g', 'c', 't']

def aprint():
    print('a')

def gprint():
    print('g')

def cprint():
    print('c')

def tprint():
    print('t')

def specialPrint(file):
    try:
        with open(file, 'r') as myfile:
            data = myfile.read()
            for i in data:
                if i in allowed:
                    if i == 'a':
                        aprint()
                    elif i == 'g':
                        gprint()
                    elif i == 'c':
                        cprint()
                    else:
                        tprint()
    except FileNotFoundError:
        print('file not found')
