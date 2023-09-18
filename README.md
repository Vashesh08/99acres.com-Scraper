# 99acres.com-Scraper
Web Scraper For 99acres.com built using Python, Selenium and Django. This is just for testing purposes. Use responsibly.

[![Video](https://img.youtube.com/vi/QprHOJzurXM/maxresdefault.jpg)](https://youtu.be/QprHOJzurXM)


# How to run it

First install a virutal env in Python
```
python -m venv "Folder_name"
```
```
cd "Folder_name"
```


Activate the virtualenv in Windows
```
Scripts\activate
```

Activate the virtualenv in Linux
```
source bin\activate
```

Clone the repo
```
git clone https://github.com/Vashesh08/99acres.com-Scraper.git
```
```
cd cd 99acres.com-Scraper
```


Install the requirement list
```
pip install -r requirements.txt
```


Run the Server
```
cd PropertyScraper
```
```
python manage.py runserver
```



# Additional Instructions:


To sync database,
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py migrate --run-syncdb
```
If you want to scrape using Selenium, then run cronjob using following commands. This does not work on windows, try using wsl2.
```
python manage.py crontab add
```
The hash returned in this command is used to run the cronjob
```
python manage.py crontab run <hash>
```

Django admin username = admin
Django admin username = password@example

