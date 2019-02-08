@echo off
setlocal

if not defined NATSPEAK_PATH call :finddragon
if not defined NATSPEAK_PATH (
  echo Unable to find natspeak.exe. if you are using Dragon NaturallySpeaking please set the environment variable NATSPEAK_PATH to point to your natspeak.exe and try again.
  set WSR=1
  goto :kill
)

if [%1] == [] goto :default
if %1 == 1 (
  set DRAGON=1
  goto :kill
)
if %1 == 2 (
  set WSR=1
  goto :kill
)
:default
set DRAGON=1
set WSR=1

:kill
if defined DRAGON (
  echo Killing Dragon NaturallySpeaking.
  taskkill /IM natspeak.exe /f /s localhost
  taskkill /FI "IMAGENAME eq dgnuiasvr*" /f /s localhost
  taskkill /IM dnsspserver.exe /f /s localhost
  taskkill /IM dragonbar.exe /f /s localhost
)
if defined WSR (
  echo Killing Windows Speech Recognition.
  taskkill /IM sapisvr.exe /f /s localhost
)


:start
timeout /t 1
if defined DRAGON (
  echo Starting Dragon NaturallySpeaking.
  start "" "%NATSPEAK_PATH%"
)
if defined WSR (
  echo Starting Windows Speech Recognition.
  start "" /d %windir%\system32\Speech\SpeechUX %windir%\Speech\Common\sapisvr.exe -SpeechUX
)
timeout /t 1
goto :eof


:finddragon
for /r "%ProgramFiles%\Nuance" %%G in (natspea?.exe) do (
  set NATSPEAK_PATH=%%G
  setx NATSPEAK_PATH "%%G"
)
if not defined ProgramFiles(x86) goto :eof
for /r "%ProgramFiles(x86)%\Nuance" %%G in (natspea?.exe) do (
  set NATSPEAK_PATH=%%G
  setx NATSPEAK_PATH "%%G"
)
goto :eof

endlocal
