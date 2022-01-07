

To run the project install python version 3.8 and higher

Clone the repository:
```bash
git clone https://github.com/azazellooo/employees.git
```

After cloning, go to the cloned folder, create virtual environment and activate it:
```bash
python3 -m virtualenv -p python3 venv
source venv/bin/activate
```
install dependencies:
```bash
pip install -r requirements.txt
```

create .env file and fill up environment variables DATABASE_NAME, DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD

apply migrations - go to "employees_app" folder and run
```bash
./manage.py migrate
```
