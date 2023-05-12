#!/usr/bin/python3
import os, subprocess
from time import sleep

# Clone or pull "mother-repo" and execute setup.sh!
main_repo = "mother-repo"
main_path = os.getcwd
path = os.getcwd() + '/' + main_repo
server_host = "github.com"
git_user = 'voiz80'
first_sleep = 180    ## 180 sec
ping_sleep = 3600    ## 3600 sec / 1hour
sleep_time = 86400   ## 86 400 sec / 24 hours
print(path)
numOfScans = 1

def pinGo(host):
    pingchk = os.system("ping -c 1 " + host + " > /dev/null")
    if pingchk == 0:
        pingchk = True      ## True
    else:
        pingchk = False      ## False
    return pingchk

sleep(first_sleep)
while True:
    ping = pinGo(server_host)
    isExistPath = os.path.exists(path)
    if ping:
        try:
            if isExistPath:
                os.chdir(path)
                status = subprocess.check_output("git pull", shell=True).decode().strip()
                if status == "Already up to date.":
                    print(f"This " + main_repo + ": " + status + " Start Script!")
                    start_without_update_script = subprocess.call("bash setup.sh", shell=True)

                else:
                    print(f"This " + main_repo + ": " + status + " Start Script!")
                    start_update_pull_script = subprocess.call("bash setup.sh", shell=True)

            else:
                try:
                    os.chdir(main_path)
                    gitclone = subprocess.check_output("git clone https://" + server_host + "/" + git_user + "/" + main_repo + ".git", shell=True)
                    print(gitclone)
                    os.chdir(path)
                    start_script = subprocess.call("bash setup.sh", shell=True)
                    print(start_script)
                except:
                    print("Some Clone Filed!!")
        except:
            print("Something error in pull or clone")
    else:
        print(f'Server is Dead')
        sleep(ping_sleep) ## After 1 hour Python service wil be broke and run after 10 sec. Then try ping again!
        break
    if numOfScans == 0:
        break
    else:
        sleep(sleep_time)
