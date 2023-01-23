echo "Build Started"
pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "Build End"