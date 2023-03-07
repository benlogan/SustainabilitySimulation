from utilities import *


# some very basic static analysis
def initial_static_analysis(applist):
    print('----initial_static_analysis start----')
    combined_sci_score = 0
    for a in applist:
        combined_sci_score += a.sci_score

    print(f'Combined SCI Score; {combined_sci_score}')

    average_sci_score = combined_sci_score / len(applist)
    print(f'Average SCI Score; {average_sci_score}')

    combined_power = 0
    for app in applist:
        for server in app.servers:
            combined_power += server.max_power_consumption
    print(f'Total Power; {combined_power}W')

    cloud_analysis(applist)

    print('----initial_static_analysis end----')


# chart data analysis
def chart_analysis(x_axis, y_axis):
    print('----chart_analysis start----')
    total_differential = y_axis[0] - y_axis[len(x_axis) - 1]
    percentage_differential = (total_differential / y_axis[0]) * 100
    print('total_differential;', total_differential)
    print('percentage_differential;', round(percentage_differential, 2), '%')
    print('----chart_analysis end----')


# final static analysis, using the chart data
def final_static_analysis(applist):
    print('----final_static_analysis start----')
    cloud_analysis(applist)
    # for app in applist:
    #    print(app)
    print('----final_static_analysis end----')


def cloud_analysis(applist):
    count_cloud = cloud_count(applist)
    print(f'Cloud Apps; {count_cloud}. As a percentage? {percentage_of(count_cloud, len(applist))}%')


def cloud_count(applist):
    # worst vampire name ever!
    count_cloud = 0
    for app in applist:
        if app.cloud:
            count_cloud += 1
    return count_cloud
