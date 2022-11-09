#!/Users/ida/miniconda3/envs/langacq/bin/python

dir=$1
output_dir=$2


# draw transitive verbs
#for i in 1 3 5 7; do
  trans_cats=`ls ${dir}/*reps${i}*.trans_cats | tr '\n' ':'`
  python draw_syn_cats_graph.py ${trans_cats} ${output_dir}/trans_reps${i}_syn_6way.png #"Learned Prior for Transitive Verbs"
#done

# draw naturalistic

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

# frequent vs. infrequent

#set files = `ls ${dir}/*reps${reps}*.verb_repo -v | tr '\n' ':'`

#python get_verb_stats.py ${files} ${output_dir}/freq_infreq_reps${reps}.png

#end



# draw lexical explosion

#set files = `ls ${dir}/train_test_parses_reps7_dump__*.out -v | tr '\n' ':'`

#python eval_lexical_explosion.py $files 0.8 ${output_dir}/lex_explosion.png
#for reps in 1 3 5 7; do
#  files=`ls ${dir}/train_test_parses_hagar_reps${reps}_dump__*.out | tr '\n' ':'`
#  python eval_lexical_explosion.py $files 0.8 ${output_dir}/lex_explosion_reps${reps}.png
#done



# draw nouns vs. verbs

#for reps in 1 3 5 7; do
#  files=`ls ${dir}/train_test_parses_hagar_reps${reps}_dump__*.out | tr '\n' ':'`
#  python eval_verb_vs_noun.py $files 0.8 ${output_dir}/verbs_vs_nouns_abs${reps}.png F
#done
