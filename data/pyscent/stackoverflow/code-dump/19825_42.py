def oldMacdonald():
    return "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"

def a(thing):
    if thing[0] in 'aeiou':
        return f'an {thing}'
    else:
        return f'a {thing}'

def verseFor(animal, sound):
    an_animal = a(animal)
    a_sound = a(sound)

    lyrics = f"""{oldMacdonald()}
And on his farm he had {an_animal}, Ee-igh, Ee-igh, Oh!
With {a_sound}, {sound} here and {a_sound}, {sound} there.
Here {a_sound}, there {a_sound}, everywhere {a_sound}, {sound}.
{oldMacdonald()}
"""
    return lyrics

def main():
    sounds = ["moo", "oink", "neigh", "cluck", "bahh"]
    animals = ["cow", "pig", "horse", "chick", "sheep"]

    for animal, sound in zip(animals, sounds):
        print(verseFor(animal, sound))

main()
