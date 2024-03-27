#still working on the assembly code
path="/Users/lennyberry/sequencingfiles"
#change this to argparse with path to files
x=glob.glob(path+"*")
list_of_fastq_prefixes=set()
for i in x:
    p=i[len(path):i.find('.fastq')]
        list_of_fastq_prefixes.add(p)
for i in list_of_fastq_prefixes:
	command= 'minimap2' +i+' \ '+i+'/ \ | gzip -1 > ./minimap.paf.gz'
        os.print(command)
	#os.system(command)
        command = 'miniasm -f \'+i+' \ /minimap.paf.gz > miniasm.gfa'
        os.system(command)
	#os.print(command)
