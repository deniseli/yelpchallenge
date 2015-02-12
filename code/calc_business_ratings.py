import json
import scipy

print "Reading json files..."
with open('../output/user_harshness.json') as f:
    harshness_content = f.readlines()
with open('../data/business.json') as f:
    business_content = f.readlines()
with open('../data/review.json') as f:
    review_content = f.readlines()

print "Decoding user_harshness.json..."
harshnesses = {}
for c in harshness_content:
    json_data = json.loads(c)
    harshnesses[json_data['user_id']] = json_data['harshness']

print "Decoding business.json..."
businesses = {}
for c in business_content:
    json_data = json.loads(c)
    businesses[json_data['business_id']] = json_data['stars']

print "Decoding review.json..."
ratings = {}
for c in review_content:
    json_data = json.loads(c)
    if json_data['business_id'] not in ratings.keys():
        ratings[json_data['business_id']] = []
    ratings[json_data['business_id']].append(harshnesses[json_data['user_id']] * json_data['stars'])

print "Writing to output file..."
f = open('../output/business_ratings.json', 'w')
f.write('')
f.close()
f = open('../output/business_ratings.json', 'a')
for business_id in ratings.keys():
    out = {'business_id': business_id, \
               'stars': businesses[business_id], \
               'norm_stars': scipy.mean(ratings[business_id])}
    f.write(json.dumps(out) + "\n")
f.close()
