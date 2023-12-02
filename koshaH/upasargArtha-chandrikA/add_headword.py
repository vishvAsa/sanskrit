import re
import glob
import json
from indic_transliteration import sanscript

def generate_file_upasarga_map():
	content_files = glob.glob('*.md')
	content_files = [f for f in content_files if 'index.md' not in f]
	file_upasarga_map = {}
	for fil in content_files:
		prt = fil.split('_')
		upasarga = prt[1].rstrip('.md')
		upasarga = sanscript.transliterate(upasarga, 'itrans', 'devanagari')
		file_upasarga_map[fil] = upasarga
	print(file_upasarga_map)
	fileout = 'trial/file_upasarga_map.json'
	fout = open(fileout, 'w')
	json.dump(file_upasarga_map, fout, ensure_ascii=False, indent=1)
generate_file_upasarga_map()

"""
with open('001_pra.md', 'r') as fin:
	data = fin.read()
upasarga = 'प्र'
data = re.sub('\n##([ ]*)(.*)([ ]*)\n-', '\n##\g<1>\g<2>\g<3>\n### '+upasarga+'\g<2>\n-', data)

print(data)
"""

