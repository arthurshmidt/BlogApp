# Blog application with Markdown and Sql

For some time I have been considering redoing my existing website which is hosted by SquareSpace.  Couple this with my incessant need to tinker and we arrive at my new project: a self hosted webserver.  This is not a reflection on SquareSpace. In fact, they have been extremely great to use. They provide great web hosting with great design.  

Goals for the new project:
1. Build my own webserver
2. Use SQL
3. Use Python
4. Simple to add blog posts

## System architecture 

In order to meet the goals of the project I landed on the following:
* Debian for the OS
* Apache2 for the webserver
* Flask as the web framework in order to incorporate Python
* mariadb for the sql database.  This will store all the blog posts and associated information.
* Markdown library in python - this addresses the simplicity goal. This way all the blog posts can be written in markdown rather than HTML.  In fact this post will be the first post to test the capabilities of the software.

## OS setup

## Preping the Apache webserver

In order to prep the web server we need to configure apache to accept Flask.  This

## Preping the SQL database

## The code
