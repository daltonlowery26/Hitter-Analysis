import pandas as pd
import numpy as np
import os
os.chdir('C:/Users/dalto/OneDrive/Pictures/Documents/Projects/Coding Projects/Biomechanics/data/full/')

pitch = pd.read_csv('pitch.csv')
print("done reading csv")

# predefined attack zones which are better then the statcast ones, need to have sztop and bottom as well as plate vert and horz in dataframe
def attack_zones(df):
    vert_bounds = [
    df['sz_top'] * 0.7744, # Lower bound for zones 1, 2, 3 # 0
    df['sz_top'] * 0.9,    # Upper bound for zones 1, 2, 3, bottom for chase
    df['sz_top'] * 0.6488, # Lower bound for zones 4, 5, 6
    df['sz_top'] * 0.7744, # Upper bound for zones 4, 5, 6 (same as lower for 1,2,3)
    df['sz_top'] * 0.5232, # Lower bound for zones 7, 8, 9, top for cgase zibe
    df['sz_top'] * 0.6488, # Upper bound for zones 7, 8, 9 (same as lower for 4,5,6)
    df['sz_top'] * 1.1, # top for chase zone,
    df['sz_top'] * .333 # bottom for chase zone 
]
    horz_bounds = [
    -6.7 / 12, #0
    -2.2333 / 12,
    2.2333 / 12,
    6.7 / 12,
    -13.3/12, #4
    -7.98/12,
    -2.66/12,
    2.66/12, #7
    7.98/12,
    13.3/12,
    0
]

# Define the conditions using vectorized comparisons on columns
    conditions = [
    (vert_bounds[0] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[1]) & (horz_bounds[0] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[1]), # Zone 1
    (vert_bounds[0] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[1]) & (horz_bounds[1] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[2]), # Zone 2
    (vert_bounds[0] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[1]) & (horz_bounds[2] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[3]), # Zone 3
    (vert_bounds[2] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[3]) & (horz_bounds[0] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[1]), # Zone 4
    (vert_bounds[2] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[3]) & (horz_bounds[1] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[2]), # Zone 5
    (vert_bounds[2] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[3]) & (horz_bounds[2] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[3]), # Zone 6
    (vert_bounds[4] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[5]) & (horz_bounds[0] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[1]), # Zone 7
    (vert_bounds[4] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[5]) & (horz_bounds[1] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[2]), # Zone 8
    (vert_bounds[4] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[5]) & (horz_bounds[2] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[3]), # Zone 9

    (vert_bounds[1] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[6]) & (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[5]), # Zone 10
    (vert_bounds[1] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[6]) & (horz_bounds[5] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[6]), # Zone 11
    (vert_bounds[1] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[6]) & (horz_bounds[6] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[7]), # Zone 12
    (vert_bounds[1] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[6]) & (horz_bounds[7] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[8]), # Zone 13
    (vert_bounds[1] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[6]) & (horz_bounds[8] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[9]), # Zone 14

    (vert_bounds[7] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[4]) & (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[5]), # Zone 15
    (vert_bounds[7] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[4]) & (horz_bounds[5] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[6]), # Zone 16
    (vert_bounds[7] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[4]) & (horz_bounds[6] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[7]), # Zone 17
    (vert_bounds[7] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[4]) & (horz_bounds[7] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[8]), # Zone 18
    (vert_bounds[7] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[4]) & (horz_bounds[8] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[9]), # Zone 19

    (vert_bounds[4] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[2]) & (horz_bounds[3] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[9]), # Zone 20
    (vert_bounds[2] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[0]) & (horz_bounds[3] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[9]), # Zone 21
    (vert_bounds[0] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[1]) & (horz_bounds[3] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[9]), # Zone 22

    (vert_bounds[4] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[2]) & (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[0]), # Zone 23
    (vert_bounds[2] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[0]) & (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[0]), # Zone 24
    (vert_bounds[0] <= df['plate_vert']) & (df['plate_vert'] <= vert_bounds[1]) & (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[0]), # Zone 25

    (df['plate_horz'] <= horz_bounds[4]) & (df['plate_vert'] <= vert_bounds[2]), # Zone 26
    (df['plate_horz'] <= horz_bounds[4]) & (df['plate_vert'] > vert_bounds[2]), # Zone 27

    (vert_bounds[6] <= df['plate_vert']) & (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[10]), #28
    (vert_bounds[6] <= df['plate_vert']) & (df['plate_horz'] >= horz_bounds[0]) & (df['plate_horz'] <= horz_bounds[9]), # Zone 29
    (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[10]) & (df['plate_vert'] <= vert_bounds[2]), # Zone 30

    (df['plate_horz'] >= horz_bounds[9]) & (df['plate_vert'] >= vert_bounds[2]), # 31
    (df['plate_horz'] >= horz_bounds[9]) & (df['plate_vert'] <= vert_bounds[2]), # 32

    (vert_bounds[7] >= df['plate_vert']) & (horz_bounds[4] <= df['plate_horz']) & (df['plate_horz'] <= horz_bounds[9]) # Zone 33

    ]
    # Define the corresponding values for each condition
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    df['nzone'] = np.select(conditions, choices, default=0)
    return df

pitch = attack_zones(pitch)
pitch.to_csv('pitch_zones.csv', index=False)