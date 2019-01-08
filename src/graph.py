def create_graph(window, turtle, values, axes=None):
    """Creates and displays a turtle graph on the given window

    Based on the values, a line graph will be displayed, showing all the data
    points.

    window - The turtle window to display the graph on
    turtle - The turtle to use to draw the graph
    values - The data points of the graph
    axes   - The x-axis values at each data point. The number of elements in
             this list should be the same as the number of data points in
             [values]. If there is no x-axis value at that point, its value
             should be None. If no axes are needed, this can be None.
             Default to None.
    """
    draw_outline(window, turtle)
    draw_grid()
    draw_data_points()


def draw_outline(window, turtle, padding_horizontal=30, padding_vertical=30):
    height = window.window_height()
    width = window.window_width()

    # Move the turtle to the top left corner of the outline
    turtle.up()
    turtle.setpos(padding_horizontal, padding_vertical)

    # Draw top left to top right
    turtle.down()
    turtle.setpos(width - padding_horizontal, padding_vertical)
    # Draw top right to bottom right
    turtle.setpos(width - padding_horizontal, height - padding_vertical)
    # Draw bottom right to bottom left
    turtle.setpos(padding_horizontal, height - padding_vertical)
    # Draw bottom left to top left
    turtle.setpos(padding_horizontal, padding_vertical)
