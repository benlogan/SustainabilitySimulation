import matplotlib.pyplot as plt


def draw_line_chart(title, x_label, y_label, x_axis, y_axis):
    plt.figure(figsize=(15, 5), num=title)
    plt.plot(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
