# encoding: utf-8

import os
import shutil
import subprocess
import sys
import tempfile

class TempDir:
	def __enter__(self):
		self.d = tempfile.mkdtemp()
		return self.d
	def __exit__(self, typ, val, trace):
		shutil.rmtree(self.d)

def TestMain():
	TestCreate()

def TestCreate():
	# OS에 맞는 create 스크립트 선택
	osExt = {
		"win32": ".bat",
		"linux2": ".sh",
		"linux": ".sh", # 파이썬3
	}
	if sys.platform not in osExt:
		print("{0} is not supported yet".format(sys.platform))
	ext = osExt[sys.platform]

	create = os.path.normpath(os.path.abspath(__file__) + "/../create" + ext)

	with TempDir() as d:
		scene = os.path.join(d, "test.blend")
		p = subprocess.Popen([create, scene], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		out, _ = p.communicate()
		if p.returncode != 0:
			print(out)

if __name__ == "__main__":
	TestMain()
