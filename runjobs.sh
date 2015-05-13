#!/bin/bash


i=1
imax=50

output_dir="/scratch/anlevin/data/lhe/13_tev/qed_4_qcd_0_ls_lm_lt_v9/"
#output_dir="/scratch/anlevin/data/lhe/14_tev/qed_4_qcd_0_ls_lm_lt_v4/"
#output_dir="/scratch/anlevin/data/lhe/13_tev/wpwm_qed_4_qcd_99_ls_lm_lt_v1/"
#output_dir="/scratch/anlevin/data/lhe/qed_4_qcd_99_ls_lm_lt_v8/"

gen_command1="'generate p p > w+ w+ p p QED=4 QCD=0, w+ > l+ vl'"
gen_command2="'add process p p > w- w- p p QED=4 QCD=0, w- > l- vl~'"

#gen_command1="'generate p p > w+ w- p p QED=4 QCD=99, w+ > l+ vl, w- > l- vl~'"
#gen_command2="'NONE'"

model="SM_LS01_LT012_LM0167"
#model="sm"

reweight_file="/scratch/anlevin/madgraph_generation/reweight_card_ls_lm_lt_v3.dat"
#reweight_file="/scratch/anlevin/madgraph_generation/reweight_card_ls0ls1_v2.dat"
#reweight_file="NONE"

run_card="/scratch/anlevin/madgraph_generation/run_card_13_tev.dat"
param_card="/scratch/anlevin/madgraph_generation/param_card_lt1_v4.dat"

echo "output directory: "$output_dir
echo "using reweight_card: "$reweight_file
echo "using run_card: "$run_card
echo "using param_card: "$param_card

if ! [ -e $output_dir ]
    then
    echo "output directory does not exist"
    exit
fi

if ((`ls $output_dir | wc -l`))
    then
    echo "output directory is not empty, exiting"
    exit
fi

if [ $reweight_file != "NONE" ] && ! ls $reweight_file >& /dev/null
    then
    echo "reweight file does not exist, exiting"
    exit
fi

if ! ls $run_card >& /dev/null
    then
    echo "runcard does not exist, exiting"
    exit
fi

if ! ls $param_card >& /dev/null
    then
    echo "paramcard does not exist, exiting"
    exit
fi

if ! ls $output_dir >& /dev/null
    then
    echo "output directory does not exist, exiting"
    exit
fi

sleep 15

if hostname | grep 'lxplus.*\.cern\.ch' >& /dev/null; then 
    echo "running on lxplus"
    while((i<=imax)); do
	bsub -q 1nd "bash /afs/cern.ch/work/a/anlevin/madgraph_generation/make_lhe_weights.sh $gen_command1 $gen_command2 $i $output_dir $reweight_file $model $run_card $param_card"
	i=$(($i+1))
    done
elif hostname | grep 'mit\.edu' &> /dev/null; then
    echo "running at MIT"
    while((i<=imax)); do
	cat > submit.cmd <<EOF
universe = vanilla
Executable = /scratch/anlevin/madgraph_generation/make_lhe_weights.sh
Arguments = "$gen_command1 $gen_command2 $i $output_dir $reweight_file $model $run_card $param_card"
GetEnv = True
Requirements = (Arch == "X86_64") && (OpSys == "LINUX") && (HasFileTransfer)
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT 
Output = stderr_stdout_lsmt_${i}.dat
Error = stderr_stdout_lsmt_${i}.dat
Log = log_lsmt_${i}.dat
+AccountingGroup        = "group_cmsuser.$USER"
Queue 1
EOF
	i=$(($i+1))
	condor_submit submit.cmd
	rm submit.cmd
    done
else
    echo "running on unknown machine, exiting"
    exit
fi
