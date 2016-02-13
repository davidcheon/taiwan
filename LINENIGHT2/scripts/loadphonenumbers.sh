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
	sleep 2
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
#------1:tongbu_time-------
	#guanggao
	#input tap 464 375
	#sleep 1
	echo "press start TongBu button"
	input tap 555 415
	sleep 5
	echo "press first step ok button"
	#input tap 464 375
	#sleep 1
	input tap 407 673
	sleep $1
	#input tap 464 375
	#sleep 2
	echo "press others else"
	input tap 305 640
	sleep 2
	#input tap 464 375
	#sleep 1
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
	input tap 300 367
	sleep 2
}
clickmyappbackup(){
#----------1::deviceid 2:rotatetimes 3:myapp_delete_time 4:myapp_load_time -----------------
#-------enter the app--
	echo "press myapp"
	clickmyapp
	echo "press myapp again"
	input tap 300 367
	sleep 2
	echo "press delete button"
#	press deletebutton
	input tap 570 415
	sleep 6
	echo "clickmyapp again"
	clickmyapp
	echo "press delete button again"
	input tap 570 415
	sleep $3
	echo "press select xls button"
#	select xls button
	input tap 300 255
	sleep 2
	echo "enter the pathname"

#	enter the pathname
	input text /sdcard/Download/AAAA/$2/$1
	sleep 2
	echo "press search button"
#	press start search button	
	input tap 300 175
	sleep 2
	
#	select searched first result
	echo "select file"
	input tap 300 235
	sleep 2
#	start load button
	echo "start loading...."
	input tap 300 365
	sleep $4
#	back myapp	to home
#	input keyevent 3
#	sleep 2
#	input keyevent 4
#	sleep 2
}
updatecontactsinline(){
#----------1:flag 2:line_tongbu_time-----------------
	echo "backtohome"
	backtohome
	echo "press Line app"
	clicklineapp $1
	echo "order first"
	orderfirst
	echo "press <...>"
	clickdotdotdot
	echo "press addfriends button"
	clickaddfriends
	echo "enter TongBu action"
	clicktongbu $2
	echo "TongBu action over"
	#back x 2
	input keyevent 4
	sleep 1
	input keyevent 4
	sleep 1
	input keyevent 4
	sleep 2
	input keyevent 4
	sleep 1
	input keyevent 4
	sleep 1
	input keyevent 4
	sleep 2
	
#	input tap 85 178
#	sleep 3
#	orderfirst
	#press chatbutton
#	input tap 180 170
#	sleep 2
	
	#tomain
#	input keyevent 3
#	sleep 2
}
loadstart(){
#----------1:device 2:deviceid 3:rotatetimes 4:myapp_delete_time 5:myapp_load_time 6:line_tongbu_time-----------------
	backtohome
	echo "backtohome over"
	flag=1	
	for file in $(ls /sdcard/Download/xls/$3/$2)
	do
		rm -rf /sdcard/Download/AAAA/$3/$2/*
		mv /sdcard/Download/xls/$3/$2/${file} /sdcard/Download/AAAA/$3/$2
		
		echo "before clickmyapp"
		clickmyappbackup $2 $3 $4 $5
		echo "after clickmyapp"
		updatecontactsinline $flag $6
		flag=$(($flag+1))
		echo "<$3 Time>${file} added succeed.[MEmu_$2]"
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
	#input keyevent 4
	#sleep 1
	#input keyevent 4
	#sleep 1
	#input keyevent 4
	#sleep 1
	#input keyevent 4
	echo "-------------------------"
	echo "Device:$1"
	echo "DeviceID:$2"
	echo "RotationTime:$3"
	echo "Myapp_delete_time:$4"
	echo "Myapp_load_time:$5"
	echo "Line_tongbu_time:$6"
	echo "------------------------"
	sleep 5
}
#---------------------start------------------------
echo "<$3 Time>[MEmu_$2] start loading.......... "
echo
echo "init"
initialize $1 $2 $3 $4 $5 $6
echo "init over"
#----------1:device 2:deviceid 3:rotatetimes 4:myapp_delete_time 5:myapp_load_time 6:line_tongbu_time-----------------
loadstart $1 $2 $3 $4 $5 $6
sleep 5

