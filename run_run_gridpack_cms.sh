nevents=100
njobs=100
gridpack_filename=/afs/cern.ch/work/a/anlevin/public/for_wwjj_ss_dim8_ewk_qcd_mc_request_05Jan2016/WWjj_SS_dim8_ewk_qcd_tarball.tar.xz
output_dir=/afs/cern.ch/work/a/anlevin/data/lhe/13_tev/wwjj_ss_dim8_ewk_qcd/

seed=1

while((seed<=njobs)); do
    bsub -q 8nh "bash run_gridpack_cms.sh $gridpack_filename $nevents $seed $output_dir"
    seed=$(($seed+1))
done
