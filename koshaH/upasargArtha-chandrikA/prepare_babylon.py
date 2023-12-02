import re
import glob

header = """
#bookname=upasargArthachandrikA (sa-sa)
#stripmethod=keep
#sametypesequence=h
#description=https://github.com/indic-dict/stardict-sanskrit-vyAkaraNa/issues/10

"""

def prepare_babylon():
	content_files = glob.glob('*.md')
	content_files = [f for f in content_files if 'index.md' not in f]
	content_files = sorted(content_files)
	fileout = 'upasargArthachandrikA.babylon'
	fout = open(fileout, 'w')
	fout.write(header)
	for filein in content_files:
		print(filein)
		fin = open(filein, 'r')
		data = fin.read()
		fin.close()
		parts = data.split('##')
		# Discarding the top title part
		parts_of_interest = parts[1:]
		for p in parts_of_interest:
			itms = p.split('-')
			dhAtu = itms[0]
			dhAtu = dhAtu.rstrip().lstrip()
			sopasarga = itms[1]
			sopasarga = sopasarga.rstrip('}\n').lstrip('- {')
			definition = '-'.join(itms[2:])
			definition = '-' + definition
			definition = definition.rstrip()
			definition = definition.replace('\n', '<br>')
			# Try to convert double asterisks to `<b></b>` tags.
			definition = re.sub('[*]{2}([^*]*)[*]{2}', '<b>\g<1></b>', definition)
			hws = dhAtu + '|' + sopasarga
			#print(hws)
			#print(definition)
			#print()
			fout.write(hws + '\n' + definition + '\n\n')

	fout.close()

	# Postprocessing to remove trailing blank lines
	babylon_file = 'upasargArthachandrikA.babylon'
	fin = open(babylon_file, 'r')
	data = fin.read()
	data = data.rstrip()
	fin.close()
	fout = open(babylon_file, 'w')
	fout.write(data)
	fout.close()



if __name__ == "__main__":
	prepare_babylon()

