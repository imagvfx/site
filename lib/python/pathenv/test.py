# encoding: utf-8

import pathenv

import os
from collections import namedtuple

def TestFrom():
	Case = namedtuple("case", "label pth want")
	cases = [
		Case(
			label = "work in progress file (valid)",
			pth = "/show/test/work/CG/0010/wip/fx/main.v001.blend",
			want = {
				"SHOW": "test",
				"GROUP": "CG",
				"UNIT": "0010",
				"PART": "fx",
				"TASK": "main",
				"VER": "v001",
				"SHOWDIR": os.path.normpath("/show/test"),
				"GROUPDIR": os.path.normpath("/show/test/work/CG"),
				"UNITDIR": os.path.normpath("/show/test/work/CG/0010"),
				"PARTDIR": os.path.normpath("/show/test/work/CG/0010/wip/fx"),
			},
		),
		Case(
			label = "mixed file separater (valid)",
			pth = "/show\\test\\work/CG/0010/wip/fx\\main.v001.blend",
			want = {
				"SHOW": "test",
				"GROUP": "CG",
				"UNIT": "0010",
				"PART": "fx",
				"TASK": "main",
				"VER": "v001",
				"SHOWDIR": os.path.normpath("/show/test"),
				"GROUPDIR": os.path.normpath("/show/test/work/CG"),
				"UNITDIR": os.path.normpath("/show/test/work/CG/0010"),
				"PARTDIR": os.path.normpath("/show/test/work/CG/0010/wip/fx"),
			},
		),
		Case(
			label = "published file (valid)",
			pth = "/some/other/path/test.CG.0010.fx.main.v001.blend",
			want = {
				"SHOW": "test",
				"GROUP": "CG",
				"UNIT": "0010",
				"PART": "fx",
				"TASK": "main",
				"VER": "v001",
				"SHOWDIR": os.path.normpath("/show/test"),
				"GROUPDIR": os.path.normpath("/show/test/work/CG"),
				"UNITDIR": os.path.normpath("/show/test/work/CG/0010"),
				"PARTDIR": os.path.normpath("/show/test/work/CG/0010/wip/fx"),
			},
		),
		Case(
			label = "unknown path (invalid)",
			pth = "/some/other/path/main.v001.blend",
			want = {
				"SHOW": "",
				"GROUP": "",
				"UNIT": "",
				"PART": "",
				"TASK": "",
				"VER": "",
				"SHOWDIR": "",
				"GROUPDIR": "",
				"UNITDIR": "",
				"PARTDIR": "",
			},
		),
	]
	for c in cases:
		got = pathenv.From(c.pth)
		if got != c.want:
			raise RuntimeError("{0}: want {1}, got {2}".format(c.label, c.want, got))

def TestMain():
	TestFrom()

if __name__ == "__main__":
	TestMain()
