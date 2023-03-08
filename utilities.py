import random

# would require that I fully specify all uses, e.g. strategies.cloud.X
# import strategies.cloud
from strategies.cloud import *

from model.applicationClass import Application
from model.serverClass import Server

# what % of apps should be cloud-based?
cloud_threshold_percentage = 30


def create_test_data(test_data_size):
    applist = []
    app_iterator = 1
    while app_iterator <= test_data_size:
        app = Application()

        app.name = 'Simulated App ' + str(app_iterator)

        # between 1000 and 1m LOC
        app.lines_of_code = random.randrange(1000, 1000000)

        # calculate the SCI as a function of LOC for now...
        app.sci_score = app.lines_of_code / 1000

        # between 1 and 100 servers
        server_count = random.randrange(1, 100)
        server_list = []
        server_iterator = 1
        while server_iterator <= server_count:
            server_list.append(Server())
            server_iterator += 1
        app.servers = server_list

        # determine if cloud (random, flip a coin)
        # cloud = random.randint(0, 1)
        # if cloud == 1:
        #    app.cloud = True

        app.cloud_progress_rate = random.uniform(cloud_progress_min, cloud_progress_max)

        applist.append(app)

        app_iterator += 1

    # post processing?
    cloud_coverage = 0
    # how many cloud apps do we need - convert the % to a real number
    cloud_threshold = cloud_threshold_percentage / 100 * len(applist)
    while cloud_coverage < cloud_threshold:
        # until we have sufficient coverage
        # keep picking apps at random
        # and converting them to cloud (if they aren't already)
        random_iterator = random.randint(0, len(applist)-1)
        if not applist[random_iterator].cloud:
            applist[random_iterator].cloud = True
            applist[random_iterator].cloud_progress = 100
            cloud_coverage += 1

    return applist


# X is what percentage of Y
def percentage_of(x, y):
    return 100 / y * x
