import re
import glob

def obsolete_change_hash_to_dash():
	content_files = glob.glob('trial/*.md')
	content_files = [f for f in content_files if 'index.md' not in f]
	for filein in content_files:
		print(filein)
		fin = open(filein, 'r')
		data = fin.read()
		fin.close()
		# make the necessary change
		data = re.sub('\n###[ ]*(.*)[ ]*\n', '\n- {\g<1>}\n', data)
		fileout = filein
		fout = open(fileout, 'w')
		fout.write(data)
		fout.close()

if __name__ == "__main__":
	filein = '212_upa.md'		
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
		hws = dhAtu + '|' + sopasarga
		print(hws)
		print(definition)
		print()

	# make the necessary change

