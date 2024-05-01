import subprocess
import os
import argparse
def generate_ani_comparison_plot(A_to_A, B_to_B, A_to_B):
    # Run R script as a subprocess
    subprocess.run(["Rscript", f"{basic_path}/Pipeline_args.r", A_to_A, B_to_B, A_to_B])

def main():
    parser = argparse.ArgumentParser(description='Generate ANI comparison plot')
    parser.add_argument('A_to_A', type=str, help='Path to A_to_A matrix')
    parser.add_argument('B_to_B', type=str, help='Path to B_to_B matrix')
    parser.add_argument('A_to_B', type=str, help='Path to A_to_B matrix')
    args = parser.parse_args()

    generate_ani_comparison_plot(A_to_A, B_to_B, A_to_B)


if __name__ == "__main__":
    main()


