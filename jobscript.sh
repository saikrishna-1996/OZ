#!/bin/bash
#SBATCH --cpus-per-task=10
#SBATCH --mem=30000M
#SBATCH --time=2-21:00
#SBATCH --requeue
#SBATCH --mail-user=saikrishnagv1996@gmail.com
#SBATCH --mail-type=ALL

source activate pytorch
echo Running on $HOSTNAME
python launch_script.py
