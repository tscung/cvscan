#!/usr/bin/env python
"""

Script to process the data from autralia postal codes

"""

import pickle
import csv
import re

pincodes = set()
district_state = {}
states = set()
address = {}

data_file = 'au_postalcodes.csv'
with open(data_file) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print row
    prev_size = len(pincodes)
    pincodes.add(row['\xef\xbb\xbfpostcode'])
    cur_size = len(pincodes)
    if cur_size != prev_size:
      state_name = row['state'].lower()
      district_name = row['name'].lower()
      sub_district_name = set()
      address[row['\xef\xbb\xbfpostcode']] = {'state': state_name, 'district':district_name}
      states.add(state_name)
      district_state[district_name] = state_name

# Store pincodes list in pincodes
with open('pincodes','wb') as fp:
  pickle.dump(pincodes,fp)

# Store address dictionaries
with open('pincode-district-state','wb') as fp:
  pickle.dump(address,fp)

# Store distric-state dictionaries
with open('district-states','wb') as fp:
  pickle.dump(district_state,fp)

# Store states list
with open('states','wb') as fp:
  pickle.dump(states,fp)
