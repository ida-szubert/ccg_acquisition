#!/Users/ida/miniconda3/envs/langacq/bin/python

dir=$1
output_dir=$2
#high_res_dir=$3

# draw accuracy graphs
#acc_dist1=`ls ${dir}/train_test_parses_hagar_reps1__1W_* | tr '\n' ':'`
#acc_dist3=`ls ${dir}/train_test_parses_adam_reps3__1W_* | tr '\n' ':'`
#acc_dist5=`ls ${dir}/train_test_parses_adam_reps5__1W_* | tr '\n' ':'`
#acc_dist7=`ls ${dir}/train_test_parses_adam_reps7__1W_* | tr '\n' ':'`
#
#python eval_test_file.py ${output_dir}/acc_graphs_hagar $acc_dist1 $acc_dist3 $acc_dist5 $acc_dist7


# draw naturalistic
#
#for reps in 1 3 5 7; do
#
#for phenom in trans prep det nouns; do
#
#python draw_syn_w_given_lf_graph.py -d ${dir}/ -p ${phenom} -c reps${reps} -s out -o ${output_dir}/${phenom}_reps${reps}
#done
#
#done


# draw dax

#foreach reps (1 3 5 7 )

#set phenom = trans_dax

#python draw_syn_w_given_lf_graph.py -d ${dir}/ -p ${phenom} -c reps${reps} -s out1 -o ${output_dir}/${phenom}_reps${reps}_1_ 

#python draw_syn_w_given_lf_graph.py -d ${dir}/ -p ${phenom} -c reps${reps} -s out2 -o ${output_dir}/${phenom}_reps${reps}_2_ 

#set phenom = corp_prep

#python draw_syn_w_given_lf_graph.py -d ${dir}/ -p ${phenom} -c reps${reps} -s out3 -o ${output_dir}/${phenom}_reps${reps}_ 

#set phenom = corp_noun

#python draw_syn_w_given_lf_graph.py -d ${dir}/ -p ${phenom} -c reps${reps} -s out4 -o ${output_dir}/${phenom}_reps${reps}_

#end



# frequent vs. infrequent

#for reps in 1 3 5 7; do
#
#  files=`ls ${dir}/*reps${reps}*.verb_repo | tr '\n' ':'`
#  python get_verb_stats.py ${files} ${output_dir}/freq_infreq_reps${reps}.png
#
#done



# draw nouns vs. verbs

#foreach reps ( 1 3 5 7 )

#set files = `ls ${high_res_dir}/train_test_parses_reps${reps}_dump__*.out -v | tr '\n' ':'`

#python eval_verb_vs_noun.py $files 0.8 ${output_dir}/verbs_vs_nouns_abs${reps}.png F

#end


