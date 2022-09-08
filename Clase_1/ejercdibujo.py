#pip install Pillow
 
from PIL import Image

IMG = "D:\Archivos rápidos\dyc.jpeg"
WIDTH = 421
HEIGHT = 384
OUTPUT = "D:\Archivos rápidos\dyc.txt"


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# La relación de mapeo entre personajes y RGB
def get_char(r,g,b,alpha=256): #originalmente estaba en 256
    if alpha == 0 :
        return ' '
    lenght = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) # gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/lenght
    return ascii_char[int(gray/unit)]

#Si se ejecuta por sí solo, ejecute lo siguiente, si es un módulo importado, no se ejecutará
if __name__ == '__main__':
    im = Image.open(IMG)
    # Aquí está el tamaño de la imagen convertida, y luego el segundo parámetro representa la calidad de la imagen, hay 4 tipos, Imagen de baja calidad. NEARSET, Imagen bilineal. BILINEAR, Imagen de interpolación spline cúbica.
    im = im.resize((WIDTH,HEIGHT),Image.BILINEAR)
    txt = ""

    for h in range(HEIGHT):
        for w in range(WIDTH):
            # im.getpixel: Obtenga los tres valores de r, gyb correspondientes a RGB según las coordenadas. Aquí, los dos corchetes de getpixel ((i, j)) son muy importantes
            txt += get_char(*im.getpixel((w,h)))
        txt += '\n'
    print(txt)

# Salida de caracteres a archivo
if OUTPUT:
    with open(OUTPUT,'w') as f:
        f.write(txt)
else:
    with open("output.txt",'w') as f:
        f.write(txt)

