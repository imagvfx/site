# encoding: utf-8

import os

def From(pth):
	"""
	From은 씬 경로를 받아 그 경로에 대한 환경변수를 사전 형식으로 반환한다.
	(받아들이는 씬 경로는 DATAROOT에 대한 상대 경로이다.)

	만일 파일 이름에 모든 환경변수 정보가 다 들어있다면 이름을 이용하고,
	그렇지 않다면 경로와 이름을 모두 이용한다.

	받아들인 경로가 유효하지 않다면 모든 키에 빈 값이 들어간 사전이 반환되므로
	이를 이용해 씬 환경변수를 초기화 할 수 있다.

	참고:  https://github.com/imagvfx/site/wiki/경로
	"""
	env = {
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
	}

	pth = os.path.normpath(pth)
	pth = pth.replace("\\", "/")

	name = os.path.basename(pth)
	names = name.split(".")
	if len(names) == 7:
		# 이름에서 환경변수 추출
		# 예) test.CG.0010.fx.main.v001.blend
		show, group, unit, part, task, ver, _ = names
	else:
		# 경로 전체에서 환경변수 추출
		# 예) /show/test/work/CG/0010/wip/fx/main.v001.blend
		if pth.startswith("/"):
			pth = pth[1:]
		pths = pth.split("/")
		if len(pths) < 8:
			return env
		if pths[0] != "show":
			return env
		if pths[2] != "work":
			return env
		if pths[5] != "wip":
			return env
		_, show, _, group, unit, _, part = pths[:7]
		if len(names) != 3:
			return env
		task, ver, _ = names

	env["SHOW"] = show
	env["GROUP"] = group
	env["UNIT"] = unit
	env["PART"] = part
	env["TASK"] = task
	env["VER"] = ver
	env["SHOWDIR"] = os.path.normpath("/show/" + show)
	env["GROUPDIR"] = os.path.normpath("/show/" + show + "/work/" + group)
	env["UNITDIR"] = os.path.normpath("/show/" + show + "/work/" + group + "/" + unit)
	env["PARTDIR"] = os.path.normpath("/show/" + show + "/work/" + group + "/" + unit + "/wip/" + part)
	return env
