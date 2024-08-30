Please follow the below steps:
1. Run git clone <repository url>
2. create a virtual env
3. activate venv
4. install requirements> pip install requirements.txt
5. run migrations:
python manage.py makemigrations
python manage.py migrate
6. Run app server:
   python manage.py runserver

The app should run on your local at http://127.0.0.1:8000

Please add new user in page: http://127.0.0.1:8000/api/users/

You can check the end points: users/ --> to get and post users
                              users/<id>/-->to view details of specific user
                              users/<id>/update--->to update users data including addtress data as list of dict:
{
    "id": 1,
    "name": "1",
    "email": "1",
    "mobile": "1",
    "addresses": [
        {
            "id": 2,
            "home": "Home 1",
            "address": "Tested",
            "city": "City 1",
            "state": "State 1",
            "pincode": "12345"
        }
{
        "id": 1,
        "home": "test",
        "address": "tested",
        "city": "Blr",
        "state": "ka",
        "pincode": "767676"
    }
    ]
}
                        users/address---> to view/add address



