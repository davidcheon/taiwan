@echo off
set /p startid=enter the from computer id:
set /p endid=enter the end computer id:
set /p filenames=enter the filenames('+'):
python D:\\david\\LINENIGHT2\\temp\\copyfilestoremote.py %startid% %endid% %filenames%
pause
