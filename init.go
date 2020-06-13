// init.go는 사이트 개발에 필요한 파일을 다운로드 받는 등 초기 설정을 돕습니다.

package main

import (
	"errors"
	"io"
	"log"
	"net/http"
	"os"
)

func main() {
	log.SetFlags(0)
	root := os.Getenv("SITEROOT")
	if root == "" {
		log.Fatal("please set SITEROOT environment variable")
	}
	setupFuncs := []func() error{
		mkdirBin,
		installRun,
	}
	for _, fn := range setupFuncs {
		err := fn()
		if err != nil {
			log.Fatal(err)
		}
	}
}

// mkdirBin은 사이트 루트에 bin 디렉토리가 존재하지 않으면 생성합니다.
func mkdirBin() error {
	err := os.Mkdir(os.Getenv("SITEROOT")+"/bin", 0755)
	if err != nil && !errors.Is(err, os.ErrExist) {
		return err
	}
	return nil
}

// installRun은 사이트의 bin 디렉토리에 리눅스/윈도우즈용 run 실행 파일을 다운로드 받습니다.
func installRun() error {
	dstd := os.Getenv("SITEROOT") + "/bin"
	if err := download("https://github.com/studio2l/run/releases/download/v0.2/run", dstd+"/run", 0755); err != nil {
		return err
	}
	if err := download("https://github.com/studio2l/run/releases/download/v0.2/run.exe", dstd+"/run.exe", 0755); err != nil {
		return err
	}
	return nil
}

// download는 특정 url의 데이터를 원하는 경로에 파일로 다운로드 받습니다.
// 다운로드 받을 파일이 이미 존재한다면 덮어쓰지 않고 넘어갑니다.
func download(from, to string, perm os.FileMode) error {
	_, err := os.Stat(to)
	if err == nil {
		log.Printf("download skipped: %q exists", to)
		return nil
	} else if !os.IsNotExist(err) {
		return err
	}
	resp, err := http.Get(from)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	out, err := os.OpenFile(to, os.O_CREATE|os.O_WRONLY, perm)
	if err != nil {
		return err
	}
	defer out.Close()
	_, err = io.Copy(out, resp.Body)
	return err
}
