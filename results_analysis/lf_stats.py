# Analysis of the LF annotation of the corpora
# how complex are the LF in term of number of subexpressions?
# what's the longitudinal dynamics of semantic complexity in CDS?

import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats

# sns.set()
sns.set_style("white")

eve_pickle = open("Eve_lf_stats", 'rb')
e_sentence_counts, e_bad_sem_counts, e_complexity_counts, e_length_counts, e_distibution_per_session, e_l_c_pairs = pickle.load(eve_pickle)

adam_pickle = open("Adam_lf_stats", 'rb')
# a_sentence_counts, a_bad_sem_counts, a_complexity_counts, a_length_counts, a_distibution_per_session, a_l_c_pairs = pickle.load(adam_pickle)
a_sentence_counts, a_bad_sem_counts, a_complexity_counts, a_length_counts, a_distibution_per_session, a_l_c_pairs = pickle.load(adam_pickle)
a_days = [0, 14, 29, 41, 56, 68, 89, 103, 117, 130, 147, 162, 180, 194, 208, 222, 236, 249, 264, 282, 296, 310, 327, 340, 352, 365, 379, 392, 409, 422, 436, 450, 460, 488, 512, 525, 537, 557, 586, 602, 615]

hagar_pickle = open("Hagar_lf_stats", 'rb')
# h_sentence_counts, h_bad_sem_counts, h_complexity_counts, h_length_counts, h_distibution_per_session, h_l_c_pairs = pickle.load(hagar_pickle)
h_sentence_counts, h_bad_sem_counts, h_complexity_counts, h_length_counts, h_distibution_per_session, h_l_c_pairs = pickle.load(hagar_pickle)
h_days = [0, 0, 0, 1, 1, 12, 15, 20, 22, 29, 32, 35, 37, 37, 38, 40, 41, 41, 58, 61, 64, 64, 65, 66, 76, 79, 79, 80, 81, 89, 89, 91, 91, 92, 98, 102, 102, 102, 103, 103, 104, 105, 106, 109, 110, 110, 113, 119, 120, 121, 124, 125, 127, 134, 136, 138, 140, 140, 145, 155, 156, 163, 164, 188, 191, 192, 192, 195, 196, 197, 202, 203, 205, 206, 206, 207, 211, 211, 213, 217, 225, 226, 232, 233, 235, 237, 238, 239, 255, 258, 259, 267, 272, 274, 275, 277, 278, 279, 287, 288, 292, 293, 297, 298, 301, 304, 308, 326, 342, 344, 353, 354, 357, 364, 370, 371, 379, 385, 387, 396, 400, 403, 405, 408, 413, 420, 424, 427, 450, 453, 454, 494, 496, 501]

###########################################
# plot average complexity longitudinally  #
#                                         #
###########################################

# Eve
eve_days = [0, 15, 30, 45, 60, 90, 100, 110, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285]
e_days = [d+30 for d in eve_days]

# plt.scatter(x=e_days, y=e_complexity_counts.values())
# plt.xticks(eve_days)
# plt.xlim(0,870)
# plt.ylim(3, 9)
# plt.show()
e_average_complexity = sum([v*e_sentence_counts[k] for k,v in e_complexity_counts.items()]) / sum(e_sentence_counts.values())
print e_average_complexity


# Adam
# adam_days = [0, 14, 29, 41, 56, 68, 89, 103, 117, 130, 147, 162, 180, 194, 208, 222, 236, 249, 264, 282, 296, 310, 327, 340, 352, 365, 379, 392, 409, 422, 436, 450, 460, 488, 512, 525, 537, 557, 586, 602, 615]
# a_days = [d+247 for d in adam_days]

# plt.scatter(x=a_days, y=a_complexity_counts.values(), c="orange")
# plt.xticks(a_days)
# plt.xlim(0,870)
# plt.ylim(3, 9)
# plt.show()
a_average_complexity = sum([v*a_sentence_counts[k] for k,v in a_complexity_counts.items()]) / sum(a_sentence_counts.values())
print a_average_complexity

