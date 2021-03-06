# website
Repository for managing arthurshmidt.com and its development.

## Implementation thoughts
Combine Python, HTML, CSS, Javascript, and SQL to manage the webpage.  All blogging content to be stored in an SQL database.  I will first try and use Flask as the initial implementation and possibly migrate to Django.

## Installing apache and flask

Install Flask

	$ sudo pip3 install Flask

## Preping Apache for Flask

Install mod_wsgi

	$ apt-get install libapache2-mod-wsgi-py3

Add wsgi to virtual host

	$ cp /var/www/FLASHAPPS/BlogApp/other/BlogApp.conf /etc/apache2/sites-available/BlogApp.conf

Disable default virtual host and enable BlogApp.conf

	$ sudo a2dissite 000-default.conf
	$ sudo a2ensite BlogApp.conf

Restart apache server to activate new virtual site

	$ sudo systemctl restart apache2

## Preping mysql (mariadb)

Create databse

	$ CREATE DATABASE 'blog_posts';
	$ SHOW DATABASES;

Create database user

	$ CREATE USER 'blog'@localhost IDENTIFIED BY 'enter password';
	$ SELECT User FROM mysql.user;

Change privilages on user to access database

	$ GRANT ALL PRIVILEGES ON blog_posts.* TO 'blog'@localhost;
	$ FLUSH PRIVILEGES;
	$ SHOW GRANTS FOR 'blog'@localhost;

## Git & Flask integration with Apache

### Apache Files
Apache locates its files in the /var/www directory. By default the "Default" files are locatedin /var/www/html.   With the Flask implementation I have removed the html directory and create a FLASKAPPS directory, where all flask applications will be stored.  

Apache allows for multiple websites through apache virtualization.  In order to do this, you designate the VirtualHost in /etc/apache2/sites-available and /etc/apache2/sites-enabled. Prior to enabling a site, you will need to disable the default webpage.  This will most likely be the 000-default.conf in /etc/apache2/sites-available.

    $ a2ensite <website>
    $ a2dissite <website>

Example: if you have have NewWebSite.conf in the /etc/apache2/sites-available the commands would be

    $ a2ensite NewWebSite
    $ a3dissite NewWebSite

    ** no path is required.  Apached assumes the /etc/apache2/sites-available directory.

### Flask Files

