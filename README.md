# newsole-proj

## Created this python project that uses Django framework.

1. install python
   `pip install pipenv`

install django using pipenv to save in virtual env
`pipenv install django`

launch virtual environment. always run this to make web app run seamlessly
`pipenv shell`

integrated terminal in vs code. this will auto run virtual environment when you open your project folder

1. search 'python interpreter'
2. search the python path inside the virtual environment. `pipenv --venv`
3. copy the path and select enter interpreter path and past the path link. add in the end /bin/python

create a project folder
`django-admin startproject <nameofyourproject> .`

create an app folder
`python manage.py startapp <nameofyourapp>`

use this code throughout
`python manage.py <command>`

run the server
`python manage.py runserver`

adding and updating models.py, always run this code to process and update the database sqlite3
`python manage.py makemigrations`
`python manage.py migrate`

### To access Django admin panel

1. create superuser
   `python manage.py createsuperuser`
2. access admin panel by adding '/admin' at the end of URL

- Django by default uses SQL Lite, a lightweight databse

### MVT

1. Model - managing data. it is the database
2. View - take user request and process. deals with logic part of application (view.py file)
   - class-based view
   - function-based view
   * urls.py - url mapping. Creates a path to access the link from views.py
3. Template - HTML markup, dynamic components. template for user interface

### Switching sqlite3 to MySQL database

1. Go to settings.py and change default engine in DATABASES to `ENGINE: 'django.db.backends.mysql'`
2. Open MySQL Workbench and create a new schema

### Create a MYSQL Database

1. Install MYSQL
   `pip install mysqlclient`
2. Access MySQL
   `mysql -u root -p`

- if you can't remember your password. Rest MySQL Root Password
  a. Stop MySQL `brew services stop mysql`
  b. Start MySQL in safe mode:
  `mysqld_safe --skip-grant-tables &`
  c. Open new terminal window and login as root
  `mysql -u root`
  d. Change the root password
  `FLUSH PRIVILEGES;`
  `ALTER USER 'root'@'localhost' IDENTIFIED BY 'newpassword';`
  e. Login with your new password

3. Create your DB
   `create database <name of db>;`
4. To use the database
   `use <nameofdb>'`
5. To see that db changed
   `show tables;`
6. To exit MySQL
   `\q`

### Configure MySql in Django

1. Install driver inside VS Code
   `pip install mysqlclient`
2. Adjust DB list in settings.py under project folder
   - Go to line DATABASE
   - Update Engine and Name
   - Add User and Password

### Handling static and media files

1. Used Whitenoise to render since this is a simple project.

- For bigger projects, it is advised to use CDN such as Google Cloud Storage, AWS, etc. Configure django's STATIC URL and point it there.

### Choosing a platform to host media files

My requirements are based on compliance and security certifications, private file features, integration with Django and deployment to Render.

### Storage Platform Free Tier and Security/Compliance Comparison

| Feature                     | Cloudinary Free Tier                 | GCS Free Tier                                    |
| --------------------------- | ------------------------------------ | ------------------------------------------------ |
| **Free storage/month**      | 25 GB or 25,000 images               | 5 GB (US multi-region only)                      |
| **Free bandwidth/month**    | 25 GB                                | 1 GB                                             |
| **Requires credit card**    | No                                   | Yes                                              |
| **Easiest to get started**  | Yes                                  | Somewhat (needs billing)                         |
| **Private file support**    | Yes (with config, public by default) | Yes (private by default)                         |
| **Signed URLs**             | Yes                                  | Yes                                              |
| **Granular access control** | No (basic API key roles)             | Yes (IAM roles, ACLs, per-object)                |
| **Audit logs**              | Basic (API access logs)              | Detailed (Cloud Audit Logs)                      |
| **Compliance**              | SOC 2, ISO 27001, GDPR, CCPA         | SOC 1/2/3, ISO 27001, HIPAA, GDPR, PCI DSS, etc. |
| **Encryption at rest**      | Yes                                  | Yes (with optional customer keys)                |
| **Encryption in transit**   | Yes                                  | Yes                                              |

**Notes:**

- **Cloudinary** is easier and more generous for free use, but files are public by default unless you configure private modes.
- **Google Cloud Storage** offers stronger compliance and security features (private by default, granular access, detailed audit logs), but its free tier is smaller and requires a credit card.

## Project Structure

```
project/
├── myfirstproj/
│   ├── templates/
│   ├── migrations/
│   └── static/
│       ├── css/
│       └── img/
├── myfirstapp/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## References

https://stockx.com/
https://limitededt.com/
