sample="E70_1"
path=/data/gouyuwei/${sample}
/data/gouyuwei/SOFTWARE/HiC-Pro_2.9.0/bin/utils/digest_genome.py Sscrofa11.1.fasta -r mboi -o MboI_resfrag_sus11.bed
/data/gouyuwei/SOFTWARE/HiC-Pro_2.9.0/bin/HiC-Pro -i $path/data -o $path/results -c $path/config_test_latest.txt