# Hagar
# h_days = [0, 1, 12, 15, 20, 22, 29, 32, 35, 37, 38, 40, 41, 58, 61, 64, 65, 66, 76, 79, 80, 81, 89, 91, 92, 98, 102, 103, 104, 105, 106, 109, 110, 113, 119, 120, 121, 124, 125, 127, 134, 136, 138, 140, 145, 155, 156, 163, 164, 188, 191, 192, 195, 196, 197, 202, 203, 205, 206, 207, 211, 213, 217, 225, 226, 232, 233, 235, 237, 238, 239, 255, 258, 259, 267, 272, 274, 275, 277, 278, 279, 287, 288, 292, 293, 297, 298, 301, 304, 308, 326, 342, 344, 353, 354, 357, 364, 370, 371, 379, 385, 387, 396, 400, 403, 405, 408, 413, 420, 424, 427, 450, 453, 454, 494]

# plt.scatter(x=h_days, y=h_complexity_counts.values()[:115], c="green")
# plt.xticks(h_days)
# plt.xlim(0,870)
# plt.ylim(3, 9)
# plt.show()
h_average_complexity = sum([v*h_sentence_counts[k] for k,v in h_complexity_counts.items()]) / sum(h_sentence_counts.values())
print h_average_complexity


# plt.scatter(x=e_days, y=e_complexity_counts.values(), c="tab:blue", label="Eve")
# plt.scatter(x=a_days, y=a_complexity_counts.values(), c="tab:green", label="Adam")
# plt.scatter(x=h_days, y=h_complexity_counts.values()[:115], c="darkorange", label="Hagar")
# plt.xlim(-10,870)
# plt.ylim(3, 9)
# plt.legend(loc="upper right")
# plt.title("Semantic complexity of CDS")
# plt.xlabel("child's age")
# plt.ylabel("avg no subexpressions in an utterance")
# plt.grid()
# plt.show()
# plt.savefig('./graphs/lf_complexity.png')


# plt.plot(e_days, e_complexity_counts.values(), c="tab:blue", label="Eve")
# plt.plot(a_days, a_complexity_counts.values(), c="tab:green", label="Adam")
# plt.plot(h_days, h_complexity_counts.values()[:115], c="darkorange", label="Hagar")
# plt.xlim(-10,870)
# plt.ylim(3, 12)
# # plt.legend(loc="upper right")
# plt.title("Semantic complexity of CDS")
# plt.xlabel("child's age")
# plt.ylabel("avg no subexpressions in an utterance")
# # plt.show()
# plt.savefig('./graphs/lf_complexity_line.png')


#############################################
# plot complexity distribution over session #
#                                           #
#############################################

# Eve

# # max_e = 1
# for session, complexity_dist in e_distibution_per_session.items():
#     total = sum(complexity_dist.values())
#     dist_norm = {k: float(v)/total for k,v in complexity_dist.items()}
#     # max_k = max(dist_norm.keys())
#     # if max_k > max_e:
#     #     max_e = max_k
#     plt.bar(list(dist_norm.keys()), dist_norm.values(), color='tab:blue')
#     plt.xticks(dist_norm.keys())
#     plt.ylim(0, 0.3)
#     plt.xlim(0, 10)
#     plt.title("Eve: LF complexity session {}".format(str(session)))
#     plt.savefig('./graphs/lf_complexity/Eve_{}.png'.format(str(session)))
#     plt.clf()
#
# # print max_e

# Adam

# # max_a = 1
# for session, complexity_dist in a_distibution_per_session.items():
#     total = sum(complexity_dist.values())
#     dist_norm = {k: float(v)/total for k,v in complexity_dist.items()}
#     # max_k = max(dist_norm.keys())
#     # if max_k > max_a:
#     #     max_a = max_k
#     plt.bar(list(dist_norm.keys()), dist_norm.values(), color='tab:green')
#     plt.xticks(dist_norm.keys())
#     plt.ylim(0, 0.25)
#     plt.xlim(0, 32)
#     plt.title("Adam: LF complexity session {}".format(str(session)))
#     plt.savefig('./graphs/lf_complexity/Adam_{}.png'.format(str(session)))
#     plt.clf()
#
# # print max_a

