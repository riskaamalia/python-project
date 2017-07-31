# learning data analysis from O'reilly book

# open file

path = '/home/riskaamalia/Documents/fromGit/my-git/python-project/sample-data/bitly-data.txt'
open(path).readline()

# example of read file per line
# import sys
# i=0
# for line in open(path) :
#     print(line)
#     i = i + 1
#     if (i == 2) :
#         sys.exit()

# read file from json
import json

records = [json.loads(line) for line in open(path)]
print(records[0]['tz'])
# get only tz (timezone) and get if in each record there is 'tz' key
# and rec['tz'] it means not empty string
time_zones = [rec['tz'] for rec in records if 'tz' in rec and rec['tz']]
# example just want to see first 10
print(time_zones[:10])

# method for count total timezone datas
from collections import defaultdict

def get_counts(sequence):
 counts = defaultdict(int) # values will initialize to 0

 for x in sequence:
    counts[x] += 1

 return counts

# count for each timezone and store in to variable
counts = get_counts(time_zones)
# example for print specific timezone
print(counts['America/New_York'])
# example print total of timezones
print(len(time_zones))

# count for top 10
def top_counts(count_dict, n=10):
 value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
 value_key_pairs.sort()
 return value_key_pairs[-n:]

print(top_counts(counts))

# count for top 10 using collections
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))
