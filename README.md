# Long read project

Our main goal is to develop a pipeline that allows comparison between long read sequences from any bacteria for strain identification.

## Description

Currently, there is no definitive way to prove two strain are identical and no universally accepted average nucleotide identity (ANI) threshold for strain identification. We aim to generate a soft-coded pipeline utilizing python and R for strain comparison by statisitcally determining the likelihood that two strains are not dissimilar to one another. Through this we will produce a method for generating assembled long reads (that can be used independently) and create non-biased subsampling of long read sequences to reassemble for theoretical comparison.

## Getting Started

### Dependencies

* Python
* R + packages: ggplot2, agricolae, dplyr
* Conda
* minimap2 - https://lh3.github.io/minimap2
* miniasm - https://github.com/lh3/miniasm
* Canu - see https://github.com/marbl/canu/releases downloading binary is recommended, can use homebrew or conda if necessary
* ANI calculator
* fastANI - use pip install fastani

### Installing

* How/where to download program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands if needed
```

## Authors

Helen Appleberry<br>
Alexa Ligon<br>
Hailey Bieneman<br>

## Acknowledgments
