@echo off
set player=D:\\download\\Genymotion\\player.exe
echo device %1 is starting...
%player% --vm-name %1
exit