REM    Windows batch script to run 1+ Python program/scripts, sequentially, within their virtual environment. This can be called from Windows Task Scheduler.

set original_dir=%CD%
set venv_root_dir=C:\Users\Clarissa\anaconda3\

cd %venv_root_dir%

call %venv_root_dir%\Scripts\activate.bat

cd "C:\Users\Clarissa\Documents\Datasets\webscraping_project_01"
python webscraping_03.py


call %venv_root_dir%\Scripts\deactivate.bat

cd %original_dir%

exit /B 1

