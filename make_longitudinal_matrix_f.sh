for file in `ls /scratch3/anlevin/MG5_aMC_v2_2_1/wp_wp_14_tev_fm0_20_longitudinal/SubProcesses/P0_qq_wmwmqq/ | grep "matrix[0123456789]*.f"`
  do
  python2.6 make_longitudinal_matrix_f.py /scratch3/anlevin/MG5_aMC_v2_2_1/wp_wp_14_tev_fm0_20_longitudinal/SubProcesses/P0_qq_wmwmqq/$file $file
  mv $file /scratch3/anlevin/MG5_aMC_v2_2_1/wp_wp_14_tev_fm0_20_longitudinal/SubProcesses/P0_qq_wmwmqq/$file
done