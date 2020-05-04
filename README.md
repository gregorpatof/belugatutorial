# Beluga Tutorial

This is a tutorial for using Python for parallel computing on Béluga.

The computation used as an example is finding prime numbers because it is very simple.

Here are the steps required to run this tutorial:

1. Clone the github repository somewhere on Beluga, preferably in the projects space. You can use this command:

git clone https://github.com/gregorpatof/belugatutorial


2. Look at the code in prime_testing.py. This is the equivalent of your executable or script that will be run in parallel. In this case, it is only a very naive way of finding the biggest prime number bigger or equal to the number passed as a comman-line argument.

3. Look at the parallel_run.py file. This is where the multiprocessing happens. The execute function is called in parallel with a Pool object, which will run it for every argument passed but with a maximum number of concurrent instances (in this example 40 because it is the number of CPUs in on compute node on Beluga).

4. Look at the beluga_job_whole_node.sh file. This is the job file that you need to submit to run on Beluga. It uses Slurm. The lines starting with #SBATCH are the parameters for the job. You should not need to change the first 5 ones. The --time one is in hours:minutes:seconds. When you run a short job you should always put 3:00:00 because it will not affect your priority and will also not overbill us (only the resources actually used are billed). You can also give the job a name with --name=something.

5. Change the path to the parallel_run.py file in the job file so that it matches the location of your file.

6. Now you can submit the job with:

sbatch beluga_job_whole_node.sh

7. You can see if your job is running with:

sq

8.
