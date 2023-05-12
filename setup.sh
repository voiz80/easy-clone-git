#!/bin/bash
#Script For clone to many Git Repo. Author:idimitrov

echo "---Start info from mother-repo---"

#ADD REPO FOR CLONE
repo_name1="/python-chatgpt-automation"
repo_name2="/github-actions-js"

main_paths="$PWD"
paths=("$main_paths$repo_name1" "$main_paths$repo_name2") #ADD VARIABLE FOR LOOP
git_user=("voiz80")
host="github.com"


for item in ${paths[@]};
    do
    if [ -d "${item}" ];
    then
	    cd "${item}"

	    echo "----------------------------------------"
	    echo "${item}"
	    echo "----------------------------------------"
	    status=$(sudo git pull) #check for local update!
	    if [[ $status == *"Already up to date."* ]];
	    then
	        echo "Local Repo is Already up to date, no git pull needed!";
	    else
		    echo "We have Pull Update! Start install packages from script ..." && bash setup.sh  || echo "git pull failed, please see log." exit; #git pull - update repo!
	    fi
	    cd ..

    else 
        echo 'Start Git clone missing repo...'
        cd ${main_paths}
        [[ "$item" =~ ([^\/]+$) ]] && echo "${BASH_REMATCH[1]}" 
        
        sudo git clone https://${host}/${git_user}/"${BASH_REMATCH[1]}".git && cd "${item}" &&
        echo 'Start install packages from script' && bash setup.sh &&
        echo 'Finish! All Git Clone Repo is created!'
    fi
done
echo "---End info from mother-repo---"
