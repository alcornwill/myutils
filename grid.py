from PIL import ImageFont, Image, ImageDraw


W, H = 128, 128
h, v = 8, 8
sx, sy = W/v, H/h
# ox, oy = 0, 0
ox, oy = sx/2, sy/2
color = "LightCyan"

img = Image.new('RGBA', (W, H), "white")
draw = ImageDraw.Draw(img)

for y in range(h):
    dy = oy + y * sy
    a = (0, dy)
    b = (W, dy)
    draw.line((a, b), color)
for x in range(v):
    dx = ox + x * sx
    a = (dx, 0)
    b = (dx, H)
    draw.line((a, b), color)
    
img.save('grid.png')