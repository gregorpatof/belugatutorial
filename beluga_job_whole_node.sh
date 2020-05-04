#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --account=rrg-najmanov
#SBATCH --time=3:00:00

module purge
module load python/3

python /home/mailhoto/projects/rrg-najmanov/mailhoto/belugatutorial/parallel_run.py