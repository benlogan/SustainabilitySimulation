class Application:
    name = ''
    lines_of_code = 0

    cloud = False
    # % complete?
    cloud_progress = 0
    cloud_progress_rate = 0

    sci_score = 0

    servers = []
    servers_total_power = 0;

    def __str__(self):
        return 'name: ' + self.name \
               + '\nlines_of_code: ' + str(self.lines_of_code) \
               + '\ncloud: ' + str(self.cloud) \
               + '\ncloud_progress: ' + str(self.cloud_progress) + '%' \
               + '\ncloud_progress_rate: ' + str(self.cloud_progress_rate) + '' \
               + '\nsci_score: ' + str(self.sci_score) \
               + '\nserver count: ' + str(len(self.servers)) \
               + '\nserver power total: ' + str(self.servers_total_power) \
               + '\n'
