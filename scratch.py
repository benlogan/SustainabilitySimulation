# simple test file for quick/dirty tests - nothing worth keeping
from utilities import *
from analysis import *

results = create_test_data(100)

# print(vars(results[9]))
# print(results[9])

for result in results:
    print(result)

initial_static_analysis(results)