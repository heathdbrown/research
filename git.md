# Ubuntu
Add latest version of git

```console
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
```

## Git worktree
https://opensource.com/article/21/4/git-worktree#:~:text=A%20Git%20worktree%20is%20a,and%20on%20a%20different%20branch.

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
