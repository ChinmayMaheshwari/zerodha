# zerodha
Zerodha Python task

Prerequisites:
  1. python3,pip3
  2. Redis server installed and running

Setup :
  1. Create a virtual enviroment (Optional).
  2. pip3 install -r requirements.txt.
  3. Add following to cronttab -e "0 18 * * * python path/to/script/script.py" (For running script everyday at 18:00).
  4. python script.py (Optinal if running first time).
  5. Run server using python manage.py runserver.
 
Check api working at http://127.0.0.1:8000/api/ 
Live Working on : http://ec2-3-19-141-59.us-east-2.compute.amazonaws.com/ (AWS EC2).
