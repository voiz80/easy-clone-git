# easy-clone-git
Python service clone git or pull git automaticily. Work on Linux!
### So i controlled 1200 Ubuntu machines this way!!!

## Getting started! Start service
```
git config --global http.sslverify "false"
git clone https://github.com/voiz80/easy-clone-git.git
cd easy-clone-git/
cp easygit.service /lib/systemd/system/
sudo systemctl enable easygit.service
sudo systemctl start easygit.service
```
## Info easygit.py
- Sleep 180 sec
- Check server_host alive. If not check again after ping_sleep
- If ExistPath pull repo and execute "setup.sh". Allways! Why we might have updates in the repo described in "mother-repo" --> setup.sh
- Else clone repo and execute "setup.sh"

## Mother Repo - this repo can control many other repos described in own "setup.sh"
```
# variable in easygit.py
main_repo = "mother-repo"
```
Create empty repository with same name like main_repo and commit "setup.sh"
```
repo_name1="/<add your name repo>"
repo_name2="/<add your name repo>"
# etc.
```
## In outher repo may be other setup.sh scripts with some bash commands.