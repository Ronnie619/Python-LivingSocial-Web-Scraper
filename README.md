Python-LivingSocial-Web-Scraper
===============================

App is a web scraper that utilizes the python tool Scrapy to scroll through Living Social, and saves local deals to a Postgres database. Source includes shell code to schedule the computer to run this script daily, so that rather than getting those annoying emails, users can query the database when they want a deal on sky diving or hot yoga.

To make a script that runs daily:

type crontab -e into the command line and add this line to the file:

0 13  * * * sh ~ <location of your scrapy.sh file>

This says that ever day at hour 13 (1pm, relative to your local machine time), run the scrapy.sh script.
