@echo off

setLocal EnableDelayedExpansion

if not exist TextFiles   (mkdir TextFiles)
if not exist SourceFiles (mkdir SourceFiles)
if not exist HeaderFiles (mkdir HeaderFiles)

for /F "tokens=1-4" %%a in (input.txt) do (
    if not exist %%a (mkdir %%a)
    cd %%a
    if not exist %%b (echo 0 > %%b) else ( 
        for /F "tokens=1" %%i in (%%b) do (
            set /a x=%%i+1
            echo !x! > %%b
        )
    )
    if not exist %%c (echo 0 > %%c) else ( 
        for /F "tokens=1" %%i in (%%c) do (
            set /a x=%%i+1
            echo !x! > %%c
        )
    )
    if not exist %%d (echo 0 > %%d) else ( 
        for /F "tokens=1" %%i in (%%d) do (
            set /a x=%%i+1
            echo !x! > %%d
        )
    )
    cd..
    copy /y %%a\*.h    HeaderFiles
    copy /y %%a\*.c    SourceFiles
    copy /y %%a\*.txt  TextFiles
)
