#!/bin/bash
#SBATCH --cpus-per-task=30
#SBATCH --mem=30000M
#SBATCH --time=2-21:00
#SBATCH --requeue
#SBATCH --mail-user=email@provider.com
#SBATCH --mail-type=ALL

source activate sai
echo Running on $HOSTNAME
python launch_script.py
