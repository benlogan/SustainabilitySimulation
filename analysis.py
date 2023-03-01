# some very basic static analysis
def initial_static_analysis(applist):
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

    count_cloud = 0
    for app in applist:
        if app.cloud:
            count_cloud += 1
    print(f'Cloud Apps; {count_cloud}. As a percentage? {(100/len(applist)*count_cloud)}%')


# final static analysis, using the chart data
def final_static_analysis(x_axis, y_axis):
    total_differential = y_axis[0] - y_axis[len(x_axis) - 1]
    percentage_differential = (total_differential / y_axis[0]) * 100
    print('total_differential;', total_differential)
    print('percentage_differential;', round(percentage_differential, 2), '%')
