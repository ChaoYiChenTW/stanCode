"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return GRAPH_MARGIN_SIZE + (width - GRAPH_MARGIN_SIZE*2) // len(YEARS) * year_index


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)    # Write your code below this line
    for year_index in range(len(YEARS)):
        year_x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(year_x, 0, year_x, CANVAS_HEIGHT)
        canvas.create_text(year_x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, anchor=tkinter.NW, text=YEARS[year_index])
    #################################


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    y_height = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000
    for j in range(len(lookup_names)):
        name = lookup_names[j]
        color = COLORS[j]
        if name in name_data:
            name_d = name_data[name]
            if str(YEARS[0]) not in name_d:
                rank = '*'
                y0 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            else:
                rank = name_d[str(YEARS[0])]
                y0 = int(rank)*y_height + GRAPH_MARGIN_SIZE
            x0 = GRAPH_MARGIN_SIZE + TEXT_DX
            canvas.create_text(x0, y0, text=f'{name} {rank}', anchor=tkinter.SW, fill=color)
            for i in range(1, len(YEARS)):
                x1 = GRAPH_MARGIN_SIZE + (CANVAS_WIDTH - GRAPH_MARGIN_SIZE*2) // len(YEARS) * i + TEXT_DX
                if str(YEARS[i]) not in name_d:
                    rank = '*'
                    y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                else:
                    rank = name_d[str(YEARS[i])]
                    if int(rank) > 1000:
                        rank = '*'
                        y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    else:
                        y1 = int(rank)*y_height + GRAPH_MARGIN_SIZE
                canvas.create_text(x1, y1, text=f'{name} {rank}', anchor=tkinter.SW, fill=color)
                canvas.create_line(x0, y0, x1, y1, fill=color, width=LINE_WIDTH)
                x0 = x1
                y0 = y1
    # Write your code below this line
    #################################


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
