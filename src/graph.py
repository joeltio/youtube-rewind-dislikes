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


def draw_graph_grid(window, turtle, data_points,
                    top_left_coord, bottom_right_coord,
                    num_vertical_cells,
                    pencolor=(220, 220, 220)):
    # Set the turtle pencolor, default to gray
    original_pencolor = turtle.pencolor()
    window.colormode(255)
    turtle.pencolor(pencolor)

    # Calculate the size of each cell
    horizontal_len = bottom_right_coord[0] - top_left_coord[0]
    vertical_len = bottom_right_coord[1] - top_left_coord[1]

    num_horizontal_cells = len(data_points)

    cell_horizontal_len = horizontal_len // num_horizontal_cells
    cell_vertical_len = vertical_len // num_vertical_cells

    # Draw the vertical lines
    turtle.setheading(0)
    turtle.up()
    turtle.setpos(*top_left_coord)
    for i in range(num_horizontal_cells-1):
        # Move one cell to the right
        turtle.up()
        turtle.forward(cell_horizontal_len)
        # Turn to face into the grid
        if i % 2 == 0:
            turtle.left(90)
        else:
            turtle.right(90)

        # Draw the vertical line
        turtle.down()
        turtle.forward(vertical_len)

        # Turn back
        if i % 2 == 0:
            turtle.right(90)
        else:
            turtle.left(90)

    # Draw the horizontal lines
    turtle.up()
    turtle.setpos(*top_left_coord)
    turtle.left(90)
    for i in range(num_vertical_cells-1):
        # Move one cell down
        turtle.up()
        turtle.forward(cell_vertical_len)

        # Turn the face into the grid
        if i % 2 == 0:
            turtle.right(90)
        else:
            turtle.left(90)

        # Draw the horizontal line
        turtle.down()
        turtle.forward(horizontal_len)

        # Turn the face into the grid
        if i % 2 == 0:
            turtle.left(90)
        else:
            turtle.right(90)

    # Reset the turtle orientation
    turtle.setheading(0)

    # Reset the turtle pencolor
    turtle.pencolor(original_pencolor)

    x_axis_points = []
    for i in range(num_horizontal_cells):
        coordinate = (top_left_coord[0] + i*cell_horizontal_len,
                      bottom_right_coord[1])
        x_axis_points.append(coordinate)

    y_axis_points = []
    for i in range(num_vertical_cells+1):
        coordinate = (top_left_coord[0],
                      top_left_coord[1] + i*cell_vertical_len)
        y_axis_points.append(coordinate)

    return (x_axis_points, y_axis_points)


def draw_graph_axes(window, turtle,
                    x_axis_points, x_axis_values,
                    y_axis_points, y_scale, y_start_val):

    font = ("Arial", 12, "normal")

    # Draw the vertical axes
    turtle.up()
    for i, point in enumerate(reversed(y_axis_points)):
        turtle.setpos(*point)
        turtle.backward(5)

        # Write the value
        point_value = y_start_val + i*y_scale
        turtle.write(point_value, align="right", font=font)

    # Do not draw x axis if there is no x axis given
    if x_axis_values is None:
        return

    for i, point in enumerate(x_axis_points):
        turtle.setpos(*point)
        turtle.left(90)
        turtle.forward(15)
        turtle.setheading(0)

        # Write the value
        point_value = x_axis_values[i]
        turtle.write(point_value, align="center", font=font)


def draw_data_points(window, turtle, data_points,
                     x_axis_points, vertical_scale,
                     y_start):
    turtle.up()
    for i in range(len(x_axis_points)):
        # Calculate the y value of the point
        y_decrement = vertical_scale * (data_points[i] - y_start)

        # Draw the dot at the data point
        axis_point = x_axis_points[i]
        coordinate = (axis_point[0], axis_point[1] - y_decrement)
        turtle.setpos(*coordinate)
        turtle.dot(8)

        # Keep the turtle down to connect the dots for subsequent points
        turtle.down()


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

    # Draw the outline of the graph
    draw_rectangle(window, turtle, top_left_coord, bottom_right_coord)

    # Figure out the scale of the vertical axis
    vertical_len = bottom_right_coord[1] - top_left_coord[1]
    vertical_cell_value = int(stdev(data_points))

    data_range = max(data_points) - min(data_points)
    num_vertical_cells = ceil(data_range / vertical_cell_value)

    # Draw the graph cells
    x_axis_points, y_axis_points = draw_graph_grid(
        window, turtle, data_points,
        num_vertical_cells=num_vertical_cells,
        top_left_coord=top_left_coord,
        bottom_right_coord=bottom_right_coord)

    # Draw axes
    vertical_grid_value_range = num_vertical_cells * vertical_cell_value
    vertical_grid_value_spacing = (vertical_grid_value_range - data_range) / 2
    y_start = min(data_points) - vertical_grid_value_spacing

    draw_graph_axes(
        window, turtle,
        x_axis_points, axes,
        y_axis_points, vertical_cell_value, y_start_val=y_start)

    vertical_scale = vertical_len / vertical_grid_value_range

    draw_data_points(window, turtle, data_points,
                     x_axis_points, vertical_scale, y_start)
