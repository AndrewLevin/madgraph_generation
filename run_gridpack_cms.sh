gridpack_filename=$1
nevents=$2
seed=$3
output_dir=$4

echo \$gridpack_filename
echo $gridpack_filename

echo \$nevents
echo $nevents

echo \$seed
echo $seed

echo \$output_dir
echo $output_dir

export SCRAM_ARCH=slc6_amd64_gcc481
scram p CMSSW CMSSW_7_1_20_patch3
cd CMSSW_7_1_20_patch3/src/
eval `scram runtime -sh`

echo "copying gridpack"
echo ""

cp $gridpack_filename run_01_gridpack.tar.gz

echo""
echo "untaring gridpack"
echo ""

tar -xvf run_01_gridpack.tar.gz

echo ""
echo "begin generating events" 
echo ""

bash 

./runcmsgrid.sh $nevents $seed 1

echo ""
echo "finished generating events"
echo ""

#gunzip events.lhe.gz

echo ""
echo "begin copying output file"
echo ""

cp cmsgrid_final.lhe ${output_dir}events_${seed}.lhe

echo ""
echo "finished copying output file"
echo ""
