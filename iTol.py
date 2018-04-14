#!/bin/bash --login
#PBS -l walltime=02:00:00
#PBS -l select=1:ncpus=36
#PBS -N Group_significance_Nitro_closed
#PBS -A d411-training
cd $PBS_O_WORKDIR
module load miniconda/python2
export TMPDIR=~/qiime_tmp
echo "loading virtualenv"
source activate qiime1

time iTol.py \
-i ~/2018_02_smb/OTU_network/otu_network/ \
-m ~/2018_02_smb/map.tsv \
-o ~/iTol_Out


