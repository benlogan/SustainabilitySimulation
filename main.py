# initial attempt at a basic simulation for tech sustainability in the enterprise

# let's distinguish between the 'model' and the 'simulation' aspects...

# inputs; a list of applications (objects), with associated sustainability properties
# outputs; expected emissions
# logic/rules; e.g. cloud reduces emissions by 90%
# variables; time, rate of migration, app growth/shrinkage

from analysis import *
from strategies.cloud import *
from visualisation import *

YEARS_1 = 365
YEARS_5 = YEARS_1 * 5

TEST_APP_COUNT = 1000


def run_simulation(show_chart):
    applist = create_test_data(TEST_APP_COUNT)

    initial_static_analysis(applist)

    x_axis = []
    y_axis = []

    # 1 iteration of the simulator = 1 day
    sim_iterations = YEARS_1

    i = 1
    while i <= sim_iterations:
        # calculate the daily emissions for each app (and sum)
        combined_sci_score = 0
        cumulative_cloud_progress = 0
        for app in applist:
            # assume the SCI scores drops daily by between 0 and 1 %
            # need to actually persist the new value for future iterations!
            app.sci_score = app.sci_score - (app.sci_score * (random.uniform(0, 1) / 100))
            combined_sci_score += app.sci_score

            # apply a carbon reduction strategy
            if not app.cloud:
                # app.cloud_progress += cloud_progress_rate
                app.cloud_progress += random.uniform(cloud_progress_min, cloud_progress_max)
            if app.cloud_progress >= 100:
                app.cloud = True
                app.cloud_progress = 100
                cumulative_cloud_progress += 1

        # print('day', i, 'combined_sci_score;', combined_sci_score)

        x_axis.append(i)
        #y_axis.append(combined_sci_score)
        y_axis.append(cumulative_cloud_progress)

        i += 1

    if show_chart == 'chart=t':
        draw_line_chart(x_axis, y_axis)

    chart_analysis(x_axis, y_axis)

    final_static_analysis(applist)
