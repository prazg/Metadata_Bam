import pysam

# Open the BAM file
bamfile = pysam.AlignmentFile("path to the bam file", "rb")

# Fetch the header
header = bamfile.header

# Open a text file to write
with open('metadata_bam_ivygap.txt', 'w') as f:
    f.write(str(header))

# Close the BAM file
bamfile.close()
