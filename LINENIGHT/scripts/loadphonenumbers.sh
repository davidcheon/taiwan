#!/bin/bash
usage(){
	echo $"Usage: device"
}
clicklineapp(){
	input tap 85 178
	if (($1==1))
		then
			sleep 6
		else
			sleep 4
	fi
}
backtohome(){
	input keyevent 3
	sleep 1
}

orderfirst(){
	input tap 55 175
	input tap 55 175
	sleep 2
}

clickbackupapp(){
	input tap 120 690
	sleep 2
}
clickeditbutton(){
	input tap 560 80
	sleep 2
	input tap 400 245
	sleep 2

}
clicktongbu(){
	#guanggao
	input tap 463 417
	sleep 1
	input tap 555 415
	sleep 2
	input tap 407 673
	sleep 30
	input tap 463 417
	sleep 2
	input tap 305 640
	sleep 2
}
clickdotdotdot(){
	input tap 540 175
	sleep 2
	}
clicksettingbutton(){
	input tap 300 270
	sleep 2
}
swipeandclickfriendsbutton(){
	input swipe 300 500 300 200
	sleep 2
	input tap 300 990
	sleep 2
}
clickaddfriends(){
	input tap 97 283
	sleep 2
	input tap 565 82
	sleep 2
}
clickmyapp(){
	input tap 300 400
	sleep 2
}
clickmyappbackup(){
#-------enter the app--
	clickmyapp
#	press deletebutton
	input tap 300 415
	sleep 45
#	select xls button
	input tap 300 255
	sleep 2

#	enter the pathname
	input text /sdcard/Download/AAAA/$1
	sleep 2
#	press start search button	
	input tap 300 175
	sleep 2
	
#	select searched first result
	input tap 300 235
	sleep 2
#	start load button
	input tap 300 365
	sleep 85
#	exit myapp	
	input keyevent 4
	sleep 2
	input keyevent 4
	sleep 2
}
updatecontactsinline(){
	backtohome
	clicklineapp $1
	orderfirst
	clickdotdotdot
	clickaddfriends
	clicktongbu
	#back x 2
	input keyevent 4
	sleep 2
	input keyevent 4
	sleep 2
	input keyevent 4
	sleep 1
	input keyevent 4
	sleep 1
	input keyevent 4
	sleep 1
	input keyevent 4
	sleep 1
	
}
loadstart(){
	backtohome
	flag=1	
	for file in $(ls /sdcard/Download/xls)
	do
		rm -rf /sdcard/Download/AAAA/*
		mv /sdcard/Download/xls/${file} /sdcard/Download/AAAA/
		

		clickmyappbackup
		
		updatecontactsinline $flag
		flag=$(($flag+1))
		echo "${file} added succeed.[MEmu_$2]"
	done
    # clicklineapp 
	input tap 85 178
	sleep 3
	orderfirst
	rm -rf /sdcard/Download/AAAA/*
	rm -rf /sdcard/Download/xls/*
	 #rm -rf /sdcard/Download/Execute/*
#	 clicklineapp

}
function initialize(){
	input keyevent 4
	sleep 2
	input keyevent 4
	sleep 2
	input keyevent 4
	sleep 2
	input keyevent 4
	sleep 2
}
#---------------------start------------------------
echo "[MEmu_$2] start loading.......... "

initialize
loadstart $1 $2


