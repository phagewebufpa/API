PhageWeb – A web interface for the rapid identification and characterization of prophages in bacterial genomes.
Software Description:

PhageWeb is a Web platform that performs the identification of prophages within bacterial genomes that takes into account similarity searches of genes sequences against a phage database. This computational tool allows to perform faster analyzes, thanks to the high performance of the alignment algorithm used compared to other computational alternatives. This work using indicators such as alteration of GC content and the presence of tRNA flanking the region for identification of regions prophages, in addition to allowing analysis of each of the regions through functional characterisation.

 

Using the API
INTRODUCTION
PhageWeb is a computer program written in PHP, Python and Perl to identify prophages in a complete bacterial genome sequences.

The PhageWeb website is maintained by Center of Genomic and System Biology - Federal University of Pará (http://computationalbiology.ufpa.br/site/)

SYSTEM REQUIREMENTS
The program should run on all Unix platforms, although it was not tested in all platforms.


SOFTWARE REQUIREMENTS
PhageWeb requires following programs to be installed in the system.

1. Python - version 3.0 or later
2. Biopython - version 1.7 or later

 

INSTALLATION
The software installation on your system can be done by downloading it in binary format for immediate use: wget http://github.com/phagewebufpa/API/teste.py


TO RUN
% python phageweb.py -i organism_directory -o output_directory -c

where:
'output directory': Output directory is the directory where the final output file will be created

'organism directory': The seed annotation directory for the input bacterial organism 
whose prophage(s) need to be identified.


Or, 
If you have new genome, you can annotate it using RAST server (http://rast.nmpdr.org/rast.cgi). 
After annotation, you can download the genome directory from the server.

 

OUTPUT FILE
There are 2 output files, located in output directory.

1. ouput_tabular.tab: This file has four columns separated by tabs [region_id, lenght the prophage, start and end (position in genome)]. 

2. output_genbanck.gbk: This file has a Genbank complete with file submitted with one annotation from each prophage region predicted.

 
