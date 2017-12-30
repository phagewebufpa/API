<h3><strong>PhageWeb &ndash; A web interface for the rapid identification and characterization of prophages in bacterial genomes.</strong></h3>
<p><strong>Software Description:</strong></p>
<p>PhageWeb is a Web platform that performs the identification of prophages within bacterial genomes that takes into account similarity searches of genes sequences against a phage database. This computational tool allows to perform faster analyzes, thanks to the high performance of the alignment algorithm used compared to other computational alternatives. This work using indicators such as alteration of GC content and the presence of tRNA flanking the region for identification of regions prophages, in addition to allowing analysis of each of the regions through functional characterisation.</p>
<p>&nbsp;</p>
<h3><strong>Using the API</strong></h3>
<p><strong>INTRODUCTION</strong><br />PhageWeb is a computer program written in PHP, Python and Perl to identify prophages in a complete bacterial genome sequences.</p>
<p>The PhageWeb website is maintained by Center of Genomic and System Biology - Federal University of Par&aacute; (http://computationalbiology.ufpa.br/site/)</p>
<p><strong>SYSTEM REQUIREMENTS</strong><br />The program should run on all Unix platforms, although it was not tested in all platforms.</p>
<p><br /><strong>SOFTWARE REQUIREMENTS</strong><br />PhageWeb requires following programs to be installed in the system.</p>
<p>1. Python - version 3.0 or later<br />2. Biopython - version 1.7 or later</p>
<p>&nbsp;</p>
<p><strong>INSTALLATION</strong><br />The software installation on your system can be done by downloading it in binary format for immediate use: wget <a href="http://github.com/phagewebufpa/API/teste.py">http://github.com/phagewebufpa/API/teste.py</a></p>
<p><br /><strong>TO RUN</strong><br />% python phageweb.py -i organism_directory -o output_directory -c</p>
<p>where:<br />'output directory': Output directory is the directory where the final output file will be created</p>
<p>'organism directory': The seed annotation directory for the input bacterial organism <br />whose prophage(s) need to be identified.</p>
<p><br />Or, <br />If you have new genome, you can annotate it using RAST server (http://rast.nmpdr.org/rast.cgi). <br />After annotation, you can download the genome directory from the server.</p>
<p>&nbsp;</p>
<p><strong>OUTPUT FILE</strong><br />There are 2 output files, located in output directory.</p>
<p>1. ouput_tabular.tab: This file has four columns separated by tabs [region_id, lenght the prophage, start and end (position in genome)]. <br /> <br />2. output_genbanck.gbk: This file has a Genbank complete with file submitted with one annotation from each prophage region predicted.</p>
<p>&nbsp;</p>
