import json
import math
from matplotlib import pyplot as plt
import numpy as np
import scipy
from pprint import pprint

with open('../output/business_ratings.json') as f:
    content = f.readlines()

r_u = []
r_norm = []
for c in content:
    json_data = json.loads(c)
    r_u.append(json_data['stars'])
    r_norm.append(json_data['norm_stars'])

r_u = np.array(r_u)
r_norm = np.array(r_norm)

r_norm = r_norm[abs(r_norm - np.mean(r_norm)) < 3 * np.std(r_norm)]
r_norm = (4.0 * (r_norm - np.amin(r_norm)) / (np.amax(r_norm) - np.amin(r_norm))) + 1.0

r_u_max = 5.0
r_u_min = 1.0
#r_norm_max = np.amax(r_norm)
r_norm_max = 5.0
r_norm_min = 0.0

r_u_histo = np.histogram(r_u, bins=100, range=(r_u_min, r_u_max))
r_norm_histo = np.histogram(r_norm, bins=100, range=(r_norm_min, r_norm_max))

r_u_freqs = r_u_histo[0]
r_norm_freqs = r_norm_histo[0]

r_u_interval = (r_u_max - r_u_min) / (len(r_u_histo[1]) - 1)
r_norm_interval = (r_norm_max - r_norm_min) / (len(r_norm_histo[1]) - 1)

r_u_newbins = np.arange(r_u_min, r_u_max, r_u_interval)
r_norm_newbins = np.arange(r_norm_min, r_norm_max, r_norm_interval)

#plt.title("Original Business Ratings")
#plt.xlabel("Rating")
#plt.text(1.5, 11000, "Mean: " + str(np.mean(r_u)) + \
#         "\nMedian: " + str(np.median(r_u)) + \
#         "\nStd Dev: " + str(np.std(r_u)))
#r_u_histogram = plt.bar(r_u_newbins, r_u_freqs, width=0.4, color='gray')
#plt.title("Normalized Business Ratings")
plt.xlabel("Ratings of Business Normalized by Harshness")
#plt.xticks(np.arange(r_norm_min, r_norm_max+0.14, 1.0))
#plt.text(8, 3000, "Mean: " + str(np.mean(r_norm)) + \
#         "\nMedian: " + str(np.median(r_norm)) + \
#         "\nStd Dev: " + str(np.std(r_norm)))
#r_norm_histogram = plt.bar(r_norm_newbins, r_norm_freqs, width=0.14, color='gray')
plt.title("Normalized Business Ratings Adjusted for Range")
plt.xticks(np.arange(r_norm_min, r_norm_max+0.05, 1.0))
plt.text(3.5, 2000, "Mean: " + str(np.mean(r_norm)) + \
         "\nMedian: " + str(np.median(r_norm)) + \
         "\nStd Dev: " + str(np.std(r_norm)))
r_norm_histogram = plt.bar(r_norm_newbins, r_norm_freqs, width=0.05, color='gray')
plt.show()