# Hagar

# # max_h = 1
# for session, complexity_dist in h_distibution_per_session.items():
#     total = sum(complexity_dist.values())
#     dist_norm = {k: float(v)/total for k,v in complexity_dist.items()}
#     # max_k = max(dist_norm.keys())
#     # if max_k > max_h:
#     #     max_h = max_k
#     plt.bar(list(dist_norm.keys()), dist_norm.values(), color='darkorange')
#     plt.xticks(dist_norm.keys())
#     plt.ylim(0, 0.5)
#     plt.xlim(0, 32)
#     # should be 48 but that's such an annoying outlier
#     plt.title("Hagar: LF complexity session {}".format(str(session)))
#     plt.savefig('./graphs/lf_complexity/Hagar_{}.png'.format(str(session)))
#     plt.clf()
#
# # print max_h


###########################################
# plot average length longitudinally      #
#                                         #
###########################################

# plt.scatter(x=e_days, y=e_length_counts.values(), c="tab:blue", label="Eve")
# plt.scatter(x=a_days, y=a_length_counts.values(), c="tab:green", label="Adam")
# plt.scatter(x=h_days, y=h_length_counts.values()[:115], c="darkorange", label="Hagar")
# # plt.xlim(-10,870)
# # plt.ylim(3, 9)
# plt.legend(loc="upper right")
# plt.title("Utterance length of CDS")
# plt.xlabel("child's age")
# plt.ylabel("avg no tokens in an utterance")
# plt.grid()
# # plt.show()
# plt.savefig('./graphs/sentence_length.png')
# plt.clf()


###########################################
# plot length vs complexity               #
#                                         #
###########################################

# Eve
e_all_pairs = []
for session, pairs in e_l_c_pairs.items():
    e_all_pairs.extend(pairs)
e_complexities = [c for l,c in e_all_pairs]
e_lengths = [l for l,c in e_all_pairs]

# plt.scatter(x=e_lengths, y=e_complexities, c="tab:blue", alpha=0.1)
# plt.show()

# # put the data into a pandas df
e_df = pd.DataFrame(dict(length = e_lengths,
                         complexity = e_complexities))
# sns.stripplot(data=e_df, x="length", y="complexity", jitter=0.3, size=2, color="tab:blue")
# plt.show()

