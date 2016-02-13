@echo off
set /p startid=enter the device startid:
set /p endid=enter the device endid:

if %endid% GTR %startid% (for /l %%i in (%startid%,1,%endid%) do start D:\david\LINENIGHT\bat\loadphonenumbers\loadphonenumberupdate.bat %%i&& ping 127.0.0.1 -n 13 > nul)else (for /l %%i in (%endid%,1,%startid%) do start D:\david\LINE\bat\startdevices\startdevice.bat %%i&& ping 127.0.0.1 -n 5 > nul)
