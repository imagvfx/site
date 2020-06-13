# imagvfx

imagvfx (이마그)는 상상속 vfx 회사입니다.

site는 그 중 git으로 관리될 수 있는 코드와 설정 부분을 담고 있습니다.


### 개발 환경

site를 개발하기 위해서는 [Go](https://golang.org)와 [Python](https://python.org)이 필요합니다.


### 규약 기반의 개발

코드는 규약에 따라서 작성됩니다.
자세한 정보는 [위키](https://github.com/imagvfx/site/wiki)를 살펴보세요.


### 사용자

사용자 컴퓨터에는 어떤 프로그래밍 언어도 설치되지 않았다고 가정하고 코드를 작성해주세요.
다만 특정 프로그램 안에서 돌아가는 코드는 그 프로그램이 가지고 있는 환경을 따른다고
생각하시면 됩니다.

### 설치

리눅스에서의 설치를 가정한 예 입니다.

```
git clone https://github.com/imagvfx/site
cd site
export SITEROOT="$PWD" # .bashrc 등에 넣을 때는 절대경로를 사용해주세요.
export PATH=$PATH:"$SITEROOT/bin" # 사이트의 bin 디렉토리를 PATH에 등록해주세요.
go run init.go
```

### 테스트

```
cd "$SITEROOT"
go test ./...
```
