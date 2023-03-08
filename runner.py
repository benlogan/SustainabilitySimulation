# simply run a simulation - wrapper

import sys
from main import *

show_chart = sys.argv[1]
simulation_count = int(sys.argv[2])

i = 1
while i <= simulation_count:
    print('**** SIMULATION ' + str(i) + '****' + '\n')
    run_simulation(show_chart)
    i += 1

# don't terminate - leave charts open?
# not necessary if we let matplotlib block execution
# input('Press ENTER to exit')
