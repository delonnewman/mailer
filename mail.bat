@echo off

set drive=%~dp0
set drivep=%drive%
if #%drive:~-1%# == #\# set drivep=%drive:~0,-1%

set PATH=%drivep%\Python27;%PATH%
rem env variables
set TERM=dumb

python "%drivep%\mail.py" %*
