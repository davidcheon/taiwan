@echo off
set killcmd=taskkill /f /t /im player.exe
%killcmd%
set vboxcmd=taskkill /f /t /im VBoxHeadless.exe
%vboxcmd%
set adbcmd=taskkill /f /t /im adb.exe
%adbcmd%