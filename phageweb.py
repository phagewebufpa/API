import os
import subprocess
import sys
file = sys.argv[1]
identity = sys.argv[2]
result = subprocess.Popen(['curl', '-F','file=@' + file  ,'http://200.239.92.140:5000/phageweb/'+ identity], stdout=subprocess.PIPE)
id , err = result.communicate()
os.system("wget -c http://computationalbiology.ufpa.br/phageweb/analysis/api/" + id + "/output_tabular.tab")
os.system("wget -c http://computationalbiology.ufpa.br/phageweb/analysis/api/" + id + "/output_genbank.gbk")
