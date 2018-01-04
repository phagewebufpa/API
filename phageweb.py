import os
import subprocess
import sys
x = False
file = 'temp/genome_temp.gbk'
def check_values(identity,cds):
    c_cds = True
    c_identity = True
    if cds < 6:
        print("The min point value for [minpoints] is '6'")
        c_cds = False


    if identity < 20 or identity > 100:
        c_identity = False
        print("Please use values between 30 ~ 100")


    if c_cds and c_identity:
        return True
    else:
        return False



if len(sys.argv) > 1:
    file = sys.argv[1]
    identity = sys.argv[2]
    cds = sys.argv[3]
    os.system("mkdir temp -p")
    os.system("cp '" + file + "' temp/genome_temp.gbk")
    x = check_values(int(identity),int(cds))
else:
    print("\nSOFTWARE REQUIREMENTS\nPhageWeb requires following programs to be installed in the system.\n1. Python - version 3.0 or later;\n2. CURL;\n\nTO RUN\n$ python3 phageweb.py [input_file] [identily] [minpts]\nWhere:\n[input_file]: Bacterial genome file in Gbk format for analysis. Check and see if your genome file (Genbank file) contains protein sequences for all CDS and the complete nucleotide sequence. A valid genome file (See the samples files below) must have complete protein sequence data (under the '/ translation' tag).\n[identily]: It is a percentage of alignment identity against the available phage database (30% ~ 100%).\n[minpts]: is the minimum number of phage proteins in a prophage region (clustering).\n\nOr, \nIf you have new genome, you can annotate it using RAST server (http://rast.nmpdr.org/rast.cgi). \nAfter annotation, you can download the genome directory from the server.\n\nOUTPUT FILE\nThere are 2 output files, located in output directory.\n1. ouput_tabular.tab: This file has four columns separated by tabs [region_id, lenght the prophage, start and end (position in genome)].\n2. output_genbank.gbk: This file has a Genbank complete with file submitted with one annotation from each prophage region predicted.\n3. output_char.txt: Contains the biological information pertaining to all sequences identified by the software.\n")

if x:
    result = subprocess.Popen(['curl', '-F','file=@' + file  ,'http://200.239.92.140:5000/phageweb/'+ identity + '/'+ cds], stdout=subprocess.PIPE)
    id , err = result.communicate()
    os.system("wget -c http://computationalbiology.ufpa.br/phageweb/analysis/api/" + id + "/output_tabular.tab")
    os.system("wget -c http://computationalbiology.ufpa.br/phageweb/analysis/api/" + id + "/output_genbank.gbk")
    os.system("wget -c http://computationalbiology.ufpa.br/phageweb/analysis/api/" + id + "/output_characterization.txt")

    os.system("rm " + file)
