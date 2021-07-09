"""Compute the word frequency in given message"""

input_string=str(input())
word_freq={}
for i in input_string:
    if i in word_freq.keys():
        word_freq[i]+=1
    else:
        word_freq[i]=1
for key,value in word_freq.items():
    print("{} repeats {} times".format(key,value))