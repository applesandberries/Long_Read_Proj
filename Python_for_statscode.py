import subprocess

def execute_r_script(file_path):
    subprocess.run(["Rscript", "/Downloads/Stats.R", file_path]) # r script

def main():
    file_path = "/Downloads/AtoB.txt" # input file
    execute_r_script(file_path)

if __name__ == "__main__":
    main()
