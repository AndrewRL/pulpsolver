__author__ = 'andrewlaird'

import pulp
import make_data
import numpy as np

max_class_size = "Fuckelaksfjkl;l thing."
data = "Anothl;kasjf;kajsfl;kjasfkljas;lfjkucked."

print('Generating groupings...')
possible_groupings = [tuple(class_arrangement) for class_arrangement in pulp.allcombinations(range(len(data)),
                                                                                             max_class_size)]

possible_groupings = [class_arrangement for class_arrangement in possible_groupings if len(class_arrangement) >= 8]

print('Creating variables...')
groups = pulp.LpVariable.dicts('class', possible_groupings, lowBound=0, upBound=1, cat=pulp.LpInteger)

print('Initializing model...')
class_model = pulp.LpProblem("Class Assignment Model", pulp.LpMinimize)


def scoring_function(data, indices):

    age_score = np.std([data[index][1] for index in indices])
    reading_score = np.std([data[index][2] for index in indices])

    #print(age_score, reading_score)

    return int(10*age_score+10*reading_score)

print('Adding scoring function...')
#print([scoring_function(data, grouping) * groups[grouping] for grouping in possible_groupings])
class_model += pulp.lpSum([scoring_function(data, grouping) * groups[grouping] for grouping in possible_groupings])

print('Setting constraints...')
class_model += pulp.lpSum([groups[grouping] for grouping in possible_groupings]) >= 2
class_model += pulp.lpSum([groups[grouping] for grouping in possible_groupings]) <= 5

print('Constraining students...')
for student in range(len(data)):
    class_model += pulp.lpSum([groups[grouping] for grouping in possible_groupings if student in grouping]) == 1



print('Calling solver...')
class_model.solve(solver=pulp.COIN_CMD())

print(pulp.LpStatus[class_model.status])

for group in possible_groupings:
    if groups[group].value() == 1.0:
        print([data[student] for student in group])




