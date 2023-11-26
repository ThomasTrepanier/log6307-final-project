import sys

n = int(sys.argv[1])

def drawtriangle(num_lines):
    # prepares the inner triagle in a list and return it together with its width (size).
    size = (2*num_lines)-1
    triangle = []
    for i in range(num_lines):
        white_side = num_lines - i - 1
        asterisks = 2*i + 1
        triangle.append(" "*white_side + "*"*asterisks + " "*white_side)
    return triangle, size

def main(num_lines):
    tr, tr_size = drawtriangle(num_lines)

    for j in range(num_lines):
        for line in tr:
            white_triangles = n - j - 1
            white_size = tr_size * white_triangles
            line_repeat = (2*j) + 1
            print(" "*white_size + line*line_repeat + " "*white_size)

main(n)
