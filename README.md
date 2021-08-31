# EmotionsOnPage

Project made out for the degree of engineering degree in software development

## Members:

-   Tania Citlali Calderon Perez -> Backend Developer
-   Diana Yazmin Camacho Vazquez -> Frontend Developer
-   Yadira Hernandez Hernandez -> FullStack Developer
-   Jose Ricardo Delgadillo Maravilla -> Backend Developer/Database administrator - ricardo.madelga@gmail.com

## For the project we are using:

-   Django
-   Bootstrap
-   Postgre SQL

## Steps for run the project in local machine:

1.  Install Python
2.  Make sure that the environment variables for python are set.
3.  Go to the path /EmotionsOnPage/ and make sure that the requirements.txt file are there.
4.  Run: 

```bash
pip install -r requirements.txt
```

5.  Go to EmotionsOnPage path, make sure that the file manage.py are in the path.
6.  Run:

```bash
 python manage.py runserver
```

7.  Go to <http://127.0.0.1:8000/> in any browser.

## Links:

<https://docs.djangoproject.com/en/3.2/topics/install/>

<https://blog.nubecolectiva.com/como-integrar-django-y-bootstrap-4/>

## Project Structure:

    -EmotionsOnPage -> Root path
        -.git   -> Don't Touch!
        -EmotionsOnPage -> Here are the files that belong to the server processing in django.
            -__init__.py -> Don't Touch!
            -asgi.py     -> Don't Touch!
            -settings.py -> Here is where the app are configurated.
            -urls.py     -> Here is where the frontend and backend.
            -views.py    -> Here is where the frontend need to be set before the url.
            -wsgi.py     -> Don't Touch!
        -frontend   -> Here are the files that belong to the user interface in bootstrap.

## The server that we are going to use to upload the app are:

Heroku: <https://dashboard.heroku.com/apps/emotionsonpage>
