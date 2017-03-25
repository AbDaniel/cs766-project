from subprocess import call

from itertools import groupby
from operator import itemgetter

global_path = '/Users/daniel/IdeaProjects/cs766-project-data/'

file_name = '/Users/daniel/IdeaProjects/cs766-project-data/vis16cat.txt'

with open('%s' % file_name) as f:
    lines = f.read().splitlines()

lines = [x.split('\t') for x in lines]

for elt, items in groupby(lines, itemgetter(0)):
    output_directory = global_path + elt
    for i in items:
        url = "wget -nc {0} -P {1} --tries=1".format(i[1], output_directory)
        call(url, shell=True)