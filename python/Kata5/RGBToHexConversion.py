def rgb(r, g, b):
    colors = ['00' if color <= 0 else 'FF' if color >= 255 else '0' + hex(color)[2:].upper() if color < 16 else hex(color)[2:].upper() for color in (r,g,b)]
    return ''.join(colors)
    
print(rgb(61 ,144 ,14))