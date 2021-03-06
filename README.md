# Spooky Spool
Deployed site: [https://spooky-spool.herokuapp.com/](https://spooky-spool.herokuapp.com/)
## Table of Contents
1. [Aim](#aim)
2. [UX](#ux)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

---

## Aim
Spooky Spool's aim is to create a usable and easily searchable database of scary/horror themed movies.
Spooky Spool is a place for horror fans to find movies, create accounts and share films not included in the database.
Currently designed as an informational store on movies, once the user base is large enough the website would transition to include links to streaming platforms.
This way users can find and share films but also be directed to where they are available, generating revenue from the referral.

## UX

Spooky Spool aims to function in the space between websites like [Fandom](https://www.fandom.com/) (wiki type websites) and [Netflix](https://www.netflix.com/) which has helped shape
the overall design. It will need to have the large information pool that fandom offers with the easily navigatabe and personalised style that
streaming sites have if it hopes to bridge the two.

* Key Features to borrow:
    * A personaliesd space for our users where they can save data they are interested in.
    * Large amounts of data for users to browse through.
    * Easily searchable data which can be refined for specific items.
    * Mobile friendly data.

### User Stories
To help refine the incorporeal aims above with real features, these user stories have been devised to structure the website:
* As a user, I want to know what I can actually do with this website, so I'll know if I want to create an account.
* As a user, I want to search the database based on my preferences, so I can find movies I want.
* As a user, I want to be able to find out more information on a movie, so I can tell if I want to watch it.
* As a user, I want to the movies I'm interested in to be easily available, so I can refer to them quickly.
* As a user, I want to add movies that aren't on the database, so I can share them with other users.
* As a user, I want to be able to edit information on my movies, so it can be corrected if I make mistakes.
* As a user, I want to know if I already added a movie to a watchlist or favourites, so I don't have duplicates in my saved lists.
* As the owner, I want many movies, so users have lots of options to browse through.
* As the owner, I want guests to create accounts, so I can increase my userbase.
* As the owner, I want creating an account to simple, to prevent barriers to entry deterring users.
* As the owner, I want users to add their own movies, so my database increases.
* As the owner, I want the website information to be easily digestible, to stop users leaving due to information overload.

### Information Architecture
To marry the needs for large amounts of infomation with a good user experience, the website will have to initailly present
small chunks of data from a large collection. This is why a card approach is best. Users can see the scope of the data
but can get more detailed information only on the topics they are interested in.

To make this information easy to escape from, a fixed navbar would suit the website. 
That way no matter where the user is on the site they are always one click away from either a clean search page, their user home or the actual home page.

Users will also want to save data they are interested in without having to search for it again. To prevent overcrowding, which will turn users off, a Netflix stlye carousel approach makes sense.
Useful data is still visible with other movie cards accessible but not displayed. Again, a card approach should be used in order for users to quickly see the scope of what they have
saved but will only get detailed information on movies they are interested in.

### Wireframes
Wireframes for the desktop and mobile versions can be found [here](https://github.com/SDGreen/SpookySpool/tree/master/wireframes)

### Target Demographic
The target demographic for Spooky Spool is scary movie fans across all ages.
This is a broad demographic but skews towards younger audiences (the average viewer is under 25)
with a roughly even split between the sexes [(source)](https://cmpalexgilbey.weebly.com/uploads/3/8/8/7/38878453/horror_film_research.pdf).
As the audience is younger the website must have a mobile-first design, which is more often used over traditional desktops by this demographic.

### Design Choices
As this website has a clear theme, a palette reminicent of Halloween colours has been settled on.
This is also gender-neutral and will appeal to a larger audience than colours which are gendered (i.e. bright pinks or red & black).
To avoid appearing kitch, a more adult palette has been selected where jet blacks are replaced with dark blues to compliment the orange throughout the site.

Other colours will be picked based on user expectations so they can intuitively learn to use the site.
Green & checkmarks will be used for buttons which add movies to a user's watchlist. This is common across websites to signify something have been added to a basket etc.
Buttons that add items to a user's "favourites" list will use yellow combined with star motifs, which will also fit user expectations.
Cancel or close buttons will also be red rather than halloween themed to fit user expectations about how they function.

Finally, the fonts picked are again a nod to Halloween without being too childish.
Information will be presented in an easily readable font, ["Raleway"](https://fonts.google.com/specimen/Raleway), with ["Didact Gothic"](https://fonts.google.com/specimen/Didact+Gothic) used for titles.
To keep the spooky theme running through the website, ["Special Elite"](https://fonts.google.com/specimen/Special+Elite) is used for the logo text but used sparingly elsewhere to maintain the more mature feel of the website.
## Features
### Existing Features
* #### User Login: 
    Users can create accounts, sign in and logout out. When signing up the website new users using existing usernames or
    emails are asked to try again to prevent duplication in the user collection. Appropriate error warnings will appear.
    The siginup form also validates passwords with a retype field, which blocks the login button until their inputs match.
    Login will also fail if the username isn't in the database or the password is incorrect with error messages for both.
* #### Responsive Movie Cards:
    Cards are generated for each movie in the database. Clicking on a card image or title will redirect the user to that movie's
    page where they can get more information about it.
    If a link to the movie's poster isn't provided, the default clapperboard image is used instead.
    If the user just wants a quick summary of the movie they can click the information Icon at the bottom of the card, which displays more detailed
    information about the plot.
    The cards are also responsive to device size, adjusting how many are displayed per row depending on the user's device to keep information clear and
    the page clutter-free.
    The cards will display more options to logged in users, with quick links to add that movie to their watchlist or favourites.
    If the movie is already on the user's lists then these links change to reflect that and provide quick visual clues that the movie was successfully added to either list.
* #### Responsive Movie Page:
    Each movie has it's data injected into a movie page template to display what information is available.
    If fields like "Age Rating" or "Metascore" aren't available then the copy changes to reflect that.
* #### Interactive Accordion:
    A materialize accordion keeps additional movie information hidden until the user needs it.
    By clicking on each accordion title the information is revealed. This keeps a lot of information packed neatly onto one page.
* #### Multiple Calls to Sign-up/Login:
    The browse page, search results page, movie page and navbar can all detect if the visitor is a guest or user.
    If the user isn't logged in then copy appears with links to the login page, encouraging users to sign in or create an account to access all the website's functions.
* #### Search Bar with Advanced Search Options:
    The browse and search results pages each include a search bar where users can search the database by movie title.
    If they would like to expand that search to include release year, genre or age rating then a drop down menu can be clicked which includes these options.
    By default, this is hidden to prevent page cluttering.
    The results page will also flash how many results are found by the search.
* #### Draggable Watchlist, Favourites and Submitted Movies Carousels:
    The user homepage has interactive carousels which will display a card for each movie in that list. 
    The carousels are responsive so smaller devices have fewer cards per slide, preventing cluttering.
    They are also draggable on touch devices (see [credits](#credits) for code). 
    If no movies are in a list then the carousel turns into a call to action asking the user to browse/input movies to add them into that list.
* #### Add Movie Insert/Update Form:
    Users can add movies into the database using a form provided by materialize (see [credits](#credits)).
    The "add movie" form will insert a movie into the database and has validation so key fields can't be missed.
    The new movie is also automatically inserted into that user's submitted list.
    Buttons are provided so users can add/remove input fields for categories like actors, which can have varying numbers of inputs.
    The update form inserts the current data as values so users can know what the default is. This also means users don't have to re-enter information that doesn't change.
* #### Selective Update/Delete buttons:
    Buttons which update or remove a movie from the database are only shown on the movie page to the users who created that film.
    This prevents core movie data being corrupted by malicious users.
* #### Responsive Navbar:
    Mobile-users have a smaller Navbar which collapses the links into a dropdown menu to prevent cluttering.
    The large title is also replaced so just the logo is visible to viewers on smaller devices.
* #### Responsive buttons:
    Link and buttons throughout the website react when hovered over so users know they can be clicked.
* #### Responsive Pagination:
    The main browse page and results page are also paginated based on how many movies there are. The browse page always has this feature as the number of movies is always over 36.
    On small devices the pagination reduces so that fewer pages are available either side of the active page to reduce clutter.

### Features Left to Implement
* #### Comment Functionality on Movie Pages:
    This would help facilitate conversation among our users and help expand the user base.
* #### Admin Functionality for Movie Inserts:
    With a larger team, admins could be used to review inserts to prevent incorrect or unsuitable data from entering the database.
* #### Links to Streaming Platforms:
    We'd like to include links to wesbites where the movies are available to stream in order to add another source of revenue.
* #### Movie Recommendation based on User's Watchlist/Favourites:
    This feature would be added on the search bar so viewers have recommendations rather than search for things they would like, increasing engagement. 
* #### Advanced Search Functionality:
    Currently you can search based on four filters, however the movies have more data which could be searched by (i.e. actors).
* #### Password Resetting:
    Currently users can create accounts but that information is lost if the user forgets their password.
    As we currently save emails it can be retrievable, we just need to add a reset password feature.
* #### Report Feature:
    A report feature would be useful for movies which have broken poster links or inappropriate information.

## Technologies Used
* [HTML5](https://html.spec.whatwg.org/multipage/) - To create the structure of the page.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - Used to style the website.
* [Materialize v0.100.2/](http://archives.materializecss.com/0.100.2/) - This framework was used to create a responsive mobile-first design, along with some components (listed in [credits](#credits)).
* [JavaScript](https://www.javascript.com/) - Included with Materialize for their framework to function.
* [jQuery](https://jquery.com/) - Included with Materialize, also used to code form_fields.js, password_validator.js and searchbar_fields.js (along with some javaScript)
* [Python (v3.8)](https://www.python.org/) - Used to code the base app.py which runs the website using the Flask framework. Also used to facilitate MongoDB operations.
* [Flask (v1.1.2)](https://flask.palletsprojects.com/en/1.1.x/) - Framework used to create the app which runs the website.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Templating language used for the website pages.
* [MongoDB](https://docs.mongodb.com/) - Used to host the database along with retrieve data, save edits, deletions and inserts.
* [Git](https://git-scm.com/) - Used for version control and tracking changes to the code whilst in development.
* [Google Fonts](https://fonts.google.com/) - Used for website fonts [Didact Gothic](https://fonts.google.com/specimen/Didact+Gothic) for headings, [Raleway](https://fonts.google.com/specimen/Raleway) for content text and [Special Elite](https://fonts.google.com/specimen/Special+Elite) for logo text.
* [Font Awesome](https://fontawesome.com/) - This library provided the Icons used across the site.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Key for finding bugs and testing responsive design.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to prefix the css, allowing it to work across different browsers.

## Testing
Spooky Spool's testing can be split into four categories: 
* Database CRUD operations.
* User validation.
* DOM Manipulation.
* Responsive Design.

### Database CRUD Operations:

* #### Read Operations:
    * On the browse page, a card is loaded for every movie in the database.
    * On the results page, movies are pulled from the database that match the search options.
    * If clicked on, the movie card redirects a page for that film which loads the data.

* #### Create Operations:
    * When a user signs up, a new user is created in the user collection with empty arrays for their watchlist, favourite list and submitted movies list.
    * When a user adds a new movie, it enters the movies collection with relevant fields. The movie's ID is also added to the user's submitted movies list.

* #### Update Operations:
    * When a user tries to update one of their films, a form is generated with all the existing data already filled in.
    * Once updated, the new data now is in the database instead.
    * If a user adds a movie to their watchlist or favourites, that movie's ID appears in the users relevant list.

* #### Delete Operations:
    * When a user deletes their movie, it is removed from the database and their submitted movies list.

### User Validation:

* #### Login Validation:
    * Users can't login with an incorrect password. The respective error message appears.
    * Users can't login with the incorrect username. The appropriate error message appears.

* #### Sign Up Validation:
    * Users can't create an account with a username currently in the database. The appropriate error message appears.
    * Users can't create an account with an email currently in the database. The correct error message appears.
    * If the password and retype password fields don't match, the login button is disabled.
    * Users can't create passwords under 5 or over 20 characters long.
    * Users can't create usernames under 3 or over 10 characters long.

* #### User is Logged On Validation:
    * If a user is logged in, the navbar "Login" button turns into an account dropdown menu.
    * If the user is logged in, links to the login page on the homepage and footer redirect to the user's homepage.
    * If the user is logged in, the movie cards display "add to watchlist" and "add to favourites" options.
    * If the user is logged in, the movie pages display "add to watchlist" and "add to favourites" options at the bottom of the page.
    * If the user is logged in and on a movie page they created, the update and delete buttons appear.
    * If a user isn't logged in, calls to login appear on the browse, search and movie pages.
    * Movie cards and movie pages will display remove from watchlist/favourites option if that movie is already in the list in question.

### DOM Manipulation:

* If the options arrow is clicked on the search bar, a larger form will appear below with more search fields. If clicked again this form is collapsed.
* If a user clicks on the plus icon on the update/insert movie forms, a new input field will appear.
* If the minus icon is click on the update/insert movie forms, new inputs will be deleted but the original cannot be.

#### Responsive Design Testing
The responsive design was tested using multiple physical devices:
* Galaxy S8 (Chrome)
* iPhone 6 plus (Safari)
* iPad Air 2 (Safari)
* Leveno IdeaPad S340 (Chrome)
* MacBook (Chrome & Safari)
* iPhone X (Safari)

Chrome DevTools was also used to test the design on the following devices:
* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad 
* iPad Pro

### Browser testing

Spooky Spool was physically tested on the following browsers:
* Microsoft Edge version 86.0.622.63
* Chrome version 86.0.4240.111 
* Firefox version 81.0
* Safari version 14.0.5 (15610.1.28.1.9)

### Code Validation
* HTML5 code validated using [https://validator.w3.org/](https://validator.w3.org/)
* CSS3 code validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
* JS code validated using [https://jshint.com/](https://jshint.com/)
* Python code validated using [Extend Class Python Validator](https://extendsclass.com/python-tester.html)
### User Stories tested
#### As a user, I want to know what I can actually do with this website, so I'll know if I want to create an account.
* The home page quickly tells users the key features, how to use them and where to go.
#### As a user, I want to search the database based on my preferences, so I can find movies I want.
* The search bar allows users to search by title, year, genre and age rating to refine results.
#### As a user, I want to be able to find out more information on a movie, so I can tell if I want to watch it.
* On every movie card are clickable links to a page with the full movie details laid out in an easily digestible fashion.
#### As a user, I want to the movies I'm interested in to be easily available, so I can refer to them quickly.
* Movie cards and movie pages have buttons allowing users to add the movie to their watchlist/favourites. Not only does this change the cards so users will know if it is on one of their lists, the user homepage has carousels diplaying these movies too.
#### As a user, I want to add movies that aren't on the database, so I can share them with other users.
* The add movie option is in the navbar (once signed in) so users can easily access it. Once clicked a form appears where users can fill in their new movie data.
#### As a user, I want to be able to edit information on my movies, so it can be corrected if I make mistakes.
* Users can go to their submitted movies by searching the database or going to their user homepage. An update option appears on movie pages if it is one the user inserted, this opens a form (with the current data as default values for easy submission) where they can edit the movie information. By only allowing the user who submitted the movie to edit it, this stops incorrect data being added by malicious users.
#### As a user, I want to know if I already added a movie to a watchlist or favourites, so I don't have duplicates in my saved lists.
* Movies already in a users lists have different icons so users can't add the same movie twice to a list.
#### As the owner, I want many movies, so users have lots of options to browse through.
* The database has info on 16072 movies, each of which can be accessed.
#### As the owner, I want guests to create accounts, so I can increase my userbase.
* Users can sign up. There are also many calls to sign up across the website if users have not already.
#### As the owner, I want creating an account to simple, to prevent barriers to entry deterring users.
* Sign-up follows the reddit model of using less barriers to sign up. All you need is a unique username and email.
#### As the owner, I want users to add their own movies, so my database increases.
* The add movies option is in the navbar so it is always easily reached. Once clicked users can add their own movies which only they can delete. This prevents malicous users from trying to reduce the database as they are limited to films they create.
#### As the owner, I want the website information to be easily digestible, to stop users leaving due to information overload.
* Movie cards, carousels and movie pages all change size to prevent the page getting overcrowded. The detailed movie infomation is stored in an accordian to prevent cluttering.

### Bugs
Below is a brief summary of the most site-breaking issues and how they were solved:

#### Movies not part of the brief (non-horror) kept appearing in the database.
* The original movie data came in a json file with over 600,000 entries. As Spooky Spool only deals with horror or spooky themed movies (Addams Family wouldn't be considered scary but does fit the brief for this website), a search was used to find just movies with "Thriller" or "Horror" in their genre array.
When first testing the movie card feature, movies like Stuart Little appeared which are not horror. This issue was the database size. The original code used to wittle down the database looped through each movie and compared this to an array of genres. In hindsight this was convolute, a simple search with the correct filters would have work.
As a result, the page would time-out before the whole database was checked, leaving off-brand movies in the database. This was fixed by using a count to check how many movies were in the database. If this count matched a count of movies with the correct genres in their array, I knew all the movies were removed. If the counts didn't match, the code was run again to remove more off-brand movies before timeing-out.
After deleting and re-uploading all the movies due to a title bug (see below), simpler code was used to remove the movies which didn't time-out as much but the count was still used. 
#### User IDs could not be stored in the session data.
* Originally the user's _id was also going to be stored in the session data to act as a easy way to identify the user for database functions (i.e. adding a movie to their watchlist). As the _id is an ObjectID (a BSON data type), this proved hard to store in the session data without manipulation. Rather than write extra code, it happens that usernames are unique, so these were used as a primary key to store in the session data instead (as a string it is much simpler to manipulate).
#### KeyErrors would appear on pages that checked for signed in users.
* Many pages used `if session["username"]:` as a check for if the user was a guest or not. As the logout function set `session["username"]` to an empty string. This didn't throw errors during development as `session["username"]` had always existed after testing the login functions earlier in development.
When trying the website on new devices though, this would throw a KeyError as the username key didn't exist. To fix this, the logout function deleted the username key and the better: `if "username" in session.keys()` was used to check if the viewer was signed in.
#### The SignUp form would call the login() function instead.
* On the login page there are two forms, one to login and one within a modal to sign up. To begin with, clicking the sign up button would incorrectly fire the login form instead.
This would throw an error as the user didn't exist yet and wouldn't create the user either. To fix this, `form` attributes were added to each button so they only triggered the correct form. 
#### Age ratings wouldn't render in order on update movie forms.
* On the insert movie form, the age ratings are hard coded as options within a select element. On the update form these options needed to be rendered in order with the current value preselected.
The idea of converting the ratings to a collection (like genres) was considered but a quicker solution was to create an array of the age ratings and just cycle through this instead. This meant the age ratings were displayed in order and the orginal value was preselected.
#### Fixed Navbar would break the mobile Navbar.
* To make the navbar sticky, materialize has a wrapper div which has a class (navbar-fixed) to easily achieve this. This div caused the mobile menu to become unclickable as it was inside the .nav-fixed wrapper. The fix was simple, the mobile navbar was moved outside the new div.
#### Movie titles would capitalize after apostrophies (i.e. Spooky Spool'S Hompage)
* Originally the movie titles were all lowercase to make searches easier, then capitalized using .title() when rendered on the page.
This caused a problem as .title() will capitalize after apostrophies. After looking for new string methods it was decided to re-upload the movie data (as this has the correct capitalization) and just make the search case insensitive using the options provided by $regex

    
## Deployment
Spooky Spool's website was coded using the GitPod IDE. The git repository is stored loacally before being pushed online to the remote repository online at GitHub.
To push the code to the remote repository you follow these steps.
1. Save any local changes made in the GitPod IDE by pressing File -> Save All (or Ctrl+Shift+S).
2. Add these changes to the git staging area by using the ```git add .``` command in the terminal.
3. Commit changes using the ```git commit -m "changes made"``` command.
4. Push these changes to a remote repository using the ```git push``` command.

To publish a live version of the site I used Heroku, here are the steps I took:
1. Create a new app in Heroku
2. Create a Procfile & requirments.txt (with the dependancies listed using `pip3 freeze`) so Heroku can run the app.
3. Add a remote repository to heroku `git remote add heroku https://git.heroku.com/spooky-spool.git`
4. Push the respository to heroku `git push -u master heroku`
5. Add the enviroment varibables to the "config vars" settings on Heroku:
    * IP : 0.0.0.0
    * PORT : 5000
    * MONGODB_URI : mongodb+srv://dbgreen:***password***.k0s1i.mongodb.net/spooky_spool?retryWrites=true&w=majority
    * SECRET_KEY : ***secret key***
4. The site is now published at [https://spooky-spool.herokuapp.com/](https://spooky-spool.herokuapp.com/)

### How to run Spooky Spool's website code locally:
#### Setting up the code:
1. Go to: [https://github.com/SDGreen/SpookySpool](https://github.com/SDGreen/SpookySpool)
2. Click the "Code" button next to the "Gitpod" button which will have a dropdown including "Clone with HTTPS", "Open with GitHub Desktop" & "Download ZIP"
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the copy to clipboard icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the copy to clipboard icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to appear.
6. Type `git clone`, and then paste the URL you copied in Step 3 (https://github.com/SDGreen/SpookySpool.git).
7. Install the requirements by typing `pip3 install -r requirements.txt` in your CLI
#### Creating a database:
1. Create or login to a [MongoDB](https://www.mongodb.com/) account.
2. Add a new cluster.
3. create a new database and create these three collections:
    * users
    * genres
    * movies
4. Populate your genres collection with genre dictionaries, making sure they have the following key-value pairs:
    * genre_name: string
5. Populate your movie collection with movie dictionaries, making sure they have the following key-value pairs:
    * title: string
    * tagline: string
    * description: string
    * runtime: string
    * rating: string
    * metascore: string
    * year: string
    * actors: array (of strings)
    * languages: array (of strings)
    * directors: array (of strings)
    * img_url: string
    * imdb_url: string
    * genre: array (of ObjectIds relating to the relevant genre_name in the genres collection)
#### Adding enviroment varibales:
1. Create an env.py file in the apps root directory.
2. Add the env.py file to your .gitignore (type eny.py in the file)
3. Go to MongoDB and copy the srv link to your database (go to "Command Line Tools", "Connect Instruction", "Connect your application" and copy the link).
4. To your env.py, add your secret key & MongoDB URI:
    >`os.environ["MONGODB_URI"] = "mongodb+srv://`username`:`password`@`username`.k0s1i.mongodb.net/`database_name`?retryWrites=true&w=majority"`    
    >`os.environ["SECRET_KEY"] = "`secret key`"`
#### Running the app
* Simply type `python3 app.py` into your CLI or press the green play button if using GitPod.


## Credits
### Media
Copyright free images taken from [Public Domain Pictures](https://www.publicdomainpictures.net/en/):
* [Clapper Board](https://www.publicdomainpictures.net/pictures/300000/velka/movie-clapperboard.jpg) as [movie-clapperboard.jpg](https://github.com/SDGreen/SpookySpool/tree/master/static/images/movie-clapperboard.jpg)

Copyright free images taken from [Pxhere](https://pxhere.com/)
* [Tree Background](https://pxhere.com/en/photo/1591751) (file name: background.jpg)

Logos created using [FreeLogoDesign](https://www.freelogodesign.org/):
* [Spooky Spool Colour Logo](https://github.com/SDGreen/SpookySpool/tree/master/static/images/logo-color.png) (file name: logo-color.png)
* [Spooky Spool White Logo](https://github.com/SDGreen/SpookySpool/tree/master/static/images/logo-transparent.png) (file name: logo-transparent.png)
* [Spooky Spool Dark Logo](https://github.com/SDGreen/SpookySpool/tree/master/static/images/logo.png) (file name: logo.png)

Favicon created using [Favicon.io](https://favicon.io/favicon-converter/) from edited logo:
* [Favicon](https://github.com/SDGreen/SpookySpool/tree/master/static/images/favicon.png) (file name: favicon.png)

## Code
* Carousels used on user homepage created using [Slick Carousel](https://kenwheeler.github.io/slick/)
* CSS prefixer used: [https://autoprefixer.github.io/](https://autoprefixer.github.io/)
* Original movie information from [Gorochu's data on Kragge](https://www.kaggle.com/gorochu/complete-imdb-movies-dataset)
* Multiple components taken from [Materialize](http://archives.materializecss.com/0.100.2/), including the Navbar, Footer, Pagination, Cards and Form