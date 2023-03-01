# initial attempt at a basic simulation for tech sustainability in the enterprise

# let's distinguish between the 'model' and the 'simulation' aspects...

# inputs; a list of applications (objects), with associated sustainability properties
# outputs; expected emissions
# logic/rules; e.g. cloud reduces emissions by 90%
# variables; time, rate of migration, app growth/shrinkage

from utilities import *
from visualisation import *
from analysis import *
from strategies.cloud import *


def run_simulation():
    applist = create_test_data(1000)

    initial_static_analysis(applist)

    x_axis = []
    y_axis = []

    sim_iterations = 365
    i = 1
    while i <= sim_iterations:
        # calculate the daily emissions for each app (and sum)
        combined_sci_score = 0
        for app in applist:
            # assume the SCI scores drops daily by between 0 and 1 %
            # need to actually persist the new value for future iterations!
            app.sci_score = app.sci_score - (app.sci_score * (random.uniform(0, 1) / 100))
            combined_sci_score += app.sci_score

            # apply a carbon reduction strategy
            if not app.cloud:
                app.cloudProgress += cloud_progress_rate
            if app.cloudProgress == 100:
                app.cloud = True

        # print('day', i, 'combined_sci_score;', combined_sci_score)

        x_axis.append(i)
        y_axis.append(combined_sci_score)

        i += 1

    draw_line_chart(x_axis, y_axis)

    final_static_analysis(x_axis, y_axis)

    # for app in applist:
    #    print(app)
