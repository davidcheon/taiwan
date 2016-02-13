@echo off
set /p startid=enter the device startid:
set /p endid=enter the device endid:
python D:\\david\\LINENIGHT\\bat\\startdevices\\startxiaoyaodeviceupdate2.py %startid% %endid%
rem python D:\\david\\LINENIGHT\\bat\\startdevices\\startxiaoyaodeviceupdate2.py %startid% %endid% >> D:\\david\\LINENIGHT\\history\\%Date:~0,4%%Date:~5,2%%Date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%.txt 2>>&1
rem python D:\\david\\LINENIGHT\\bat\\startdevices\\startxiaoyaodevice.py %startid% %endid%

pause
