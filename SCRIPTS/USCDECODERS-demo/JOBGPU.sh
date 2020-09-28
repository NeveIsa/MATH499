#!/bin/bash
#SBATCH --gres=gpu:k40:1        # 1 node with 1 K40 GPU
#SBATCH --ntasks=1              # 1 process
#SBATCH --cpus-per-task=8       # 8 CPUs
#SBATCH --mem=32GB              # 32 GB of memory
#SBATCH --time=0:20:00          # 20 mins run time
#SBATCH --account=tommytrojan  # Account to charge resources to
  
module load gcc
module load cuda
module load cudnn
module load python

#nvcc program.cu -o program
#./program

python demo-naive-model.py
