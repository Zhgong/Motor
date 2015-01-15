@echo off

set WaitTime=2
set COMMAND=python C:\Users\gong\Scripts\serialscan.py

:Loop
	cls
	echo repeat %COMMAND% : every %WaitTime% s		%DATE%	%TIME%
	%COMMAND%
	echo off 
	timeout /t %WaitTime%
goto Loop