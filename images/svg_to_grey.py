import re

def svg_to_greyscale(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        svg = f.read()
    # Replace hex colors with greyscale
    def to_grey(match):
        hex_color = match.group(1)
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        grey = int(0.3*r + 0.59*g + 0.11*b)
        grey_hex = f"{grey:02x}"*3
        return f'#{grey_hex}'
    svg = re.sub(r'#([0-9a-fA-F]{6})', to_grey, svg)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

# Usage:
svg_to_greyscale('py.svg', 'grey.svg')
