from statistics import stdev
from math import ceil


def draw_rectangle(window, turtle, top_left_coord, bottom_right_coord):
    bottom_left_coord = (top_left_coord[0], bottom_right_coord[1])
    top_right_coord = (bottom_right_coord[0], top_left_coord[1])

    # Move the turtle to the top left of the rectangle
    turtle.up()
    turtle.setpos(*top_left_coord)

    # Draw the rectangle
    turtle.down()
    turtle.setpos(*top_right_coord)
    turtle.setpos(*bottom_right_coord)
    turtle.setpos(*bottom_left_coord)
    turtle.setpos(*top_left_coord)


def calculate_cells(data):
    """Calculates the number of cells a set of data can be represented with
    based ont its standard deviation."""
    cell_size = int(stdev(data))
    data_range = max(data) - min(data)

    return ceil(data_range / cell_size)


def draw_graph_grid(window, turtle, data_points,
                    top_left_coord, bottom_right_coord,
                    pencolor=(220, 220, 220)):
    # Set the turtle pencolor, default to gray
    original_pencolor = turtle.pencolor()
    window.colormode(255)
    turtle.pencolor(pencolor)

    # Calculate the size of each cell
    horizontal_len = bottom_right_coord[0] - top_left_coord[0]
    vertical_len = top_left_coord[1] - bottom_right_coord[1]

    num_horizontal_cells = len(data_points)
    num_vertical_cells = calculate_cells(data_points)

    cell_horizontal_len = horizontal_len // num_horizontal_cells
    cell_vertical_len = vertical_len // num_vertical_cells

    # Draw the vertical lines
    turtle.up()
    turtle.setpos(*top_left_coord)
    for i in range(num_horizontal_cells-1):
        # Move one cell to the right
        turtle.up()
        turtle.forward(cell_horizontal_len)
        # Turn to face into the grid
        if i % 2 == 0:
            turtle.right(90)
        else:
            turtle.left(90)

        # Draw the vertical line
        turtle.down()
        turtle.forward(vertical_len)

        # Turn back
        if i % 2 == 0:
            turtle.left(90)
        else:
            turtle.right(90)

    # Draw the horizontal lines
    turtle.up()
    turtle.setpos(*top_left_coord)
    turtle.right(90)
    for i in range(num_vertical_cells-1):
        # Move one cell down
        turtle.up()
        turtle.forward(cell_vertical_len)

        # Turn the face into the grid
        if i % 2 == 0:
            turtle.left(90)
        else:
            turtle.right(90)

        # Draw the horizontal line
        turtle.down()
        turtle.forward(horizontal_len)

        # Turn the face into the grid
        if i % 2 == 0:
            turtle.right(90)
        else:
            turtle.left(90)

    # Reset the turtle pencolor
    turtle.pencolor(original_pencolor)

    x_axes_points = []
    for i in range(1, num_horizontal_cells):
        x_axes_points.append(top_left_coord[0] + i*cell_horizontal_len)

    y_axes_points = []
    for i in range(1, num_vertical_cells):
        y_axes_points.append(top_left_coord[1] + i*cell_vertical_len)

    return (x_axes_points, y_axes_points)


def create_graph(window, turtle, data_points, axes=None):
    """Creates and displays a turtle graph on the given window

    Based on the values, a line graph will be displayed, showing all the data
    points.

    window      - The turtle window to display the graph on
    turtle      - The turtle to use to draw the graph
    data_points - The data points of the graph
    axes        - The x-axis values at each data point. The number of elements
                  in this list should be the same as the number of data points
                  in [values]. If there is no x-axis value at that point, its
                  value should be None. If no axes are needed, this can be
                  None.
                  Default to None.
    """
    horizontal_padding = 30
    vertical_padding = 30

    # Box out an area where the graph should be
    top_left_coord = (horizontal_padding, vertical_padding)
    bottom_right_coord = (window.window_width() - horizontal_padding,
                          window.window_height() - vertical_padding)

    draw_rectangle(window, turtle, top_left_coord, bottom_right_coord)
    x_axes_points, y_axes_points = draw_graph_grid(
        window, turtle, data_points,
        top_left_coord=top_left_coord,
        bottom_right_coord=bottom_right_coord)
