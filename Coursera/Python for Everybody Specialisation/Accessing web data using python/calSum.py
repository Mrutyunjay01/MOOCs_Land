# -*- coding: utf-8 -*-
import re

print(sum([int(k) for k in re.findall('[0-9]+', open('regex_sum_42.txt').read())]))
print(sum([int(k) for k in re.findall('[0-9]+', open('regex_sum_379562.txt').read())]))
