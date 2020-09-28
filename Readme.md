
# MATH499 - Fall 2020 
---

### Linux commands cheatsheet
https://files.fosswire.com/2007/08/fwunixref.pdf

### Using Tensorflow on Discovery Cluster  
---

##### 1. Login to Discovery
`ssh usc_username@discovery.usc.edu` || `ssh usc_username@discovery2.usc.edu`

##### 2. Change directory to your SCRIPTS subfolder
`cd /project/tiruvilu_529/MATH499/SCRIPTS/TeamX for X in {1,2,3,4,...}`

##### 3. Create and set Parameters in a JOB.sh (or JOBGPU.sh if using GPU) file

- Make sure you pass your USC_USERNAME to --account
- Make sure you are calling your python script in the last line - python YourScript.py
- Be careful about the time for which you reserve resources in the --time field. Only reserve the amount you need. 
- Experiment with smaller time values first to see epoch time estimates (see STEP 4) and accordingly over provision resource time by about 25%. 

 
```
#!/bin/bash
#SBATCH --gres=gpu:k40:1        # 1 node with 1 K40 GPU (DELETE line for no GPU)
#SBATCH --ntasks=1              # 1 process
#SBATCH --cpus-per-task=8       # 8 CPUs
#SBATCH --mem=16GB              # 16 GB of memory
#SBATCH --time=0:20:00          # 20 minutes run time
#SBATCH --account=USC_USERNAME  # Account to charge resources to
  
module load gcc
module load cuda
module load cudnn
module load python

python YourScript.py

```


##### 4. Call your script JOB.sh (or JOBGPU.sh if using GPU)

To get resource and run your python script in the allocated resource, call the JOB.sh (or JOBGPU.sh) file you created above. 

```
sh JOB.sh

or 

sh JOBGPU.sh

```












------------
OLDER INSTRUCTIONS 
------------

### go to /scratch/USCusername
`cd /scratch/USCusername`

### clone this repo
`git clone https://github.com/NeveIsa/MATH499`

### change directory to MATH499
`cd MATH499`


### Download RAW data
```
cd RAW

make tranchX #for just tranch_X data where X -> {1,2,3}

make all # for downloading all data i.e tranch1,2 and 3

```


### Project Folder
```
cd /project/tiruvilu_529/
```
