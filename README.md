# Movie Catalog
 
 
 ## Project Overview
 
• Developed a RESTful web application using Flask python framework along with Google OAuth authentication.

• Implemented HTTP methods to perform CRUD operations and set up the database, configured users and required permissions.

## Getting Started

  1. Install Vagrant and VirtualBox
  2. Download or Clone (https://github.com/udacity/fullstack-nanodegree-vm) repository. 
  3. Unzip the project folder in catalog folder. 
 

## Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository in your shell using command:
  
   `vagrant up`
 
  2. Then Log into this using command:
  
   `vagrant ssh`

  3. Change directory to /vagrant /catalog
  
## Launching the application:
   From the vagrant directory inside the virtual machine

  1. Setup the database.
  
  
     `python database_setup.py`
  
  2. To insert default movie data 
  
    `python database_init.py`

  3.To start the web browser:
  
   `python app.py`
   
  4. Open browser to view the web application:
  
   `http://localhost:8000`
   
   `http://localhost:8000/genre`

  

## Features:

* Can access JSON data at the following pages:

  -> All Genres: [http://localhost:8000/genre/JSON
  
  -> Movies in specific genre: [http://localhost:8000/genre/\<genre_id\>/JSON
  
  -> Specific movie : [http://localhost:8000/genre/\<genre_id\>/\<movie_id\>/JSON
  
* Users can login / logout with Google Plus sign in.

* Users cannot Get or Post New, Edit, or Delete movies without sign in into the account.

*  Users cannot Get or Post Edit or Delete movies without being the original creators of the movie.

* Logged in users can create new movie.

  
  
