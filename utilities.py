import random

from model.applicationClass import Application
from model.serverClass import Server

def create_test_data(size):
    applist = []
    i = 1
    while i <= size:
        app = Application()

        app.name = 'Simulated App ' + str(i)

        app.lines_of_code = random.randrange(1, 1000000)

        # calculate the SCI as a function of LOC for now...
        app.sci_score = app.lines_of_code / 1000

        server_count = random.randrange(1, 100)
        server_list = []
        j = 1
        while j <= server_count:
            server_list.append(Server())
            j += 1
        app.servers = server_list;

        # print('Created an app. LOC; ', app.lines_of_code, ' SCI; ', app.sci_score, ' Server Count; ', len(app.servers))

        applist.append(app)

        i += 1
    return applist
