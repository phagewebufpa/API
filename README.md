<h2 style="text-align: justify;"><strong>PhageWeb &ndash; A web interface for the rapid identification and characterization of prophages in bacterial genomes.</strong></h2>
<p style="text-align: justify;"><strong>Software Description:</strong></p>
<p style="text-align: justify;">PhageWeb is a Web platform that performs the identification of prophages within bacterial genomes that takes into account similarity searches of genes sequences against a phage database. This computational tool allows to perform faster analyzes, thanks to the high performance of the alignment algorithm used compared to other computational alternatives. This work using indicators such as alteration of GC content and the presence of tRNA flanking the region for identification of regions prophages, in addition to allowing analysis of each of the regions through functional characterisation.&nbsp;</p>
<p style="text-align: justify;">For to acess the complete tool:&nbsp;<a href="http://computationalbiology.ufpa.br/phageweb">http://computationalbiology.ufpa.br/phageweb</a></p>
<p style="text-align: justify;">&nbsp;</p>
<h3 style="text-align: justify;"><strong>Using the API</strong></h3>
<p style="text-align: justify;"><strong>INTRODUCTION</strong><br />PhageWeb is a computer program written in PHP, Python and Perl to identify prophages in a complete bacterial genome sequences.</p>
<p style="text-align: justify;">The PhageWeb website is maintained by Center of Genomic and System Biology - Federal University of Par&aacute; (http://computationalbiology.ufpa.br/site/)</p>
<p style="text-align: justify;"><strong>SYSTEM REQUIREMENTS</strong><br />The program should run on all Unix platforms, although it was not tested in all platforms.</p>
<p style="text-align: justify;"><br /><strong>SOFTWARE REQUIREMENTS</strong><br />PhageWeb requires following programs to be installed in the system.</p>
<p style="text-align: justify;">1. Python - version 3.0 or later</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;"><strong>INSTALLATION</strong><br />The software installation on your system can be done by downloading it in binary format for immediate use: wget <a href="http://github.com/phagewebufpa/API/teste.py">http://github.com/phagewebufpa/API/phageweb.py</a></p>
<p style="text-align: justify;"><br /><strong>TO RUN</strong><br />% python3 phageweb.py --file [inpu_file] --id [identily] --integrity [integrity] --cds [minpts] --email '[mail]'</p>
<p style="text-align: justify;"><br /><strong>Example:</strong><br />% python3 phageweb.py --file genome.gbk --id 80 --integrity 90 --cds 6 --email 'example@mail.com'</p>
<p style="text-align: justify;"><strong>Where:</strong></p>
<p style="text-align: justify;">'input_file': Bacterial genome file in Gbk format for analysis.&nbsp;Check and see if your genome file (Genbank file) contains protein sequences for all CDS and the complete nucleotide sequence. A valid genome file (See the samples files below) must have complete protein sequence data (under the "/ translation" tag).</p>
<p style="text-align: justify;">'identily':&nbsp;It is a percentage of alignment identity against the available phage database (30% ~ 100%).</p>
<p style="text-align: justify;">'integrity ':&nbsp;is the minimum number of phage proteins in a prophage region (clustering).</p>
<p style="text-align: justify;">'minpts':&nbsp;that will be used in the analysis of the elements of the regions of prophages identified.</p>
<p style="text-align: justify;">'mail':&nbsp;email that do you want to receive the results .</p>
<p style="text-align: justify;"><br />Or, <br />If you have new genome, you can annotate it using RAST server (http://rast.nmpdr.org/rast.cgi). <br />After annotation, you can download the genome directory from the server.</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;"><strong>OUTPUT FILE</strong><br />There are 2 output files, located in output directory.</p>
<p style="text-align: justify;">1. ouput_tabular.tab: This file has four columns separated by tabs [region_id, lenght the prophage, start and end (position in genome)]. <br /> <br />2. output_genbank.gbk: This file has a Genbank complete with file submitted with one annotation from each prophage region predicted. <br /> <br />3. output_char.txt: Contains the biological information pertaining to all sequences identified by the software.</p>
<p style="text-align: justify;">&nbsp;</p>
