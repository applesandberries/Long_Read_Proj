import subprocess

def generate_ani_comparison_plot(A_to_A, B_to_B, A_to_B):
    # Run R script as a subprocess
    subprocess.run(["Rscript", "/Downloads/pipline_rscript.R", A_to_A, B_to_B, A_to_B])

def main():
    # Provide the paths to the three matrices here
    A_to_A = "/Downloads/AtoA.txt"
    B_to_B = "/Downloads/BtoB.txt"
    A_to_B = "/Downloads/AtoB.txt"

    generate_ani_comparison_plot(A_to_A, B_to_B, A_to_B)


if __name__ == "__main__":
    main()


