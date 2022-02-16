Article in the references area looks at multiple parsing libraries with sample code.

- Argparse
- DocOpt
- Click
- Invoke* as a bonus

Summary:
- Argparse: built-in handles several cases and is popular.
- DocOpt: Documentation focused, opionionated on how to build the tools.
- Click: Decorator focused but clean
- Invoke: it can do the job.

I prefer docopt as I think I like writing the documentation based approach, although I also tend to try different ones. ArgParse and DocOpt I always find I deal with handling options with if statements. The article showcases using the built-in 'func' option in Argparse to directly call a function that can handle the options.

# Reference
- [RealPython Commmand line Parsing Libraries](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/#:~:text=Argparse%20To%20add%20an%20argument%20to%20a%20subcommand,the%20set_defaults%20method%20to%20set%20a%20default%20function.)
