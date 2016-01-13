# BookTime
* BookTime will provide users with easy access to their favorite novels, biographies, short stories, and more!  Users will be able to search for a specific book based on title, author, or a key word. Individual accounts will allow users to store and organuze books in different libraries. Each book entry will contain:
	*A plot summary
	*An MLA citation
	*Links to purchase the book
		*Information on availability and price
	*A sample of 100-200 words from the book, which the user can read (specifying his or her 	start/stop with the corresponding buttons).  The website will generate an estimate accordingly 	of how long it will take the user to read the book, depending on his or her rate of words read 	per minute.


## Tools:
* Google Books API.
* Project Gutenberg Data
* AJAX and JQuery to better the user experience

##Futute Implementations
* Include SparkNotes links/ information
* Use JS Live Updates for when a new and/or better offer on a book is released


## The Team
|Role      |Name          	|
|----------|----------------|
|Leader    |Ari Hatzimemos  |
|Frontend  |Andrew Kratsios |
|Backend   |Mary McGreal    |

##To Do List
* README.md
* app.py
  * APIs
* utils.py
  * user account database
  * helper functions (i.e. removing whitespace from string input)
* user.py
	* authenticates user logins
* database.py
	* handles data from the database
* user interface
  * javascript/AJAX where needed
  * templates
    * css
    * html
	
###left to do:
* finalize images for website
* make a stored book less like a post and more like a "favorite" item
* create libraries for books
	* instead of users being directed to a main page with book entries, allow them to select a library which will then display books they/ other users have searched for and stored
* finalize color scheme!!
* description of BookTime on homepage

##Timeline
* By midnight January 10th (Sunday night):
  * all API work in app.py
* By midnight January 13th (Wednesday night):
  * at least half of utils.py
* By midnight January 17th (Sunday night):
  * user accounts
  * templates
* By midnight January 20th (Wednesday night):
  * finish utils.py
* by midnight January 21st (Thursday night):
  * polish up everything and submit!
