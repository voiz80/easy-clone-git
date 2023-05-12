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
- If ExistPath pull repo and execute "setup.sh"
- Else clone repo and execute "setup.sh"

## Mother Repo - this repo can control many other repos described in own "setup.sh"
```
# variable in easygit.py
main_repo = "mother-repo"
```
Create empty repository with same name like main_repo and commit "setup.sh"