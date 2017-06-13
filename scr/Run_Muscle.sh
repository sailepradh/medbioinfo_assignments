#! /bin/bash -l  

## Before running the command install the necessary software or for this purpose module in uppmax

input=/Users/salendrapradh/Desktop/KTH courses/Medbio/Applied Bioinformatics/yeast_genes
## path to the directory where the files are available

cd ${input}
## change to the given directory

## loop out in each fasta file the muscle command as shown in http://www.drive5.com/muscle/muscle.html

for f in *.fasta; do
	echo "$f"
	## outputting the files that are processed
	muscle -in $f -out $f".aligned"
	echo "$f alignment done"
done
		
	