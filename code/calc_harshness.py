import json
from pprint import pprint

print "Decoding user.json..."
with open('../data/user.json') as f:
    user_content = f.readlines()

print "Decoding business.json..."
with open('../data/business.json') as f:
    business_content = f.readlines()

print "Decoding review.json..."
with open('../data/review.json') as f:
    review_content = f.readlines()

print "Getting useful user data..."
users = {}
for c in user_content:
    json_data = json.loads(c)
    users[json_data['user_id']] = {}
    users[json_data['user_id']]['name'] = json_data['name']
    users[json_data['user_id']]['harshness'] = []

print "Getting useful business data..."
businesses = {}
for c in business_content:
    json_data = json.loads(c)
    businesses[json_data['business_id']] = {}
    businesses[json_data['business_id']]['name'] = json_data['name']
    businesses[json_data['business_id']]['stars'] = json_data['stars']

print "Getting useful review data..."
for c in review_content:
    json_data = json.loads(c)
    harshness = businesses[json_data['business_id']]['stars'] / json_data['stars']
    users[json_data['user_id']]['harshness'].append(harshness)

print "Calculating harshness and writing to out.txt..."
f = open('../output/user_harshness.json', 'w')
f.write('')
f.close()
f = open('../output/user_harshness.json', 'a')
for uid in users.keys():
    if len(users[uid]['harshness']) > 0:
        h = users[uid]['harshness']
        out = {'user_id': uid, 'harshness': sum(h) / float(len(h))}
        f.write(json.dumps(out) + "\n")
f.close()
