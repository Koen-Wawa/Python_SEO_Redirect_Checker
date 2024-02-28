How to use the SEO Redirect Checker

*** SETUP FOR PEAK ACERS ***

--> Ask at the IT desk to have the following two programs installed: 

- Python	(programming language)
- Pycharm 	(interpreter of the python language)

--> Next, run Pycharm



*** INSIDE THE PYCHARM PROGRAM ***

--> Follow the following steps before you run the Python script:

- Create a new project, so that you will have a 'main.py' file.
- Copy the lines of code in the main_py_code file that you can find on this github page, there should be 128 lines of code. 
- Paste the lines of code into the main.py file.
- Download the CSV file called "URL list" that you can find on this github page, and move it from the "Downloads" folder on your pc into
  the folder of your new python project, so that it's next to the 'main.py' file.
  Currently, you can't rename the URL List file to something else, the program would no longer recognize it if you do.
- Now a slightly tricky part. Within PyCharm, use ALT + F12 to open the terminal window, and type in the following command:

pip install requests 

- Hit enter and the requests module will be added to your current virtual environment. This will take a couple of seconds. After that you can close the terminal window again. 

- Now open the "URL list" CSV file that you downloaded, using Excel. You see two columns, underneath them you can add the URLs that you want to check. 
  It's best to leave the first row with "Original Page" and "Intended Page" as it is, start below it on row 2.
- Under "Original Page", add the URL that you want to check, and under "Intended Page" add the destination URL, where your redirect should end up. 
  
- You can add as many URLs as you like, but it's better not to overdo it. If you have a list of 200 URLs you want to check 
  from one domain, those URLs will be visited by the script very fast. And if you (for some reason) re-run your program 
  several times in a row, you are basically giving the domain too many HTTP requests to handle, which might make it
  appear slower to others who are trying to visit it. So either keep your list of urls sensibly small, or if its a large list, 
  don't run the python script several times in a row. 

- Please double check that the "Intended Page" input you provide in your CSV file is consistent with the actual URL you want to check,
  when it comes to trailing slashes (/) or having no trailing slashes at the end of a url. Otherwise the script might understand 
  an additional redirect took place.. (e.g. from '/' to ' ', or from ' ' to '/').
  
- After you have added all the urls to the CSV, save it and close it. 


*** HOW TO RUN THE SCRIPT ***

--> You have set up everything to run the script now:

- It's a simple matter of hitting the green 'play' button in the upper right corner, and the program should execute. 
  
- In the folder where you also find the 'main.py' and 'URL list.csv' files, a new CSV file called "Redirect Check" has been added that gives you information
  on the redirect status of your URLs.

- Please keep in mind that when you run the program again, this file will be overwritten,
  so it's best to rename the newly created CSV file (e.g. "Redirect Check [client]") immediately, this takes care of that problem.
