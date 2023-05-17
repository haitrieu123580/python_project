# python_project

## how to run this project

1. To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

2. That will create a new folder env in your project directory. Next activate it with this command on windows:

```
py -m venv myenv
```
and 

```
./myenv/Scripts/activate 
```

3.Then install the project dependencies with

```
pip install -r requirements.txt
```

4. Then go to folder mysite and makemigrations

```
cd mysite
```

```
py manage.py makemigrations
```

```
py manage.py migrate
```

5. Then create admin account

```
py manage.py createsuperuser 
```

And enter your infor

6.Now you can run the project with this command

```
py manage.py runserver
```