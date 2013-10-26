#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Your Team Name,Description,Goal,Member 1,Member 2,Member 3,Member 4,Member 5

import csv

with open('projects.md', 'w') as mdfile:
  with open('projects.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
      name, desc, goal, m1, m2, m3, m4, m5 = row
      mdfile.write('# %s\n' % name)
      mdfile.write('[Project Repo link](https://)  \n')
      mdfile.write('*Description:* %s  \n' % desc)
      mdfile.write('*Goal:* %s  \n' % goal)
      mdfile.write('*Members:*\n\n')
      for m in [m1, m2, m3, m4, m5]:
        m = m.strip()
        if len(m) == 0: continue
        mdfile.write('* %s (@<your github name>)\n' % m)
      mdfile.write('\n')
