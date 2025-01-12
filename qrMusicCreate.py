import qrcode
from qrcode.constants import ERROR_CORRECT_L
import re

def ultra_minimize_html(content):
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'>\s+<', '><', content)
    
    # Remove quotes where possible
    content = re.sub(r'(\w+)="([^"]+)"', lambda m: 
        f'{m.group(1)}={m.group(2)}' if m.group(2).isalnum() else m.group(0), content)
    
    replacements = {
        'document.getElementById': 'document.get',
        'function ': 'function',
        'return ': 'return',
        'const ': 'let ',
        'addEventListener': 'on',
        'onmousedown': 'onmd',
        'onmouseup': 'onmu',
        'onmouseleave': 'onml',
        'createOscillator': 'createO',
        'createGain': 'createG'
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    return content.strip()

with open('qrMusicMin.html', 'r') as f:
    html = f.read()

minimized = ultra_minimize_html(html)

qr = qrcode.QRCode(
    version=40,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(minimized)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrMusic.png")

# Print stats
print(f"Original size: {len(html)} bytes")
print(f"Minimized size: {len(minimized)} bytes")