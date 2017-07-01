import ADNACII as adnacii

molecules = ['a', 'g', 't', 'c']
strand = []

def openSpecial():
    adnacii.openSpecial()

def textConvert():
    text = adnacii.converter()
    save = input("Would you like to save your strand? y or n: ")
    if save == "y":
        filename = input("What would you like the filename to be? ")
        with open(filename, 'w') as f:
            f.write(str(text))
        print("file saved")

def specialPrint():
    file = input("Which file? ")
    import printfcli as pf
    pf.specialPrint(file)

while 1 == 1:
    action = input("would you like to open a file, convert standard text. or print a file? ")
    if action == "open":
        openSpecial()
    elif action == "print":
        specialPrint()
    elif action == "convert":
        textConvert()

