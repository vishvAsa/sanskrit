import re
import glob
import json
from indic_transliteration import sanscript

def obsolete_generate_file_upasarga_map():
	content_files = glob.glob('*.md')
	content_files = [f for f in content_files if 'index.md' not in f]
	file_upasarga_map = {}
	for fil in content_files:
		prt = fil.split('_')
		upasarga = prt[1].replace('.md', '')
		upasarga = sanscript.transliterate(upasarga, 'itrans', 'devanagari')
		file_upasarga_map[fil] = upasarga
	print(file_upasarga_map)
	fileout = 'trial/file_upasarga_map.json'
	fout = open(fileout, 'w')
	json.dump(file_upasarga_map, fout, ensure_ascii=False, indent=1)
# No need to rerun. The file is already generated.
#generate_file_upasarga_map()


def obsolete_prepare_auto_added_upasargas():
	content_files = glob.glob('*.md')
	content_files = [f for f in content_files if 'index.md' not in f]
	with open('trial/file_upasarga_map.json', 'r') as jin:
		fup_map = json.load(jin)
	
	for filein in content_files:
		with open(filein, 'r') as fin:
			data = fin.read()
		upasarga = fup_map[filein]
		print(filein)
		data = re.sub('\n##([ ]*)(.*)([ ]*)\n-', '\n##\g<1>\g<2>\g<3>\n### '+upasarga+'\g<2>\n-', data)
		fileout = 'trial/' + filein
		fout = open(fileout, 'w')
		fout.write(data)
		fout.close()

# Not necessary to run again
# prepare_auto_added_upasargas()

# change the triple hashes to "- {प्राज्}"
def change_hash_to_dash():
	content_files = glob.glob('trial/*.md')
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
	change_hash_to_dash()

