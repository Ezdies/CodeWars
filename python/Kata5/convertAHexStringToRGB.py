def hex_string_to_RGB(hex_string):
    values = [int(hex_string[i:i+2], 16) for i in range(1, len(hex_string), 2)]
    keys = ['r', 'g', 'b']
    return {key: value for key, value in zip(keys, values)}

print(hex_string_to_RGB('#FF9933'))