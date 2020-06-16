chcp 65001

set HERE=%~dp0

:: 프로그램(예: 블렌더)에 따라 상대경로를 인식하지 못하는 경우가 있으므로
:: 절대경로로 변환한 씬 경로를 전달한다.
set SCENE="%~f1"

run -envset="%HERE%run.envs" blender --background --python "%HERE%create.py"
