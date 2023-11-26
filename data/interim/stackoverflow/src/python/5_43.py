def oldMacdonald():
    return "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n"

def verseFor(animal, sound):
    lyrics = oldMacdonald() + "And on his farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!\n" \
                                                                        "With a " + sound + ", " + sound + " here and a " + sound + ", " \
                                                                                                                                             "" + sound + ".\nHere a " + sound + ", there a " + sound + ", " \
                                                                                                                                                                                                                 "everywhere a " + sound + ", " + sound + "\n" + oldMacdonald()

    return lyrics

def main():
    for animal,sound in zip(["cow", "pig", "horse", "chick", "sheep"],["moo", "oink", "neigh", "cluck", "bahh"]):
        print(verseFor(animal, sound))

main()
