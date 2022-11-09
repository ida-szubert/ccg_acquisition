#############################################
## Testing of LF parsing                   ##
##                                         ##
#############################################

import sys
from optparse import OptionParser
# from grammar_classes import *
# from lexicon_classes import *
# from parser import *
# from cat import synCat
# import cat
# from exp import *
# from correct_dependencies_with_templates import checkIfWh
# from errorFunct import error
import expFunctions
from collections import defaultdict
import pickle

noQ = False

def sem_reps_stats(input_template, file_no):
    sentences_per_session = {}
    bad_sem_per_session = {}
    complexity_per_session = {}
    length_per_session = {}
    c_distribution_per_session = {}
    l_c_per_session = {}

    for i in range(1, file_no):
        inputpairs = open(input_template.format(str(i))).readlines()
        # sent_count, bad_sem_count, freq_dict, l_c_pairs, subexp_dict = sem_reps_stats_file(inputpairs)
        sent_count, bad_sem_count, freq_dict, l_c_pairs = sem_reps_stats_file(inputpairs)
        sentences_per_session[i] = sent_count
        bad_sem_per_session[i] = bad_sem_count
        c_distribution_per_session[i] = freq_dict
        average_complexity = 1.0 * sum([k*v for k,v in freq_dict.items()]) / (sent_count-bad_sem_count)
        complexity_per_session[i] = average_complexity
        average_length = (sum([l for l,c in l_c_pairs])*1.0) / len(l_c_pairs)
        length_per_session[i] = average_length
        l_c_per_session[i] = [(l, c, i) for l,c in l_c_pairs]


    return sentences_per_session, bad_sem_per_session, complexity_per_session, \
           length_per_session, c_distribution_per_session, l_c_per_session


def sem_reps_stats_file(inputpairs):
    line_count = 0
    sentence_count = 0
    sem_not_parsable = 0
    complex_freq = defaultdict(int)
    l_c_pairs = []
    # subexp = {}

    while line_count < len(inputpairs):
        line = inputpairs[line_count]
        line_count += 1
        if line[:5] == "Sent:":
            sentence = line[6:].strip().rstrip()
            no_tokens = len(sentence.split())

        if sentence and line[:4] == "Sem:":
            semstring = line[5:].strip().rstrip()
            parsable = True

            try:
                sem, _ = expFunctions.makeExpWithArgs(semstring, {})
                if not sem:
                    sem_not_parsable += 1
                else:
                    # subexpressions = set(sem.allSubExps())
                    subexpressions = set(sem.allExtractableSubExps())
                    complex_freq[len(subexpressions)] += 1
                    l_c_pairs.append((no_tokens, len(subexpressions)))
                    # subexp[sentence] = subexpressions
            except (AttributeError, IndexError):
                print "LF could not be parsed\nSent : " + sentence
                print "Sem: " + semstring + "\n\n"
                sem_not_parsable += 1

        if sentence and line[:11] == "example_end":
                sentence_count += 1
    return sentence_count, sem_not_parsable, complex_freq, l_c_pairs
           # subexp


# def train_rules(sem_store, RuleSet, lexicon, inputpairs, output,
#                 test_out=None, dotest=False, sentence_count=0, truncate_complex_exps=True):
#     print "testout = ", test_out
#     print "put in sent coutn = ", sentence_count
#     if not sentence_count:
#         sentence_count = 0
#     datasize = 20000
#     lexicon.set_learning_rates(datasize)
#     sentence_limit = 10
#     num_reps = 0
#     line_count = 0
#     sentence = None
#     topCatList = []
#     sents_with_no_sc = []
#
#     with open("./my_test/Adam_no_sc.txt", "w") as no_sc_file:
#         while line_count < len(inputpairs):
#             line = inputpairs[line_count]
#             line_count += 1
#             if line[:5] == "Sent:":
#                 sentence = line[6:].strip().rstrip()
#                 if sentence.count(" ") > sentence_limit:
#                     print "rejecting ", line
#                     sentence = None
#                     continue
#                 topCatList = []
#
#             if sentence and line[:4] == "Sem:":
#                 semstring = line[5:].strip().rstrip()
#                 sem, expString = expFunctions.makeExpWithArgs(semstring, {})
#                 subexpressions = sem.allExtractableSubExps()
#                 if len(subexpressions) > 9 and truncate_complex_exps:
#                     print "rejecting ", sem.toString(True)
#                     for e in subexpressions:
#                         print e.toString(True)
#                     sem, expString = None, ""
#                     sentence = None
#                     continue
#                 if not sem:
#                     error("could not make exp")
#
#                 # if checkIfWh(sem):
#                 if sem.checkIfWh():
#                     isQ = False
#                     sc = synCat.swh
#                 elif sem.isQ():
#                     isQ = True
#                     sc = synCat.q
#                     # if not topCatList:
#                     #     sentisq = True
#                 else:
#                     isQ = False
#                     try:
#                         sc = synCat.allSynCats(sem.type())[0]
#                     except IndexError:
#                         sents_with_no_sc.append(("Sent: "+sentence+"\n", line))
#                         sc = None
#                         no_sc_file.write("Sent: "+sentence+"\n")
#                         no_sc_file.write(line)
#                         no_sc_file.write("example_end\n\n")
#
#                 if sc:
#                     words = sentence.split()
#                     if not isQ and words[-1] in ["?", "."]:
#                         words = words[:-1]
#                     else:
#                         print "Is Q"
#                     if len(words) == 0:
#                         words = None
#                         sentence = None
#                         sem = None
#                         sc = None
#                         continue
#
#                     print "sentence is ", sentence
#                     topCat = cat.cat(sc, sem)
#                     topCatList.append(topCat)
#
#             if sentence and line[:11] == "example_end":
#                 if sc:
#                     print '\ngot training pair'
#                     print "Sent : " + sentence
#                     print >> output, "Sent : " + sentence
#                     print >> output, "update weight = ", lexicon.get_learning_rate(sentence_count)
#                     print >> output, sentence_count
#                     for topCat in topCatList:
#                         print "Cat : " + topCat.toString()
#                         print >> output, "Cat : " + topCat.toString()
#
#                     # if len(words) > 8 or (noQ and "?" in sentence):
#                     #     sentence = []
#                     #     sem = None
#                     #     continue
#
#                     sentence_count += 1
#                     num_reps += len(sem.allExtractableSubExps())
#
#     print "returning sentence count ", sentence_count
#     return sentence_count, num_reps

