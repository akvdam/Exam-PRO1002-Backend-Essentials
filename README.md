# Exam-PRO1002-Backend-Essentials
This is the exam project for Backend Essentials. The project was to create an interactive web app blog. 

## Project overview
This repository includes relevant files, set up and databases for the exam project in Backend Essentials. The main files include python scripts, for both the app and the database, as well as scrips for running tests. It contains SQL and database files, as well as HTML and CSS files, in addition to the basic files like read me, license etc. 


## Project structure

```text
├── static folder
│ └── app.css
│ 
├── templates folder
│ └── layout.html
│ └── main.html
│ └── post.html
│ └── post-form.html
│ └── tag.html
│
├── app.py
├── database.py
├── test_app.py
├── test_database.py
├── shared_test_setup.py
│
├── blogspots.sql
├── blog.db
│
├── read me
├── git.ignore
├── license
```

## How to install, run and test the program
Make sure to have Python installed. 



#### Install the program through terminal and clone the repository
Open terminal, choose your desired folder and write the commmand:

```git clone https://github.com/akvdam/BackendEssentials-work_req_4.git](https://github.com/akvdam/Exam-PRO1002-Backend-Essentials```


#### Run the program in terminal
Open terminal, access the project folder and run: 

```python3 app.py```

After running, click on or copy the http-adress to a web browser to display the blog.
Press CTRL+C to exit the program. 


#### Run the tests of the program in terminal
Open terminal, access the project folder and run one command for testing the app, and another for testing the database setup: 

```python3 test_app.py```
```python3 test_database.py```


### Known limitations or future improvements
No known limitations at the moment. A future improvement would be to set up a separte navigation for the tag-page. For now, the tag-page can be accessed by clicking on the tags you want to explore further. It shows all posts with the same tag, but without the possibility to search for specific tags. 

