#!/bin/bash
set -e

export HERE=$(dirname $(realpath "${BASH_SOURCE}"))

# 프로그램(예: 블렌더)에 따라 상대경로를 인식하지 못하는 경우가 있으므로
# 절대경로로 변환한 씬 경로를 전달한다.
run -envset="$HERE/run.envs" blender "$(realpath $1)"
