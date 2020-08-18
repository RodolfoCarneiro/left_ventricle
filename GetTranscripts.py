output_file = open('GTEx_Analysis_v8_Annotations_SampleAttributesDS_LeftVentricleOnly.txt', 'w')
for line in open('GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt', 'r'):
	itens = line.split('\t')
	if 'left ventricle' in itens[6].lower():
		output_file.write(line)