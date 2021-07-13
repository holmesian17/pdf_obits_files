@echo off
for /f "eol=: delims=" %%i in ('dir /b /a-d *^|findstr /live ".bat .txt"') do (
 if not "%%~ni" == "organize"
 (
  md "%%~ni" && move "%%~i" "%%~ni"
 )
)
