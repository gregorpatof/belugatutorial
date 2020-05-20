# Beluga Tutorial

This is a tutorial for using Python for parallel computing on Béluga.

The computation used as an example is finding prime numbers because it is very simple.

Here are the steps required to run this tutorial:

1. Clone the github repository somewhere on Beluga, preferably in the projects space. You can use this command:

git clone https://github.com/gregorpatof/belugatutorial


2. Look at the code in prime_testing.py. This is the equivalent of your executable or script that will be run in parallel. In this case, it is only a very naive way of finding the smallest prime number bigger or equal to the number passed as a command-line argument.

3. Look at the parallel_run.py file. This is where the multiprocessing happens. The execute function is called in parallel with a Pool object, which will run it for every argument passed but with a maximum number of concurrent instances (in this example 40 because it is the number of CPUs in on compute node on Beluga).

4. Look at the beluga_job_whole_node.sh file. This is the job file that you need to submit to run on Beluga. It uses Slurm. The lines starting with #SBATCH are the parameters for the job. You should not need to change the first 5 ones. The --time one is in hours:minutes:seconds. When you run a short job you should always put 3:00:00 because it will not affect your priority and will also not overbill us (only the resources actually used are billed). You can also give the job a name with --name=something.

5. In the job file, change the path to the parallel_run.py file so that it matches the location of your file.

6. Now you can submit the job with:

sbatch beluga_job_whole_node.sh

7. You can see if your job is running with:

sq

8. When sq does not show your job anymore, it is done! You can find its output in the directory you started it from. It contains 100 very big prime numbers (which are to be treated with respect as they are rare entities) and will be looking something like:

slurm-xxxxxxx.out

9. xxxxxxx is the job number. With this number you can get info on the job's running time and efficiency (both CPU and memory) with the command:

seff xxxxxxxx

Note: usually the memory efficiency of jobs is very low, and that is perfectly fine. It just means that what you are doing is more compute-intense than memory-intense. However, if your CPU efficiency is below around 50%, it probably means that you are doing too much input-output or that your parallelization scheme is not working.

That's all folks! Now you should be ready to run parallel jobs on Beluga using Python :-)

P.S. Remember to periodically check our usage of the allocation with:

sshare -A rrg-najmanov_cpu -l

The column we care about is LevelFS, and as long as it is bigger than 1 we can submit as many jobs as we like.