sns.regplot(data=e_df, x="length", y="complexity", fit_reg = True, color="tab:blue",
           x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
plt.show()
# plt.savefig('./graphs/lf_complexity/complexity_length_Eve.png')
# plt.clf()


# Adam
a_complexities = []
a_lengths = []
a_age = []
for session_no, l_c in a_l_c_pairs.items():
    a_complexities.extend([x[1] for x in l_c])
    a_lengths.extend([x[0] for x in l_c])
    a_age.extend([a_days[session_no-1]]*len(l_c))

# a_all_pairs = []
# for session, pairs in a_l_c_pairs.items():
#     a_all_pairs.extend(pairs)
# a_complexities = [c for l,c in a_all_pairs]
# a_lengths = [l for l,c in a_all_pairs]


# plt.scatter(x=a_lengths, y=a_complexities, c="tab:green", alpha=0.1)
# plt.show()

# # put the data into a pandas df
a_df = pd.DataFrame(dict(length = a_lengths,
                         complexity = a_complexities,
                         age = a_age))
# sns.stripplot(data=a_df, x="length", y="complexity", jitter=0.3, size=2, color="tab:green")
# plt.show()

# # plot complexity vs length on utterance level
# sns.regplot(data=a_df, x="length", y="complexity", fit_reg = True, color="tab:green",
#            x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
# plt.show()
# # plt.savefig('./graphs/lf_complexity/complexity_length_Adam.png')
# plt.clf()

# plot complexity vs age on utterance level
sns.regplot(data=a_df, x="age", y="complexity", fit_reg = True, color="tab:green",
           x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
plt.show()
# plt.savefig('./graphs/lf_complexity/complexity_age_Adam.png')
plt.clf()

#########
# Hagar #
#########
h_complexities = []
h_lengths = []
h_age = []
for session_no, l_c in h_l_c_pairs.items():
    h_complexities.extend([x[1] for x in l_c])
    h_lengths.extend([x[0] for x in l_c])
    h_age.extend([h_days[session_no-1]]*len(l_c))

# h_all_pairs = []
# for session, pairs in h_l_c_pairs.items():
#     h_all_pairs.extend(pairs)
# h_complexities = [c for l,c in h_all_pairs]
# h_lengths = [l for l,c in h_all_pairs]

# plt.scatter(x=h_lengths, y=h_complexities, c="darkorange", alpha=0.1)
# plt.show()

# # put the data into a pandas df
h_df = pd.DataFrame(dict(length = h_lengths,
                         complexity = h_complexities,
                         age = h_age))
# sns.stripplot(data=h_df, x="length", y="complexity", jitter=0.3, size=2, color="darkorange")
# plt.show()

# # plot complexity vs length on utterance level
# sns.regplot(data=h_df, x="length", y="complexity", fit_reg = True, color="darkorange",
#            x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
# plt.show()
# # plt.savefig('./graphs/lf_complexity/complexity_length_Hagar.png')
# plt.clf()

# plot complexity vs length on utterance level
sns.regplot(data=h_df, x="age", y="complexity", fit_reg = True, color="darkorange",
           x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
plt.show()
# plt.savefig('./graphs/lf_complexity/complexity_age_Hagar.png')
plt.clf()

all_lengths = [l for l in e_lengths]
all_lengths.extend(a_lengths)
all_lengths.extend(h_lengths)

all_complexities = [l for l in e_complexities]
all_complexities.extend(a_complexities)
all_complexities.extend(h_complexities)

# names = ["Eve"]*len(e_lengths) + ["Adam"]*len(a_lengths) + ["Hagar"]*len(h_lengths)
# all_df = pd.DataFrame(dict(length = all_lengths,
#                          complexity = all_complexities,
#                          names = names))

# # sns.regplot(data=all_df, x="length", y="complexity", fit_reg = False, hue="names",
# #            x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
# sns.regplot(data=e_df, x="length", y="complexity", fit_reg = False, color="tab:blue",
#            x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
# sns.regplot(data=a_df, x="length", y="complexity", fit_reg = False, color="tab:green",
#            x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
# sns.regplot(data=h_df, x="length", y="complexity", fit_reg = False, color="darkorange",
#            x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 0.2})
# plt.show()

#############################################
# time series analysis                      #
#    are the distributions shifting?        #
#############################################


#############################################
# just correlation                          #
#                                           #
#############################################

# print scipy.stats.pearsonr(e_complexities, e_lengths)
print "Adam complexity length correlation (utterance level): "
print scipy.stats.pearsonr(a_complexities, a_lengths)
print "Adam complexity age correlation (uttearnce level): "
print scipy.stats.pearsonr(a_complexities, a_age)
print "Adam complexity length correlation (session level): "
print scipy.stats.pearsonr(a_complexity_counts.values(), a_length_counts.values())
print "Adam complexity age correlation (session level): "
print scipy.stats.pearsonr(a_complexity_counts.values(), a_days)
print "\n\n"
print "Hagar complexity length correlation (utterance level): "
print scipy.stats.pearsonr(h_complexities, h_lengths)
print "Hagar complexity age correlation (utterance level): "
print scipy.stats.pearsonr(h_complexities, h_age)
print "Hagar complexity length correlation (session level): "
print scipy.stats.pearsonr(h_complexity_counts.values(), h_length_counts.values())
print "Hagar complexity age correlation (session level): "
print scipy.stats.pearsonr(h_complexity_counts.values(), h_days)
# print scipy.stats.pearsonr(all_complexities, all_lengths)




