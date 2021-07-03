from matplotlib import pyplot
from PIL import Image, ImageDraw, ImageFont



def plot(n, inv, start=1, width=900, height=1000, border_x = 10, border_y = 10, r=15):
    '''
    Plots graph for inv.

    n - number of levels plotted
    inv - inverse function (return TOUPLE of numbers)
    start - number on which we start
    '''
    # Currently this is not optimized even a bit
    # we want sizes of every level
    connections = {}
    reverse_connections = {}
    levels = [[start]]
    while len(levels) <= n:
        ans = []
        for i in levels[-1]:
            j = inv(i)
            ans += j
            connections[i] = tuple(j)
            for k in j:
                reverse_connections[k] = i
        levels.append(ans)

    print(levels)
    print(connections)

    img = Image.new('RGB', (width, height), (225, 225, 225, 0))
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/media/Ubuntu-R.ttf', 18)
    coordinates = {}

    n_levels = len(levels)
    dy = (height - 2*border_y ) // (n_levels+1)
    y = border_y +dy
    for level in levels:
        n_nodes = len(level)
        dx = (width - 2*border_x) // (n_nodes +1)
        x = border_x + dx 
        for i in level:
            coordinates[i] = (x, y+r)
            #draws connectzions
            j = reverse_connections.get(i, ())
            x1, y1 = coordinates.get(j, (x, y))
            draw.line((x,y,x1,y1), fill=(0, 0, 0), width=3)

            #draws node
            draw.ellipse((x-r,y-r, x+r, y+r), fill=(180,230,230,50), outline=(0,0,0))
            draw.text((x-r/2,y-4*r/5), str(i),font=fnt, fill=(0,0,0))

            # moves to the next node
            x += dx


        # move to the next line
        y += dy
    img.show()
    
