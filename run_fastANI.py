import subprocess
import os
import argparse
from Bio import SeqIO

def read_fasta_files(folder_path):
    fasta_files = [f for f in os.listdir(folder_path) if f.endswith('.fasta')]
    return [os.path.join(folder_path, f) for f in fasta_files]

def run_fastani(query_folder, reference_folder, output_dir):
    query_files = read_fasta_files(query_folder)
    reference_files = read_fasta_files(reference_folder)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    for query_file in query_files:
        query_name = os.path.splitext(os.path.basename(query_file))[0]
        for reference_file in reference_files:
            reference_name = os.path.splitext(os.path.basename(reference_file))[0]
            output_file = os.path.join(output_dir, f"{query_name}_vs_{reference_name}_fastani_output.txt")
            
            # Define FastANI command
            fastani_cmd = f"./fastANI -q {query_file} -r {reference_file} -o {output_file}"
            
            # Run FastANI using subprocess
            try:
                subprocess.run(fastani_cmd, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running FastANI for {query_file} and {reference_file}: {e}")
                continue

            print(f"FastANI completed successfully for {query_file} and {reference_file}!")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run FastANI on multiple pairs of query and reference FASTA files")
    parser.add_argument("query_folder", type=str, help="Folder containing query FASTA files")
    parser.add_argument("reference_folder", type=str, help="Folder containing reference FASTA files")
    parser.add_argument("output_dir", type=str, help="Output directory")
    args = parser.parse_args()

    # Run FastANI
    run_fastani(args.query_folder, args.reference_folder, args.output_dir)

# command line: python3 new_fastANI.py full_fasta full_fasta f_f_ANIout1
