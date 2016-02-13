@echo off
set /p startid=enter the device startid:
set /p endid=enter the device endid:

python D:\\david\\LINENIGHT\\bat\\startdevices\\startxiaoyaodevice.py %startid% %endid%

pause