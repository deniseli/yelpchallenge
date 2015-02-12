import json
import math
from matplotlib import pyplot as plt
import numpy as np
import scipy
from pprint import pprint

with open('../output/user_harshness.json') as f:
    content = f.readlines()

h = []
log_h = []
for c in content:
    json_data = json.loads(c)
    h.append(json_data['harshness'])
    log_h.append(math.log(json_data['harshness'], 5))

h = np.array(h)
log_h = np.array(log_h)

h_max = 5.0
h_min = 0.2
log_h_max = 1.0
log_h_min = -1.0

h_histo = np.histogram(h, bins=100, range=(h_min, h_max))
log_h_histo = np.histogram(log_h, bins=100, range=(log_h_min, log_h_max))

h_freqs = h_histo[0]
log_h_freqs = log_h_histo[0]

h_interval = (h_max - h_min) / (len(h_histo[1]) - 1)
log_h_interval = (log_h_max - log_h_min) / (len(log_h_histo[1]) - 1)

h_newbins = np.arange(h_min, h_max, h_interval)
log_h_newbins = np.arange(log_h_min, log_h_max, log_h_interval)

#plt.title("Raw Harshness Scores")
#plt.xlabel("h")
#plt.text(3, 40000, "Mean: " + str(np.mean(h)) + \
#         "\nMedian: " + str(np.median(h)) + \
#         "\nStd Dev: " + str(np.std(h)))
#h_histogram = plt.bar(h_newbins, h_freqs, width=0.048, color='gray')
plt.title("Log Harshness Scores")
plt.xlabel("log(h)")
plt.xticks(np.arange(log_h_min, log_h_max+0.02, 0.25))
plt.text(0.25, 35000, "Mean: " + str(np.mean(log_h)) + \
         "\nMedian: " + str(np.median(log_h)) + \
         "\nStd Dev: " + str(np.std(log_h)))
log_h_histogram = plt.bar(log_h_newbins, log_h_freqs, width=0.02, color='gray')
plt.show()
