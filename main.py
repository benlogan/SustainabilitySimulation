# initial attempt at a basic simulation for tech sustainability in the enterprise

# let's distinguish between the 'model' and the 'simulation' aspects...

# inputs; a list of applications (objects), with associated sustainability properties
# outputs; expected emissions
# logic/rules; e.g. cloud reduces emissions by 90%
# variables; time, rate of migration, app growth/shrinkage
import random
import matplotlib.pyplot as plt

from applicationClass import Application


def create_test_data(size):
    appList = []
    i = 1
    while i <= size:
        app = Application()

        app.name = 'Simulated App ' + str(i)
        app.linesOfCode = random.randrange(1, 1000000)
        # calculate the SCI as a function of LOC for now...
        app.sciScore = app.linesOfCode / 1000
        # print('Created an app. LOC; ', app.linesOfCode, ' SCI; ', app.sciScore)

        appList.append(app)

        i += 1
    return appList


def static_analysis(appList):
    combinedSciScore = 0
    for a in appList:
        combinedSciScore += a.sciScore

    print(f'Combined SCI Score; {combinedSciScore}')
    averageSciScore = combinedSciScore / len(appList)
    print(f'Average SCI Score; {averageSciScore}')


def run_simulation():
    appList = create_test_data(1000)

    # some basic static analysis
    # static_analysis(appList)

    x_axis = []
    y_axis = []

    simIterations = 365
    i = 1
    while i <= simIterations:
        # calculate the daily emissions for each app (and sum)
        combinedSciScore = 0
        for a in appList:
            # assume the SCI scores drops daily by between 0 and 1 %
            # need to actually persist the new value for future iterations!
            a.sciScore = a.sciScore - (a.sciScore * (random.uniform(0, 1) / 100))
            combinedSciScore += a.sciScore
        print('day', i, 'combinedSciScore;', combinedSciScore)

        x_axis.append(i)
        y_axis.append(combinedSciScore)

        i += 1

    # draw a chart!
    plt.figure(figsize=(15, 5))
    plt.plot(x_axis, y_axis)
    plt.title('Emissions Over Time')
    plt.xlabel('Days')
    plt.ylabel('Combined SCI Score')
    plt.show()

    # final static analysis...

    totalDifferential = y_axis[0] - y_axis[364]
    percentageDifferential = (totalDifferential / y_axis[0]) * 100
    print('totalDifferential;', totalDifferential)
    print('percentageDifferential;', round(percentageDifferential, 2), '%')


run_simulation()
