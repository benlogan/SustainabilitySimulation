import matplotlib.pyplot as plt


# retired - moved to subplots and grids
def draw_line_chart(title, x_label, y_label, x_axis, y_axis):
    plt.figure(figsize=(15, 5), num=title)
    plt.plot(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def draw_charts(cloud_x_axis, cloud_y_axis, footprint_x_axis, footprint_y_axis):
    # note that if you only use 1 column, you don't need 2 dimensional arrays
    figure, axis = plt.subplots(2, 1, figsize=(15, 10), num='Sustainability Simulation Charts')

    draw_chart(axis[0], 'Cloud Progress', cloud_x_axis, cloud_y_axis, 'Days', 'App Count')
    draw_chart(axis[1], 'Emissions Over Time', footprint_x_axis, footprint_y_axis, 'Days', 'Total Power Usage(W)')

    plt.show()


def draw_chart(array_item, title, x_axis, y_axis, x_label, y_label):
    array_item.plot(x_axis, y_axis)
    array_item.set_title(title)
    array_item.set_xlabel(x_label)
    array_item.set_ylabel(y_label)
