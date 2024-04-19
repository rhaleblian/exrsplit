set PYTHONPATH=
py -3 -m venv venv
call venv\scripts\activate.bat
python setup.py sdist
copy dist\* \\gfs\thr3dcgi_config\repo\3
dir \\gfs\thr3dcgi_config\repo\3
deactivate
