# Index
* [Cli Apps](#Cli-Apps)
    * [Cobra basics](#Cobra-basics)
        * [Default cobra structure](#Default-cobra-structure)
        * [Cobra subcommand structure](#Cobra-subcommand-structure)
        * [Cobra subcommand tied to parent command](#Cobra-subcommand-tied-to-parent-command)
        * [Cobra with subcommands in different packages](#Cobra-with-subcommands-in-different-packages)
        * [Cobra with subcommands with subsubcommands in different packages](#Cobra-with-subcommands-with-subsubcommands-in-different-packages)
    * [CLI with Standard library](#CLI-with-Standard-library)
    * [Cli with FlagSets command-line subcommands](#Cli-with-FlagSets-command-line-subcommands)
* [Logging](#Logging)
  * [Standard Library slog](#Standard-Library-slog)
  * [Manual Log Prefixes](#Manual-Log-Prefixes)
* [Tools](#Tools)
* [References](#References)
***

# Cli Apps
- [Cobra, Viper, Structs](https://github.com/benchkram/cli-utils/blob/main/base/cli/cmd_root.go)
- [Golang Ultimate Config for golang apps](https://benchkram.de/blog/dev/ultimate-config-for-golang-apps)
- [GoLang Cli with standard library](https://www.rapid7.com/blog/post/2016/08/04/build-a-simple-cli-tool-with-golang/)
- [CharmBracelet libraries for pretty TUI/cli apps](https://github.com/charmbracelet)
- [GoLang CLI Apps](https://github.com/heathdbrown/research/issues/76)

```bash
go run main.go

go build main.go
```

## Cobra basics

The following steps will install cobra-cli which is a tool that will scaffold a cobra cli project by default.

```bash
go install github.com/spf13/cobra-cli@latest
mkdir <tool>
go mod init github.com/<user>/<tool>
cobra-cli init
# basics
cobra-cli add <subcommand>
# basic; subcommand in same folder cmd/
cobra-cli add <subcommand> -p <parentsubcommand>
```

### Default cobra structure

`tool -h`

```bash
# cobra-cli init
├── cmd
│   └── root.go
├── go.mod
├── go.sum
├── LICENSE
└── main.go
```

### Cobra subcommand structure

`tool subcommand`

```bash
# cobra-cli add subcommand
├── cmd
│   ├── root.go
│   └── subcommand.go
├── go.mod
├── go.sum
├── LICENSE
└── main.go
```

### Cobra subcommand tied to parent command

`tool subcommand subsubcommand`

```bash
# cobra-cli add subsubcommand -p subcommand
├── cmd
│   ├── root.go
│   ├── subcommand.go
│   └── subsubcommand.go
├── go.mod
├── go.sum
├── LICENSE
└── main.go
```

### Cobra with subcommands in different packages

`tool lb`

1. make the 'rootCmd' in root.go Exportable = 'RootCmd`
2. create a folder for your package `mkdir lb`
3. create the subcommand `cobra-cli add lb` = `cmd/lb.go`
4. move subcommand into package = `mkdir cmd/lb`
5. change the subcommand package name from `cmd` to `subcommand` or whatever you want the package to be called
6. Add the 'cmd' package as an import for the subcommand, Update the subcommand to be exportable and update the init function of the new subcommand to have the proper 'rootCmd'
    ```go
    // change package from cmd to lb
    package lb

    import (
        // Add cmd package import
        "github.com/<tool>/cmd"
        "github.com/spf13/cobra"
    )

    // make the LbCmd exportable
    var LbCmd = &cobra.Command{
        	Use:   "lb",
	        Short: "A brief description of your command",
	        Long: `A longer description that spans multiple lines and likely contains examples
                and usage of using your command. For example:

                Cobra is a CLI library for Go that empowers applications.
                This application is a tool to generate the needed files
                to quickly create a Cobra application.`,
        	Run: func(cmd *cobra.Command, args []string) {
	        	fmt.Println("lb called")
        	},
     }

    func init(){
       // Use the exported and imported cmd/RootCmd and attach the subcommand LbCmd
       cmd.RootCmd.AddCommand(LbCmd)
    }
    ```

```bash
├── cmd
│   ├── lb
│   │   ├── diff.go
│   │   └── lb.go
│   ├── root.go
│   ├── switch
│   │   └── switch.go
│   └── version.go
├── go.mod
├── go.sum
├── main.go
```

### Cobra with subcommands with subsubcommands in different packages

There is a subtle difference in what was created beforehand, with just subcommand and then moving it to the new package layout and the steps with exporting etc. with this type of subsubcommand. The main difference being you only need to put the generated command in the package folder, update the package name, and attach the subcommand for your new command.

`tool lb diff`

```bash
cobra-cli add diff -p lb
```

This outputs the 'diff' command under the `cmd/` folder, by default.

Move this diff.go file under the 'lb' package and then edit the package name, and the exported subcommand.

```go
package lb

import (
	"fmt"

	"github.com/spf13/cobra"
)

// diffCmd represents the diff command
var diffCmd = &cobra.Command{
	Use:   "diff",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("diff called")
	},
}

func init() {
        // Attach to exported subcommand
	LbCmd.AddCommand(diffCmd)
}

```

## CLI with Standard library

- From Rapid7

```go
package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	fmt.Println("packat summary")
	textPtr := flag.String("text", "", "Text to parse.")
	metricPtr := flag.String("metric", "chars", "Metric {chars|words|lines};.")
	uniquePtr := flag.Bool("unique", false, "Measure unique values of a metric.")
	flag.Parse()

	if *textPtr == "" {
		flag.PrintDefaults()
		os.Exit(1)
	}

	fmt.Printf("textPtr: %s, metricPtr: %s, uniquePtr: %t\n", *textPtr, *metricPtr, *uniquePtr)
}
```

Example output from Go code:

```bash
go run main.go -text "test"
packat summary
textPtr: test, metricPtr: chars, uniquePtr: false
```

## Cli with FlagSets command line subcommands
- https://gobyexample.com/command-line-subcommands

```go
package main

import (
    "flag"
    "fmt"
    "os"
}

func main() {
    foocmd := flag.NewFlagSet("foo", flag.ExitOnError)
    fooEnable := fooCmd.Bool("enable", false, "enable)
    fooName := fooCmd.String("name", "", "name")

    barcmd := flag.NewFlagSet("bar", flag.ExitOnError)
    barLevel := barCmd.Int("level", 0, "level")

    if len(os.Args) < 2 {
        fmt.Println("expected 'foo' or 'bar' subcommands")
        os.Exit(1)
    }

    switch os.Args[1] {
    case "foo":
        fooCmd.Parse(os.Args[2:])
        fmt.Println("subcommand" 'foo'")
        fmt.Println("   enable:", *fooEnable)
        fmt.Pirntln("   name:", *fooName)
        fmt.Println("   tail:", fooCmd.Args())
    case "bar":
        barCmd.Parse(os.Args[2:])
        fmt.Println("subcommand" 'bar'")
        fmt.Println("   level:", *barLevel)
        fmt.Println("   tail:",  barCmdArgs())
    default:
        fmt.Println("expected 'foo' or 'bar' subcommands")
        os.Exit(1)
    }
}
```
output:

```go
$ go build command-line-subcommands.go 

$ ./command-line-subcommands foo -enable -name=joe a1 a2
subcommand 'foo'
  enable: true
  name: joe
  tail: [a1 a2]

$ ./command-line-subcommands bar -level 8 a1
subcommand 'bar'
  level: 8
  tail: [a1]

$ ./command-line-subcommands bar -enable a1
flag provided but not defined: -enable
Usage of bar:
  -level int
        level
```
# Logging
- https://www.delftstack.com/howto/go/golang-log-levels/#:~:text=go%20get%20%22github.com/Sirupsen/logrus%22.%20Logrus%20provides%20the%20seven%20log%20levels,%20which
- https://stackoverflow.com/questions/16895651/how-to-implement-level-based-logging-in-golang

## Standard Library slog

```go
package main

import "log/slog"

func main() {
    slog.Info("hello")
    slog.Warn("hello")
    slog.Error("hello")
}
```

```bash
2023/08/09 20:05:49 INFO hello
2023/08/09 20:05:49 WARN hello
2023/08/09 20:05:49 ERROR hello
```

## Manual Log Prefixes
```go
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

var (
	Warning_Level *log.Logger
	Info_Level    *log.Logger
	Debug_Level   *log.Logger
	Error_Level   *log.Logger
)

func init() {
	file, err := os.OpenFile("Demo_logs.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		log.Fatal(err)
	}

	Info_Level = log.New(file, "INFO: ", log.Ldate|log.Ltime|log.Lshortfile)
	Warning_Level = log.New(file, "WARNING: ", log.Ldate|log.Ltime|log.Lshortfile)
	Debug_Level = log.New(file, "Debug: ", log.Ldate|log.Ltime|log.Lshortfile)
	Error_Level = log.New(file, "ERROR: ", log.Ldate|log.Ltime|log.Lshortfile)
}

func main() {
	Info_Level.Println("Loading the application.")
	Info_Level.Println("Loading taking time.")
	Warning_Level.Println("There is warning.")
	Debug_Level.Println("Here is debugging information.")
	Error_Level.Println("An Error Occured.")

	// read the log file
	data, err := ioutil.ReadFile("Demo_logs.txt")

	if err != nil {
		log.Panicf("failed reading data from file: %s", err)
	}
	fmt.Printf("\nThe file data is : %s", data)
}
```


# Tools
- [Json to Go Structs](https://mholt.github.io/json-to-go/)

```go
	var u User = User{
		Name:                 "Bob",
		Email:                "bob@testemail.local",
		LoginAccountGroup:    LoginAccountGroup{Aid: 12345},
		AccountGroupRoles:    []AccountGroupRoles{AccountGroupRoles{
			AccountGroup: AccountGroup{
				Aid: 0,
			},
			Roles:        []Roles{Roles{
				RoleID: 0,
			}},
		}},
		AllAccountGroupRoles: []AllAccountGroupRoles{AllAccountGroupRoles{
			RoleID: 0,
		}},
	}
```

# References
- https://gobyexample.com/
- https://go.dev/doc/devel/release
- https://snyk.io/advisor/packages/golang/popular
- [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests)
- [GoLang CLI API Wrapper](http://blog.hellonico.info/posts/golang/jquants/#using-the-library-from-an-external-program)
- [Github Style Guide for CLI apps](https://github.com/cli-guidelines/cli-guidelines)
- [Learning Go Book (code repos)](https://github.com/learning-go-book-2e/ch03)
- [GoLang Best Practices](https://medium.com/@golangda/golang-quick-reference-top-20-best-coding-practices-c0cea6a43f20)
- [Youtube Cobra Example from SkunkWorks](https://github.com/cloud-native-skunkworks/toolbox-cli-example/blob/main/cmd/net/ping.go)
- [Youtube Blueprint example](https://github.com/Melkeydev/go-blueprint/tree/main)
- [Go Articles](https://go.dev/doc/articles/wiki/)
- [Gophercises](https://gophercises.com/)
- [Gophercises Github](https://github.com/gophercises)
- [Grafana Web Services Overview](https://grafana.com/blog/2024/02/09/how-i-write-http-services-in-go-after-13-years/)
- [Awesome Go list of Go libraries](https://github.com/avelino/awesome-go)
- [GoLang with Pipes](https://zetcode.com/golang/pipe/)
- [Idiomatic Go tells a Story - Kaylyn Gibilterra](https://www.youtube.com/watch?v=iiIL3LbAFWk)
- [Effective Go](https://go.dev/doc/effective_go)
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
- [Build Interactive CLI App with Go Cabra Promptui](https://divrhino.com/articles/build-interactive-cli-app-with-go-cobra-promptui/)