# symbolic-recommendations

This repository contains a web application that allows you to make content-based movie recommendations using symbolic data.

The application runs using MongoDB. [Mongo Download](https://www.mongodb.com/try/download/compass)

Also the initial data to upload to the database is in the data folder.

More details and other approaches to recommender systems [here](https://github.com/DelmiroDaladier/recommender_system_using_symbolic_data).

### Running project

In the folder symbolic-recommendations type:

```
pip install -r requirements.txt
```

Then

```
cd backend
```

Run the database migrations:

```
python manage.py migrate
```


Now execute the application:
```
python manage.py runserver
```
