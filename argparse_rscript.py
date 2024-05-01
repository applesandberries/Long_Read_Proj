import argparse
import subprocess

def generate_ani_comparison_plot(A_to_A, B_to_B, A_to_B):
    # run R script as a subprocess
    subprocess.run(["Rscript", "ani_comparison_plot.R", A_to_A, B_to_B, A_to_B])

def main():
    parser = argparse.ArgumentParser(description="Generate ANI comparison plot.")
    parser.add_argument("--A_to_A_ANI_file", required=True, help="Path to A to A ANI file")
    parser.add_argument("--B_to_B_ANI_file", required=True, help="Path to B to B ANI file")
    parser.add_argument("--A_to_B_ANI_file", required=True, help="Path to A to B ANI file")
    args = parser.parse_args()

    generate_ani_comparison_plot(args.A_to_A, args.B_to_B, args.A_to_B)

if __name__ == "__main__":
    main()
