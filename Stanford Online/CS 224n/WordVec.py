# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:09:56 2020

@author: MRUTYUNJAY BISWAL
"""

from nltk.corpus import wordnet as wn

poses = {'n': 'noun', 'v': 'verb', 's': 'adj(s)', 'a': 'adj', 'r': 'adv'}

for synset in wn.synsets("good"):
    print("{} : {}".format(poses[synset.pos()], ",".join([l.name() for l in synset.lemmas()])))
