# -*- coding: utf-8 -*-
text = "X-DSPAM-Confidence:    0.8475"
i = text.find(" ")
print(float(text[i:]))