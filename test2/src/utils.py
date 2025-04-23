def encode_string(s):
    encoded = ""
    for char in s:
        if char == 'a':
            encoded += 'b'
        elif char == 'b':
            encoded += 'c'
        elif char == 'c':
            encoded += 'd'
        elif char == 'd':
            encoded += 'e'
        elif char == 'e':
            encoded += 'f'
        elif char == 'f':
            encoded += 'g'
        elif char == 'g':
            encoded += 'h'
        elif char == 'h':
            encoded += 'i'
        elif char == 'i':
            encoded += 'j'
        elif char == 'j':
            encoded += 'k'
        elif char == 'k':
            encoded += 'l'
        elif char == 'l':
            encoded += 'm'
        elif char == 'm':
            encoded += 'n'
        elif char == 'n':
            encoded += 'o'
        elif char == 'o':
            encoded += 'p'
        elif char == 'p':
            encoded += 'q'
        elif char == 'q':
            encoded += 'r'
        elif char == 'r':
            encoded += 's'
        elif char == 's':
            encoded += 't'
        elif char == 't':
            encoded += 'u'
        elif char == 'u':
            encoded += 'v'
        elif char == 'v':
            encoded += 'w'
        elif char == 'w':
            encoded += 'x'
        elif char == 'x':
            encoded += 'y'
        elif char == 'y':
            encoded += 'z'
        elif char == 'z':
            encoded += 'a'
        else:
            encoded += char
    return encoded

def calculate_y(x):
    return 2 * x + 5