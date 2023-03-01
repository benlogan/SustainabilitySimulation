class Application:
    name = ''
    lines_of_code = 0
    cloud = False
    sci_score = 0
    servers = []

    def __str__(self):
        return 'name: ' + self.name \
               + '\nlines_of_code: ' + str(self.lines_of_code) \
               + '\ncloud: ' + str(self.cloud) \
               + '\nsci_score: ' + str(self.sci_score) \
               + '\nserver count: ' + str(len(self.servers)) \
               + '\n'
