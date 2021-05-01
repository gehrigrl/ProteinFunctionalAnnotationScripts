# ProteinFunctionalAnnotationScripts

Set of code to parse .gbff files containing sequence information for Desulfovibrio Vulgaris str.
Hildenborough, as well as files with functional annotation of protein coding regions of this genome. 
Extracts the hypothetical proteins from the genome sequence and compiles annotations of these proteins
from a few different predictive methods into a .csv file. 

4 different tables can be created using the files MakeHypoTable.py, MakeECtable.py, 
MakeSummaryTable.py, and MakeProbTable.py. These files import a long chain of other files throughout the directory to create the tables, and can be run by themselves. The primary method for constructing tables throughout the files is to assemble a python dictionary with hypothetical protein IDs as keys and information of interest as values in the form of lists. The dictionary is then converted to a pandas dataframe, then to a .csv file.

Each file contains comments at the top describing its purpose. 

The first files that were made, and the primary files in the order of the pipeline include Hypo.py, DSVtags.py, DSVcheck.py, DSVtypes.py, MakeValues.py, MakeHypoTable.py, ResParse.py, and GoneList.py. These files extract basic information about the hypothetical proteins from GenBank files. The March annotation was primarily used, but the October annotation is also available and was compared to the March annotation. The Retrieve2014.py file fetches the 2014 DSV chromosome genome and the 2016 DSV plasmid genome.

MakeValues.py creates the MarProtIDList, which is used throughout most of the files to match up the hypothetical protein IDs with information about them from DeepEC, SAdLSA, hhblits, etc. 

Files associated with the DeepEC method include 3digit_EC_prediction.txt, Enzyme_prediction.txt, 3digitHypos.txt, BinaryHypos.txt, CheckRelate.py, and ExtractEnzymes.py. 

EnzymeTranslate.py translates EC numbers to descriptions of the enzymes biological functions. 

The two files SalsaGetUP.py and BlitsGetUP.py share a lot of repeated content and could be condensed into a single file. 

