from Bio import SeqIO

# Specify the path to your file
file_path = "polar_bear.gene.cds\polar_bear.v1.5.cds.change"

# Read and parse the sequences from the file
for record in SeqIO.parse(file_path, "fasta"):
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence: {record.seq}")
    print("-----------")