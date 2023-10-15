import colorgram

if __name__ == '__main__':
    colors = colorgram.extract('image.jpg', 6)
    palette = []
    for i in colors:
        currentcolor = (i.rgb.r, i.rgb.g, i.rgb.b)
        palette.append(currentcolor)
    print(palette)



