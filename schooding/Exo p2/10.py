def compter_extrait(extrait, texte):
    count = 0
    index = texte.find(extrait)

    while index != -1:
        count += 1
        index = texte.find(extrait, index + 1)

    return count
    
extrait_input = input()
texte_input = input()


result = compter_extrait(extrait_input, texte_input)
print(result)
