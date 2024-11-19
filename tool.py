import subprocess
import os
import sys
import time


def print_green(text): print("\033[92m{}\033[00m" .format(text))

def print_red(text): print("\033[91m{}\033[00m" .format(text))

def print_cyan(text): print("\033[96m{}\033[00m" .format(text))

def find_file(root_dir, file_name):
    for root, dirs, files in os.walk(root_dir, topdown=True):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def Run_JLECmd():

    # To be used after running the function
    initial_directory = os.getcwd()

    destination_path = os.path.join(initial_directory, f"Results_JLECmd")
    source_path = "C:\\"

    # Define the command to be executed
    command = f'JLECmd.exe -d {source_path} --csv {destination_path} -q --mp'

    # Change the current working directory to 'bin'
    bin_directory = 'bin'
    if not os.path.exists(bin_directory):
        os.makedirs(bin_directory)

    # Change the current working directory
    os.chdir(bin_directory)

    # Execute the command and print real-time output
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Print real-time output from stdout
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print_cyan(output.strip())

        # Print any errors
        stderr_output = process.stderr.read()
        if stderr_output:
            print_red(f"Error message: \n{stderr_output}")
            print_red(f"Make sure that: ")
            print_red("- The appropriate .exe file is in the /bin folder")
            print_red("- Directories does not contain any whitespaces")
            print()

        # Check if the process exited with an error code
        return_code = process.poll()
        if return_code:
            raise subprocess.CalledProcessError(return_code, command)

    except subprocess.CalledProcessError as e:
        print_red("An error occurred while executing the command.")
        print_red(f"Error message: \n{e.stderr}")

    # Exits the bin folder and goes back to the previous directory
    os.chdir(initial_directory)

def Run_MFTECmd(file):

    # To be used after running the function
    initial_directory = os.getcwd()

    destination_path = os.path.join(initial_directory, f"Results_MFTECmd")

    # Finding the file
    print_green(f"Finding {file} in...")
    source_path = find_file('C:\\', f'{file}')
    if not source_path:
        print_red(f"Error: {file} file not found.")
        return
    else:
        print_green(f"Found {file} in {source_path}\n")

    # Define the command to be executed
    command = f'MFTECmd.exe -f {source_path} --csv {destination_path}'

    # Change the current working directory to 'bin'
    bin_directory = 'bin'
    if not os.path.exists(bin_directory):
        os.makedirs(bin_directory)

    # Change the current working directory
    os.chdir(bin_directory)

    # Execute the command and print real-time output
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Print real-time output from stdout
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print_cyan(output.strip())

        # Print any errors
        stderr_output = process.stderr.read()
        if stderr_output:
            print_red(f"Error message: \n{stderr_output}")
            print_red(f"Make sure that: ")
            print_red("- The appropriate .exe file is in the /bin folder")
            print_red("- Directories does not contain any whitespaces")
            print()

        # Check if the process exited with an error code
        return_code = process.poll()
        if return_code:
            raise subprocess.CalledProcessError(return_code, command)

    except subprocess.CalledProcessError as e:
        print_red("An error occurred while executing the command.")
        print_red(f"Error message: \n{e.stderr}")

    # Exits the bin folder and goes back to the previous directory
    os.chdir(initial_directory)

if __name__ == "__main__":

    print_green("JLECmd x MFTECmd")

    print_green("\nRunning JLECmd...\n")
    Run_JLECmd()

    print_green("\nRunning MFTECmd...\n")
    Run_MFTECmd("$J")
    Run_MFTECmd("$Secure_$SDS")
    Run_MFTECmd("$Boot")
    Run_MFTECmd("$MFT")

    print_green("\n-------------------")
    print_green("Press enter to exit")
    print_green("-------------------\n")

    input()
    sys.exit()

