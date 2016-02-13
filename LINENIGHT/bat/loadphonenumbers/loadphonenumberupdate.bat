@echo off
rem ---------start--------------------
rem del /F /S /Q D:\david\LINE\xls\1
rem copy D:\david\LINE\sources\ D:\david\LINE\xls\1
set deviceid=%1
set /a port=%deviceid%*100+19004
set device=127.0.0.1:%port%
set cmd1="su -c '[ ! -d /storage/sdcard1/Download/AAAA/%deviceid% ] && mkdir -p /storage/sdcard1/Download/AAAA/%deviceid%'"
adb -s %device% shell %cmd1%
set cmd2="su -c '[ ! -d /storage/sdcard1/Download/xls/%deviceid% ] && mkdir -p /storage/sdcard1/Download/xls/%deviceid%'"
adb -s %device% shell %cmd2%
set cmd3="su -c '[ ! -d /storage/sdcard1/Download/Execute/%deviceid% ] && mkdir -p /storage/sdcard1/Download/Execute/%deviceid%'"
adb -s %device% shell %cmd3%

rem ###############################
set cmd4="su -c '[ ! -d /storage/sdcard1/Download/Execute/%deviceid% ] && mkdir -p /storage/sdcard1/Download/Execute/%deviceid%'"
adb -s %device% shell %cmd4% > D:\david\LINE\temp\temp%deviceid%.txt
FIND /C "xls" D:\david\LINE\temp\temp%deviceid%.txt> D:\david\LINE\temp\result%deviceid%.txt
FOR /F "tokens=3,3 delims= " %%i in (D:\david\LINE\temp\result%deviceid%.txt) do (set lv_cnt=%%i)
if %lv_cnt% equ 0 (adb -s %device% push D:\\david\\LINE\\xls\\%deviceid% /storage/sdcard1/Download/xls/%deviceid%)
del D:\david\LINE\temp\result%deviceid%.txt
del D:\david\LINE\temp\temp%deviceid%.txt

rem //adb -s 127.0.0.1:19105 push D:\\david\\LINE\\xls\\1 /storage/sdcard1/Download/xls/1

adb -s %device% push D:\\david\\LINE\\scripts\\loadphonenumbers.sh /storage/sdcard1/Download/Execute/%deviceid%

adb -s %device% shell sh /storage/sdcard1/Download/Execute/%deviceid%/loadphonenumbers.sh %device% %deviceid%

del /F /S /Q D:\david\LINE\xls\%deviceid%

rem //python D:\david\LINE\scripts\savecontactmids.pyc "test1@zgi3p8z.com" "abcd123456" "127.0.0.1:19105"
