def two_string(a, b):
    for i, ca in enumerate(a):
        # Prevent index out of bounds
        if i < len(b) and b[i] == ca:
            print(i, ca)


two_string('The Holy Grail', 'Life of Brian')
