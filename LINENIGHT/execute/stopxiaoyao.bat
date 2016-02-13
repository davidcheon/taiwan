@echo off
set killadb=taskkill /f /t /im adb.exe
rem %killadb%
set killmanage=taskkill /F /im MemuManage.exe
%killmanage%
set killsvc=taskkill /F /im MEmuSVC.exe
%killsvc%
set killheadless=taskkill /F /im MEmuHeadless.exe
%killheadless%
set killcmd=taskkill /F /t /im MEmu.exe
%killcmd%
set killfault=taskkill /F /im WerFault.exe
%killfault%
