
def gfa_to_fasta(gfa_file, fasta_file):
    with open(gfa_file, 'r') as gfa, open(fasta_file, 'w') as fasta:
        for line in gfa:
            if line.startswith('S'):
                fields = line.strip().split('\t')
                sequence_id = fields[1]
                sequence = fields[2]
                fasta.write(f'>{sequence_id}\n{sequence}\n')

# Example usage
gfa_file = '24_miniasm.gfa'
fasta_file = '24_miniasm.fasta'
gfa_to_fasta(gfa_file, fasta_file)