###########################################
# Main.                                   #
# Try to keep to just build or check      #
###########################################

# def main(argv, opts):
#     print argv
#     build_or_check = argv[1]
#     print "build or check is ", build_or_check
#
#     if build_or_check == "i_n":  # train on months 1..i, test on the n-th
#         exp.allowTypeRaise = False
#         oneWord = True
#         numreps = 1
#         rule_alpha_top = 1.0
#         beta_tot = 1.0
#         beta_lex = 0.005
#         type_to_shell_alpha_o = 1000.0
#         shell_to_sem_alpha_o = 500.0
#         word_alpha_o = 1.0
#
#         Lexicon.set_one_word(True)
#         RuleSet = Rules(rule_alpha_top, beta_tot, beta_lex)
#         Current_Lex = Lexicon(type_to_shell_alpha_o, shell_to_sem_alpha_o, word_alpha_o)
#         RuleSet.usegamma = False
#         Current_Lex.usegamma = False
#         sem_store = SemStore()
#
#         sentence_count = 0
#         prev_sentence_count = 0
#         input_file = opts.inp_file  # "trainFiles/trainPairs"
#         inputpairs = open(input_file).readlines()
#         word_sign = "_1W" if oneWord else "_MWE"
#         rep_sign = "_{0:d}reps".format(numreps) if numreps>1 else ""
#         outfile = opts.train_parses + ''.join([word_sign, rep_sign])
#         output = open(outfile, "w")
#
#         sentence_count, num_reps_for_section = train_rules(sem_store, RuleSet, Current_Lex, inputpairs,
#                                                            output, None, False, sentence_count)
#
#         print "XXX returned sentence count = ", sentence_count
#         print "XXX prev sentence count = ", prev_sentence_count
#         print "XXX num of sub-reps per section = ", num_reps_for_section
#         print "XXX avg num of sub-reps per section = ", 1.0 * num_reps_for_section / (
#             sentence_count - prev_sentence_count)
#         prev_sentence_count = sentence_count


###########################################
# Main for LF analysis                    #
#                                         #
###########################################

def main_lf_stats(argv, opts):
    print argv
    build_or_check = argv[1]
    print "build or check is ", build_or_check

    if build_or_check == "i_n":  # train on months 1..i, test on the n-th

        sentence_counts, bad_sem_counts, complexity_counts, length_counts,\
        distibution_per_session, l_c_pairs = \
            sem_reps_stats(opts.inp_file, int(opts.last_file))

        print sentence_counts
        print bad_sem_counts
        print complexity_counts
        print length_counts

        f_dump = open("./results_analysis/Hagar_lf_stats", 'wb')
        to_pickle_obj = (sentence_counts, bad_sem_counts, complexity_counts,
                         length_counts, distibution_per_session, l_c_pairs)
        pickle.dump(to_pickle_obj, f_dump)
        f_dump.close()


def cmd_line_parser():
    """
    Returns the command line parser.
    """
    usage = "usage: %prog [options]\n"
    opt_parser = OptionParser(usage=usage)
    opt_parser.add_option("--ai", action="store", dest="alternative_input",
                          help="an alternative input file (works only with load_from_pickle)")
    opt_parser.add_option("--dl", action="store", dest="dumped_lexicon",
                          help="a dumped lexicon file (works only with load_from_pickle")
    opt_parser.add_option("--dotest", action="store_true", dest="dotest", default=False,
                          help="use this flag if you want to apply testing")
    opt_parser.add_option("-t", action="store", dest="test_parses",
                          help="the output file for the test parses")
    opt_parser.add_option("-n", action="store", dest="train_parses",
                          help="the output file for the train parses")
    opt_parser.add_option("-i", dest="inp_file", default="trainFiles/trainPairs",
                          help="the input file names (with the annotated corpus)")
    opt_parser.add_option("--devel", dest="development_mode", default=False, action="store_true",
                          help="development mode")
    opt_parser.add_option("-f", dest="last_file", default=42, action="store",
                          help="number of LF files to analyse +1")

    return opt_parser


if __name__ == '__main__':
    parser = cmd_line_parser()
    options, args = parser.parse_args(sys.argv)
    if len(args) == 1 or args[1] != 'i_n':
        print('Illegal option for now.')
        sys.exit(-1)
    # if not options.train_parses or not options.test_parses:
    #     print('Train and test parses have to be defined')
    #     sys.exit(-1)

    # main(args, options)
    main_lf_stats(args, options)
