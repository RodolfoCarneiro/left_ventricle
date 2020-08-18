GetTranscripts.py and WriteValues.py are short algorithms written in Python solely to get Left Ventricle experiments from GTEx RNA-seq data.

GetTranscripts.py uses an annotation file downloaded from GTEx portal in .txt format, and creates an output file containing only the annotations that contained the key expression "left ventricle".

WriteValues.py uses the output from GetTranscripts.py and any RNA-Seq data downloaded from GTEx portal and writes as output only the data from the experiments listed in the GetTranscript.py output.

Both scipts were written in Python 3 language, and are easily editable via notepad, requiring only to change the files names and the key expression.