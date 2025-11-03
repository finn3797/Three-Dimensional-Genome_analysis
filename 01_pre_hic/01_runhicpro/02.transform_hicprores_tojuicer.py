#transform  Hic-pro result to juicer short format
import os
import gzip
import sys


def get_frag_info(frag_fname):
    info = {}
    count = 1
    f = open(frag_fname)
    for line in f:
        parts = line.split()
        info[parts[3]] = count
        count += 1
    f.close()
    return info


def main(infname,outfname,frag_fname):
    frag_info = get_frag_info(frag_fname)
    outf = open(outfname,'w')
    if 'gz' in infname:
        inf = gzip.open(infname)
        for line in inf:
            line = line.decode()
            parts = line.split()
            strand1 = parts[3]
            strand2 = parts[6]
            chr1 = parts[1]
            chr2 = parts[4]
            pos1 = parts[2]
            pos2 = parts[5]
            frag1 = parts[8]
            frag2 = parts[9]
            if strand1 == '+':
                str1 = '0'
            else:
                str1 = '1'
            if strand2 == '+':
                str2 = '0'
            else:
                str2 = '1'
            outf.write(f'{str1} {chr1} {pos1} {frag_info[frag1]} {str2} {chr2} {pos2} {frag_info[frag2]}\n')
    else:
        inf = open(infname)
        for line in inf:
            parts = line.split()
            strand1 = parts[3]
            strand2 = parts[6]
            chr1 = parts[1]
            chr2 = parts[4]
            pos1 = parts[2]
            pos2 = parts[5]
            frag1 = parts[8]
            frag2 = parts[9]
            if strand1 == '+':
                str1 = '0'
            else:
                str1 = '1'
            if strand2 == '+':
                str2 = '0'
            else:
                str2 = '1'
            outf.write(f'{str1} {chr1} {pos1} {frag_info[frag1]} {str2} {chr2} {pos2} {frag_info[frag2]}\n')
    outf.close()
    inf.close()



if __name__ == '__main__':
    infname = sys.argv[1]
    outfname = sys.argv[2]
    frag_fname = '/data/gouyuwei/MboI_resfrag_sus11.bed'
    main(infname,outfname,frag_fname)