# a strategy for gradual cloud adoption/migration
# don't realise energy savings until migration is 100% (could be improved)

# we have a target
# we have a rate of progress
# other more complicated factors we can come back to later...

# rate of progress will change per app, but this is baseline/typical
# each iteration(day) you get closer, eventually you are done

cloud_progress_rate = 0.1
# 1% a day, so after 100 days all apps would be fully migrated
# so 0.1% each day, would only equate to ~36% a year
# that's probably actually fairly realistic
# what's a sensible range?
# slow = 5 years = 0.055
# fast = 6 months= 0.55
# TODO this probably needs to be modelled per app
# but then that's different to simulation, that's making a prediction in advance!
# if we leave it to vary during simulation, then we can do that via some randomness/variability;
cloud_progress_min = .055
cloud_progress_max = .485
# .45 results in no apps migrated in the year
# .48 consistently around 40%
# .49 consistently around 60%
# .5 ~ 70%. doesn't make much sense?

# TODO incorporate randomness and variability to make for more realistic cloud progress
# TODO factor that cloud status into the carbon footprint
