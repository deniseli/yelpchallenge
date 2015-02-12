import json
import math
from matplotlib import pyplot as plt
import numpy as np
import scipy
from pprint import pprint

with open('../output/business_ratings.json') as f:
    content = f.readlines()

r_norm = []
ratings = {}
for c in content:
    json_data = json.loads(c)
    r_norm.append(json_data['norm_stars'])
    ratings[json_data['business_id']] = {}
    ratings[json_data['business_id']]['stars'] = json_data['stars']
    ratings[json_data['business_id']]['norm_stars'] = json_data['norm_stars']

r_norm = np.array(r_norm)
    
f = open('../output/adj_ratings.json', 'w')
f.write('')
f.close()
f = open('../output/adj_ratings.json', 'a')
diffs = []
for business_id in ratings.keys():
    if abs(ratings[business_id]['norm_stars'] - np.mean(r_norm)) < 3 * np.std(r_norm):
        ratings[business_id]['adj_stars'] = (4.0 * (ratings[business_id]['norm_stars'] - np.amin(r_norm)) / (np.amax(r_norm) - np.amin(r_norm))) + 1.0
        out = {'business_id': business_id, 'adj_stars': ratings[business_id]['adj_stars']}
        diffs.append(ratings[business_id]['adj_stars'] - ratings[business_id]['stars'])
        f.write(json.dumps(out) + "\n")
f.close()

diffs = np.array(diffs)
max = np.amax(diffs)
min = np.amin(diffs)

histo = np.histogram(diffs, bins=100, range=(min, max))
freqs = histo[0]
interval = (max - min) / (len(histo[1]) - 1)
newbins = np.arange(min, max, interval)

plt.title("Difference between Original Ratings and Adjusted Ratings")
plt.xlabel("adj_stars - stars")
plt.text(-1, 2000, "Mean: " + str(np.mean(diffs)) + \
         "\nMedian: " + str(np.median(diffs)) + \
         "\nStd Dev: " + str(np.std(diffs)))
r_norm_histogram = plt.bar(newbins, freqs, width=0.04, color='gray')
plt.show()
