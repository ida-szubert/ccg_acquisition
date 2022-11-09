# this is a simple script to introduce noise by pairing the current
# sentence with the adjacent ones.

#infile = raw_input("where are the pairs?\n")
#numreps = int(raw_input("what is the window size?\n"))
infile = "trainFiles/trainPairs.adam.ready"

for distractors in [3,5,7]:
    for session_no in range(1,42):

        sents = []
        sems = []

        for line in open(infile+"_"+str(session_no)):
            line = line.strip().rstrip()
            if line[:5]=="Sent:": sents.append(line)
            if line[:4]=="Sem:": sems.append(line)

        output = open(infile+str(distractors)+"reps_"+str(session_no), "w")
        i=0
        for sent in sents:
            print >> output, sent
            for j in range(distractors):
                index=(i-int(distractors/2)+j)%len(sems)
                print >> output,sems[index]
            i+=1
            print >> output,"example_end\n"
    
