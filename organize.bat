@echo off
for %%i in (*) do (
 if not "%%~ni" == "organize"
 if not "%%~ni" == pdf_quick_split.py"
 (
  md "%%~ni" && move "%%~i" "%%~ni"
 )
)
