echo "Build Started"
ls
mkdir staticfiles_build
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "Build End"