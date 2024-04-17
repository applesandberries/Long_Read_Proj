import subprocess
import os
import argparse

def run_fastani(fasta_file1, fasta_file2, output_dir, output_file):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Define output file path
    output_path = os.path.join(output_dir, output_file)
    
    # Define FastANI command
    fastani_cmd = f"./fastANI -q {fasta_file1} -r {fasta_file2} -o {output_path}"
    
    # Run FastANI using subprocess
    try:
        subprocess.run(fastani_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running FastANI: {e}")
        return

    print("FastANI completed successfully!")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run FastANI on two fasta files")
    parser.add_argument("fasta_file1", type=str, help="First fasta file")
    parser.add_argument("fasta_file2", type=str, help="Second fasta file")
    parser.add_argument("output_dir", type=str, help="Output directory")
    parser.add_argument("output_file", type=str, help="Output file name")
    args = parser.parse_args()

    # Run FastANI
    run_fastani(args.fasta_file1, args.fasta_file2, args.output_dir, args.output_file)
    