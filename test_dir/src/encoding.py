def encode_string(input_string):
    encoded_string = ""
    for char in input_string:
        if char == 'a':
            encoded_string += 'b'
        elif char == 'b':
            encoded_string += 'c'
        elif char == 'c':
            encoded_string += 'd'
        elif char == 'd':
            encoded_string += 'e'
        elif char == 'e':
            encoded_string += 'f'
        elif char == 'f':
            encoded_string += 'g'
        elif char == 'g':
            encoded_string += 'h'
        elif char == 'h':
            encoded_string += 'i'
        elif char == 'i':
            encoded_string += 'j'
        elif char == 'j':
            encoded_string += 'k'
        elif char == 'k':
            encoded_string += 'l'
        elif char == 'l':
            encoded_string += 'm'
        elif char == 'm':
            encoded_string += 'n'
        elif char == 'n':
            encoded_string += 'o'
        elif char == 'o':
            encoded_string += 'p'
        elif char == 'p':
            encoded_string += 'q'
        elif char == 'q':
            encoded_string += 'r'
        elif char == 'r':
            encoded_string += 's'
        elif char == 's':
            encoded_string += 't'
        elif char == 't':
            encoded_string += 'u'
        elif char == 'u':
            encoded_string += 'v'
        elif char == 'v':
            encoded_string += 'w'
        elif char == 'w':
            encoded_string += 'x'
        elif char == 'x':
            encoded_string += 'y'
        elif char == 'y':
            encoded_string += 'z'
        elif char == 'z':
            encoded_string += 'a'
        else:
            encoded_string += char
    return encoded_string

def calculate_y(x):
    return 2 * x + 5