import matplotlib.pyplot as plt


def draw_line_chart(x_axis, y_axis):
    plt.figure(figsize=(15, 5))
    plt.plot(x_axis, y_axis)
    plt.title('Emissions Over Time')
    plt.xlabel('Days')
    plt.ylabel('Combined SCI Score')
    plt.show()
