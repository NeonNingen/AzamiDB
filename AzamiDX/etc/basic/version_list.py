from random import choice
from pathlib import Path

def version_num():
	version_num = ["V1.0", "V2.0", "V2.1"]
	return version_num

def version_desc():
	version1 = Path('AzamiDX/etc/basic/vlogs/version1.txt').read_text()
	version2 = Path('AzamiDX/etc/basic/vlogs/version2.txt').read_text()
	version2_1 = Path('AzamiDX/etc/basic/vlogs/version2_1.txt').read_text()

	version_desc = [version1, version2, version2_1]
	return version_desc