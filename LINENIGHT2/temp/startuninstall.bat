@echo off
set /p startid=enter the device startid:
set /p endid=enter the device endid:
python D:\\david\\LINENIGHT2\\temp\\uninstallapp.py %startid% %endid%

pause
