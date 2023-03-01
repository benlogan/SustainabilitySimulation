import random

from applicationClass import Application


def create_test_data(size):
    applist = []
    i = 1
    while i <= size:
        app = Application()

        app.name = 'Simulated App ' + str(i)
        app.linesOfCode = random.randrange(1, 1000000)
        # calculate the SCI as a function of LOC for now...
        app.sciScore = app.linesOfCode / 1000
        # print('Created an app. LOC; ', app.linesOfCode, ' SCI; ', app.sciScore)

        applist.append(app)

        i += 1
    return applist
