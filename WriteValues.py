input_file = open('GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct', 'r')

list_file = open('GTEx_Analysis_v8_Annotations_SampleAttributesDS_LeftVentricleOnly.tsv', 'r')
lisfile = list_file.read()
lisfile = lisfile.split('\n')

output_file = open('GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads_left_ventricle.tsv', 'w')

valid_exps = []
for line in lisfile:
	items = line.split('\t')
	valid_exps += [items[0]]

headers = []
output_file.write('\t')


input_line = 0
for line in input_file:
	items = line.split('\t')
	input_line += 1

	if input_line == 2:
		size_total = items[0]

	if input_line == 3:
		for experiment in items:
			valid = experiment in valid_exps
			headers += [[valid, experiment]]
			if valid:
				output_file.write('\t' + experiment)

	if input_line > 3:
		print('\rcurrent read ' + str(input_line-3) + ' of ' + size_total, end='')
		output_file.write('\n' + '\t'.join(items[0:2]))
		for i in range(len(headers)):
			if headers[i][0]:
				output_file.write('\t' + items[i])