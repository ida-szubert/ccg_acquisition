#############################
# Generate files mapping words to their morphologically annotated form
# adj_lfs, det_lfs, noun_lfs, prep_lfs, verb_logical_forms
# print out all adverbs and auxiliaries, to paste into
#  extract_from_lexicon3.py manually
# it needs to be extracted from the connl files
# TODO what to do about participles? now in verb_lfs

# never mind, I'll just use this file to inspect pickled sem_store

import cPickle

s1 = open("adam_reps1_1_sem_store", "rb")
sem_store1 = cPickle.load(s1)
s3 = open("adam_reps1_3_sem_store", "rb")
sem_store3 = cPickle.load(s3)
print("check it out now")
