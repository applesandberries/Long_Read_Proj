import subprocess
import os
import argparse

def gfa_to_fasta(gfa_file, fasta_file):
    with open(gfa_file, 'r') as gfa, open(fasta_file, 'w') as fasta:
        for line in gfa:
            if line.startswith('S'):
                fields = line.strip().split('\t')
                sequence_id = fields[1]
                sequence = fields[2]
                fasta.write(f'>{sequence_id}\n{sequence}\n')

def convert_gfa_files(gfa_folder, fasta_folder):
    # Ensure output directory exists
    os.makedirs(fasta_folder, exist_ok=True)
    
    # List all files in the input folder
    gfa_files = [f for f in os.listdir(gfa_folder) if f.endswith(".gfa")]

    for gfa_file in gfa_files:
        # Generate output file name
        fasta_file = os.path.splitext(gfa_file)[0] + ".fasta"
        fasta_path = os.path.join(fasta_folder, fasta_file)
        
        # Convert GFA to FASTA
        try:
            gfa_to_fasta(os.path.join(gfa_folder, gfa_file), fasta_path)
        except Exception as e:
            print(f"Error converting {gfa_file} to FASTA: {e}")
            continue

        print(f"Converted {gfa_file} to {fasta_file}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert GFA files to FASTA files")
    parser.add_argument("gfa_folder", type=str, help="Folder containing GFA files")
    parser.add_argument("fasta_folder", type=str, help="Folder to save FASTA files")
    args = parser.parse_args()

    # Convert GFA files to FASTA
    convert_gfa_files(args.gfa_folder, args.fasta_folder)
