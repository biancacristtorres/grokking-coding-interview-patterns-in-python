def sort_colors(colors):
    red = 0
    white = 0
    blue = len(colors) -1

    if blue == white:
        return colors

    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                temp = colors[red]
                colors[red] = colors[white]
                colors[white] = temp
            red+=1
            white+=1
            
        if white <= blue and colors[white] == 1:
            white+=1  

        if white <= blue and colors[white] == 2:
            if colors[blue] != 2:
                temp = colors[blue]
                colors[blue] = colors[white]
                colors[white] = temp
            blue-=1

    return colors

test = [0, 1, 0]
result = sort_colors(test)
print(result)