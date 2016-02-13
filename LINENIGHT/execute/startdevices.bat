@echo off
set /p startid=enter the device startid:
set /p endid=enter the device endid:

for /l %%i in (%startid%,1,%endid%) do start D:\david\LINENIGHT\bat\startdevices\startdevice.bat %%i&& ping 127.0.0.1 -n 10 > nul
ping 127.0.0.1 -n 5> null
python D:\\david\\LINENIGHT\\scripts\\pushfiletodevice.py %startid% %endid%
pause
