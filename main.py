# initial attempt at a basic simulation for tech sustainability in the enterprise

# let's distinguish between the 'model' and the 'simulation' aspects...

# inputs; a list of applications (objects), with associated sustainability properties
# outputs; expected emissions
# logic/rules; e.g. cloud reduces emissions by 90%
# variables; time, rate of migration, app growth/shrinkage
import random

from utilities import *
from visualisation import *


# some very basic static analysis
def static_analysis(applist):
    combined_sci_score = 0
    for a in appList:
        combined_sci_score += a.sciScore

    print(f'Combined SCI Score; {combined_sci_score}')
    average_sci_score = combined_sci_score / len(applist)
    print(f'Average SCI Score; {average_sci_score}')


# final static analysis, using the chart data
def final_static_analysis(x_axis, y_axis):
    total_differential = y_axis[0] - y_axis[len(x_axis) - 1]
    percentage_differential = (total_differential / y_axis[0]) * 100
    print('total_differential;', total_differential)
    print('percentage_differential;', round(percentage_differential, 2), '%')


def run_simulation():
    applist = create_test_data(1000)
    # static_analysis(appList)

    x_axis = []
    y_axis = []

    sim_iterations = 365
    i = 1
    while i <= sim_iterations:
        # calculate the daily emissions for each app (and sum)
        combined_sci_score = 0
        for a in applist:
            # assume the SCI scores drops daily by between 0 and 1 %
            # need to actually persist the new value for future iterations!
            a.sciScore = a.sciScore - (a.sciScore * (random.uniform(0, 1) / 100))
            combined_sci_score += a.sciScore
        # print('day', i, 'combined_sci_score;', combined_sci_score)

        x_axis.append(i)
        y_axis.append(combined_sci_score)

        i += 1

    draw_line_chart(x_axis, y_axis)

    final_static_analysis(x_axis, y_axis)
