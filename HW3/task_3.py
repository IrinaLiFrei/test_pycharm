# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = ('Ants are eusocial insects of the family Formicidae and, along with the related wasps and bees, '
        'belong to the order Hymenoptera. Ants evolved from vespoid wasp ancestors in the Cretaceous period. '
        'More than 13,800 of an estimated total of 22,000 species have been classified. '
        'They are easily identified by their geniculate (elbowed) antennae and the distinctive node-like structure '
        'that forms their slender waists.) '
        'Ants form colonies that range in size from a few dozen predatory individuals living in small natural '
        'cavities to highly organised colonies that may occupy large territories and consist of millions '
        'of individuals. '
        'Larger colonies consist of various castes of sterile, wingless females, most of which are workers (ergates), '
        'as well as soldiers (dinergates) and other specialised groups. Nearly all ant colonies also have some '
        'fertile males called "drones" and one or more infertile females called "queens" (gynes). '
        'The colonies are described as superorganisms because the ants appear to operate as a unified entity, '
        'collectively working together to support the colony. '
        'Ants have colonised almost every landmass on Earth. The only places lacking indigenous ants are Antarctica '
        'and a few remote or inhospitable islands. Ants thrive in moist tropical ecosystems and may exceed the '
        'combined biomass of wild birds and mammals. Their success in so many environments has been attributed '
        'to their social organisation and their ability to modify habitats, tap resources, and defend themselves. '
        'Their long co-evolution with other species has led to mimetic, commensal, parasitic, '
        'and mutualistic relationships.').lower().replace(',', ' ').replace('.', ' ').split()

word_counts = {}
for word in text:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print('10 самых частых слов: ')
for word, count in sorted_word_counts[:10]:
    print(f'{word}: {count}')
