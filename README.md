# Sample Django App with AWS S3 as File Stroage

## About:
This app implements [django-storages](https://github.com/jschneier/django-storages) to enable using AWS S3 as the File Storage Backend. This app only serves as a sample/base which you can build on further. 

It contains the following:
- Simple Model with 1 field field
- Simple List, Download & Upload pages.

## Prerequisites:
AWS Account with ACCESS_KEY & SECRET KEY (Preferably of a non-root user, you can create a user with just access to S3 and use the users credentials instead of root user)

## Installation
1. Clone the repo.
2. Install requirements/dependancies.
3. Create a .env file with the following variables:

    1. AWS_ACCESS_KEY_ID
    2. AWS_SECRET_ACCESS_KEY
    3. DJANGO_SECRET_KEY

4. Run migrations.
5. Run the app.

## References:
1. https://django-storages.readthedocs.io/en/latest/
2. https://docs.djangoproject.com/en/dev/ref/request-response/#telling-the-browser-to-treat-the-response-as-a-file-attachment
3. https://docs.djangoproject.com/en/4.1/topics/files/
4. https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/

