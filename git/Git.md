## Installing Git

### Ubuntu
Add latest version of git

```console
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
```

## Git basics

### Git branch rename
```bash
git branch -m master main
```

## Git Credential Manager

```bash

git-credential-manager github login
```

## Git worktree

```console
$ git branch | tee
* dev
trunk
```

```console
$ git worktree add -b hotfix ~/code/hotfix trunk
Preparing ../hotfix (identifier hotfix)
HEAD is now at 62a2daf commit
```

```
$ cd ~/code/hotfix
$ sed -i 's/teh/the/' hello.txt
$ git commit --all --message 'urgent hot fix'
```

```console
$ git push origin HEAD
$ cd ~/code/myproject
```

```
git worktree list
/home/seth/code/myproject  15fca84 [dev]
/home/seth/code/hotfix     09e585d [master]
```

## Configuration
```
#.gitmessage.txt
<type>[optional scope]: <description>

[optional body]

[optonal footer(s)]
ref: https://www.conventionalcommits.org/en/v1.0.0/#specification
[Ticket: X]

Example:

fix: prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: Z
Refs: #123
```

```bash
git config --global user.name "FirstName LastName"
git config --global user.email email@dot.com
git config --global core.editor vim
git config --global commit.template ~/.gitmessage.txt
```

References
- [So You Think You Know Git - FOSDEM 2024 Scott Chacon](https://www.youtube.com/watch?v=aolI_Rz0ZqY)
- [Git Worktree - OpenSource.com](https://opensource.com/article/21/4/git-worktree#:~:text=A%20Git%20worktree%20is%20a,and%20on%20a%20different%20branch.)
- [Git Worktrees - Mtklad 2024-07-25](https://matklad.github.io/2024/07/25/git-worktrees.html)
- [Git Worktree Best Practices and Tools - ChristopherA - 2024-02-06](https://gist.github.com/ChristopherA/4643b2f5e024578606b9cd5d2e6815cc)
