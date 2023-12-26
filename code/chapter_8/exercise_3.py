fabacae = ['lentil', 'bean', 'acacia', 'soya']
brassicace = ['radish', 'rocket', 'cabbage']

item = input('vegetable: ')
match item:
    case f if item in fabacae:
        print('fabacae')
    case b if item in brassicace:
        print('brassicace')
    case _:
        print('I don\'t know')