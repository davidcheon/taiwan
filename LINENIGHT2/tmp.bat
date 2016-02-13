@echo off
ping 127.0.0.1 -n 5 > null
echo 1
adb shell input tap 464 375
ping 127.0.0.1 -n 2 > null
echo 2
adb shell input tap 555 415
ping 127.0.0.1 -n 5 > null
echo 3
adb shell input tap 464 375
ping 127.0.0.1 -n 2 > null
echo 4
adb shell input tap 407 673
ping 127.0.0.1 -n 26>null
echo 5
adb shell input tap 464 375
ping 127.0.0.1 -n 2 >null
echo 6
adb shell input tap 305 640
ping 127.0.0.1 -n 2 > null
echo 7
adb shell input tap 464 375
ping 127.0.0.1 -n 2 > null
echo over
pause
