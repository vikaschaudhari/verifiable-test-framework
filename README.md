# verifiable-test-framework


This is read me file for verifiable test framework.


How to open project?
========================================================
1) Navigate to particular folder/directory where you need checkout this code.
2) Checkout the code
	Ex. git clone https://github.com/vikaschaudhari/verifiable-test-framework.git
3) Open download project in editor
	Ex. pycharm editor



How to run?
========================================================
1) Go to the tests directory in the editor.
2) Select test_*.py file which you want to execute.
3) Right click on it and select 'Run' option
4) You need to configure Python interpreter if not configured.

OR

1) Open command prompt
2) Navigate to the tests directory
3) Run 'pytest' (NOTE: it will all files under tests directory)
4) Run 'pytest <test-file-name>' which you want to execute. (NOTE: This will execute particular file)

 Framework Structure:
=======================================================
This framework structure created for demo purpose only. 
framework structure explained below.
1) tests:
   In this directory, all test_*py files stored. 
   Also we can classify test files based on features. 
   Means we create separate directory for each feature
   and keep related test py files under that directory. 
   
2) logs:
   All logs should be stored under log directory for debug purpose.
   
3) reports:
   All reports should be stored under reports directory.
   
4) config:
   All common configurations related to framework should be configured under config file.
   Ex. log -> log path, 
   reports -> reports path
   log format
   
   Also, we keep common data under config directory.
5) lib:
   All common libraries related to framework should be stored under this directory.
   we also keep helper functions files, common operation files 
   under lib. 
     
