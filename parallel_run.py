from multiprocessing import Pool
import subprocess
import shlex
import random


def execute(command_string, working_directory=None, capture_output=True):
    """ This function executes a system command that is passed as a string. It returns a CompletedProcess instance
        ( see https://docs.python.org/3/library/subprocess.html#subprocess.run for more info).
        The working directory can be set with the optional argument working_directory, otherwise it will be the
        current directory. By default the output (stdout and stderr) is captured.
    """
    assert isinstance(command_string, str)
    commands_list = shlex.split(command_string)  # the command needs to be a list for subprocess.run()
    if capture_output:
        return subprocess.run(commands_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_directory)
    else:
        return subprocess.run(commands_list, cwd=working_directory)


def find_n_primes(n_primes, n_processors=40):
    """ Function that finds n prime numbers with a very naive algorithm (as an example of somewhat costly computation).
        It picks n random starting numbers between 50000000000000000 and 100000000000000000, and finds the first prime
        bigger or equal to each of these random numbers by making a system call to the prime_testing.py script.
    """
    all_commands = []  # list that will contain all the commands to run
    for i in range(n_primes):
        r = random.randint(50000000000000000, 100000000000000000)
        all_commands.append("python prime_testing.py {0}".format(r))

    p = Pool(n_processors)  # creates a pool to run parallel processes
    results = p.map(execute, all_commands)

    # results is now a list of CompletedProcess objects, so we need to fetch the stdout attribute
    results = [x.stdout.decode('utf-8').strip() for x in results]  # strip() removes the newline
    return results


if __name__ == "__main__":
    for prime in find_n_primes(100):
        print(prime)
