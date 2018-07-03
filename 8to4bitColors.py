color_array = '''
0x341234, 0x223333, 0x332211, 0x341234, 0x223333, 0x332211, 0x341234, 0x223333,
0x341234, 0x223333, 0x332211, 0xFFDDEE, 0xCCBBAA, 0x332211, 0x341234, 0x223333,
0x341234, 0x223333, 0x332211, 0x341234, 0x223333, 0x332211, 0x341234, 0x223333,
0x341234, 0x223333, 0x332211, 0x341234, 0x223333, 0x332211, 0x341234, 0x223333
'''

for char in '\n\t ':
    color_array = color_array.replace(char, '')

color_array = color_array.split(',')

processed_color_array = []

for color_string in color_array:
    color_int = int(color_string, 16)

    red = (color_int & 0xFF0000) >> 16
    green = (color_int & 0x00FF00) >> 8
    blue = color_int & 0x0000FF

    red //= 16
    green //= 16
    blue //= 16

    processed_color_array.append('X"{:x}{:x}{:x}"'.format(red, green, blue))

col = 0
out_string = '('
for color in processed_color_array:
    if col == 0:
        out_string += '('

    out_string += color + ', '

    col += 1

    if col == 16:
        out_string = out_string[:-2] + '),\n'
        col = 0

out_string = out_string[:-2] + ');'

print(out_string)
