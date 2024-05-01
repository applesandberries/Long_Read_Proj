# Long read project

Our main goal is to develop a pipeline that allows comparison between long read sequences from any bacteria for strain identification using average nucleotide identity.

## Description

Currently, there is no definitive way to prove two strain are identical and no universally accepted average nucleotide identity (ANI) threshold for strain identification. We aim to generate a soft-coded pipeline utilizing python and R for strain comparison by statisitcally determining the likelihood that two strains are not dissimilar to one another. Through this we will produce a method for generating assembled long reads (that can be used independently) and create non-biased subsampling of long read sequences to reassemble for theoretical comparison.

## Getting Started

### Dependencies
* Python
* R + packages: ggplot, dplyr, agricolae, tidyverse, writex1, ggbreak, hrbrthemes, plotrix, RColorBrewer, empirical
* Conda
* minimap2 - https://lh3.github.io/minimap2
* miniasm - https://github.com/lh3/miniasm
* fastANI - https://github.com/ParBLiSS/FastANI easiest install using dependency-free binary for Linux or OSx from FastANI v1.34 release
* Seqtk (please install via (conda install seqtk) rather than github or install through github but be sure to add seqtk to main path to be used as a command without providing path))

### Installing

clone repo here:
```
git clone https://github.com/applesandberries/Long_Read_Proj.git
```
### Executing program

First download and unzip out two example files! SKIP THIS STEP IF YOU ALREADY HAVE FILES TO RUN THIS WITH.
MAKE SURE TO PUT THESE FILES IN A FOLDER WITH ONLY THEMSELVES. I RECOMMEND CALLING IT fastaFiles
```
mkdir fastaFiles
cd fastaFiles
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR169/056/SRR16938656/SRR16938656_1.fastq.gz -o SRR16938656_Long-read_sequencing_of_E._coli_UMB1284_1.fastq.gz
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR169/058/SRR16938658/SRR16938658_1.fastq.gz -o SRR16938658_Long-read_sequencing_of_E._coli_UMB1180_1.fastq.gz
gunzip SRR16938656_Long-read_sequencing_of_E._coli_UMB1284_1.fastq.gz
gunzip SRR16938658_Long-read_sequencing_of_E._coli_UMB1180_1.fastq.gz
```
Then cd into the github repo you just downloaded!
```
cd Long_Read_Project
```
Now run the pipeline!
The pipeline will run from the python6 file. It requires several other files in github to run, and it makes the assumption they are in the same directory as the python6 file, so please don't move arround any of the files in the github.
It takes two arguments:
-i path to fastq files
-o path for ani output
I recommend calling the ani output: output because I am lazy
SYNTAX IS VERY IMPORTANT PLEASE ADD THE / AT THE END OF YOUR -i PATH, BUT NOT YOUR -o PATH
Your graph output will be in the Long_Read_Project folder under Rplots.pdf
Here is a sample of what the running the pipeline looks like:
```
python python6 -i /home/happleberry/Long_Read_Proj/fastqFiles/ -o /home/happleberry/Long_Read_Proj/Long_Read_Proj/output
```
## Authors

Helen Appleberry<br>
Alexa Ligon<br>
Hailey Bieneman<br>

## Acknowledgments

Special thanks to Dr. Putonti and Dr. Banerjee for allowing us to work on this project, giving advice on the project, and providing valuable resources. 
