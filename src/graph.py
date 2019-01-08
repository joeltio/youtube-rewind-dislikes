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
    draw_outline(window, turtle)
    draw_grid(window, turtle, data_points)
    draw_data_points()


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


def draw_outline(window, turtle, padding_horizontal=30, padding_vertical=30):
    height = window.window_height()
    width = window.window_width()

    top_left = (padding_horizontal, padding_vertical)
    bottom_right = (width - padding_horizontal, height - padding_vertical)
    draw_rectangle(window, turtle, top_left, bottom_right)
