# oldMacDonald.py
# Program to print out the song Old MacDonald Had a Farm

def oldMacD():
    print('Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!')

def animal(name, sound):
    print('And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!'.format(name))
    print('With a {0}, {0} here and a {0}, {0} there.'.format(sound))
    print('Here a {0}, there a {0}, everywhere a {0}, {0}.'.format(sound))

def main():
    oldMacD()
    animal('cow', 'moo')
    oldMacD()
    print()

    oldMacD()
    animal('turkey', 'gobble')
    oldMacD()
    print()

    oldMacD()
    animal('pig', 'oink')
    oldMacD()

main()

 









