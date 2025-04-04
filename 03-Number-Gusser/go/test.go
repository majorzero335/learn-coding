cd %HOMEPATH%
mkdir hello
cd hello
$ go mod init example/hello
go: creating new go.mod: module example/hello
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}