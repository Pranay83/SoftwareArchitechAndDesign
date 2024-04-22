# Hello world - App using Django

Hello world app application is created using DJANGO, tool used for 
creation is Pycharm and it comes pre installed with venv and Django, and python hence no need to install separately.

## Start webapp

- on command prompt of pycharm tool, acticate venv scripts using venv\scripts\activate
- then start proejct by giving django-admin startproject project_Name
- create django application using django-admin startapp App_Name
- Add the new app name to installed apps on settings.py file that can be found on the project folder
- Then copy urls.py file from the project folder and define function
  to create HTTP request and response, of own mesaage
- on urls.py file set the path of helloworld that is defined in HTTP response creation part to access urls


## Accessing Hello world app on browser

- To access hello world applicaiton on browser oepn terminal
- Navigate to the project folder
- Run the command "python manage.py runserver"
- Server starts running and response can be captured form the browser
- Copy the URL [""http://127.0.0.1:8000/"] in any browser to see HTTP response.





