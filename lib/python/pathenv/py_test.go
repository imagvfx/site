package main

import (
	"fmt"
	"os/exec"
	"testing"
)

func TestPython(t *testing.T) {
	out, err := exec.Command("python", "test.py").CombinedOutput()
	if err != nil {
		t.Fatal(string(out))
	}
	fmt.Print(string(out))
}
