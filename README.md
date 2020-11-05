# Spooky Spool
Deployed site: [https://sdgreen.github.io/TotalTarot/](https://sdgreen.github.io/TotalTarot/)
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
The aim of Spooky Spool is to create a usable and easily searchable database of scary/horror themed movies.
Spooky Spool is a place for horror fans to find movies, create accounts and share movies to increase the database.
Currently designed as an informational store on the movies, once the userbase is large enough the website would transition to include links to streaming platforms. This way users can find films, share films but also be directed to where they are avaliable, revenue being generate from the referal.

## UX
Total Tarot's design is aimed to look sleek and simple to make navigation as easy as possible.
Competitor websites tend fall into two categories: 
1. Course advertisements that look good but provide little information
2. Free websites with good information that looked terrible & were hard to navigate
As Total Tarot will straddle between these two worlds, I want to combine the refined and easy handling of a paid for course website with the good information of a free website.
This way it can stand out in the free market and draw a large crowd which can be directed to affiliated websites for users who want to continue their learning.

As Total Tarot will be catering to a niche market with varying levels of IT skills it needs to be easy to navigate and understand. This means it follows a very standard website layout with a Navbar across the top with easily accessible links to each page, a simple hub and spoke model. Each page (other than the card library) is designed to be as small and easy to read as possible, only providing as much information as necessary to learn whilst keeping everything nice and clear. Large pictures are included to keep the users engaged without overcrowding the page as was seen on other free websites.

User research on what and how they would like to learn from a website about Tarot cards came up with three clear goals:
1. An almost "Amazon" like view of all the Tarot cards where you could click each one to find their meaning.
2. Information about where they could find/attend workshops displayed on a map for easy use.
3. Information about how to place the cards to do readings. Many people know the cards have meanings but don't know where to go from there.

This research led most of the design for the web pages. The classes page has a clickable map displaying all the Total Tarot approved classes in the UK. Clicking on your closest mentor brings up more information about how to book a class, keeping the information hidden until needed, maintaining a clean website.
The page dedicated to learning about the cards is a visual library where you can scroll through all 78 cards and click each one to find more information. To keep this easily digestible, the information is concise and easy to view. Once the user wants to learn about a new card, the site hides the previous card's information. There is also a search function to easily find a card and a back-to-top button to keep the page simple to navigate.
The final page again has a lot of information about how to interpret cards without becoming messy. Key information about how to interpret the cards appears first, all other information is signposted but collapsed. When a viewer wants to learn more about layouts they can bring up that information but it will hide itself once the user clicks on a new one. This helps maintain a clean and sleek look whilst having a lot information on the page.

To help the business goal of growing a large following, each page has links to social accounts. No matter where you are on the site, it's easy to follow Total Tarot's social media streams.
As this site wants to make learning as easy as possible it also includes a dark mode feature. This is so users don't strain their eyes whilst using the site.

### Target Demographic
The target demographic for Spooky Spool is scary movie fans across all ages.
This is a broad demographic but scews younger (the average viewer is under 25) with a roughly even split between the sexes [(source)](https://cmpalexgilbey.weebly.com/uploads/3/8/8/7/38878453/horror_film_research.pdf).
As the audience is younger the website must have a mobile first design (which is more often used over traditional desktops by this demographic).
A gender neutral design has also be used as users are expecting more of a scary feel compared to anything gendered.


### User Stories
To help focus the design of Total Tarot's website, user stories were created which point to key features or layouts.
* As a user, I want to know what I can actually do with this website, so I know if I want to create an account.
* As a user, I want search the database based on my prefrences, so I can find movies I want.
* As a user, I want to be able to find out more information on a movie, so I can tell if I want to watch it.
* As a user, I want to movies I'm interested in to be easily avaliable, so I can refer to them quickly.
* As a user, I want to add movies that aren't on the database, so I can share them with other users.
* As a user, I want to be able to edit information on my movies, so it can be correct if I make mistakes.
* As a user, I want to know if I already added a movie to a watchlist or favourites, so I don't have mutliples in my saved lists.
* As the owner, I want links to social accounts, so I can grow our followers.
* As the owner, I want a clean website so users aren't put off and go elsewhere.
* As the owner, I want the information to be interactive so users are hooked and stay on the site.
* As the owner, I want users to be easily directed to affiliated sites, so we can get a commission from them.
* As the owner, I don't want too much information available so viewers want to get classes.
### Wireframes
Wireframes for the desktop and mobile versions can be found [here](https://github.com/SDGreen/SpookySpool/tree/master/wireframes)

## Features
### Existing Features
* #### User Login: 
    Users can create accounts, sign in and logout out. When signing up the website new users using existing usernames or emails are asked to try again (with messages explaining why they failed) to prevent repetition.
    The siginup form also validates passwords with a retype field which blocks the login button untill their inputs match.
    Login will also fail if the username isn't in the database or the password is incorrect with error messages for both.
* #### Responsive Movie Cards:
    Cards are generated for each movie in the databse. Clicking on a card image or title will redirect the user to that movie's page where they can get more information about it.
    If a link to the movie's poster isn't provided, the default clapperboard image is used instead.
    The the user just wants a quick summary they can click the information Icon at the bottom of the card which displays more detailed information about the plot.
    The cards are also resposive to size, ajusting how many are displayed per row depending on the users device to keep information and the page clutter free clear.
    The cards will display more options to logged in users with quick links to add that movie to their watchlist or favourites. If the movie is already on the user's lists then these links change to relflect that and provide quick visual clues that the movie was sucessfully added to either list.
* #### Resposive Movie Page:
    Each movie has it's data injected into a movie page template to display what information is avaliable. If fields like Age rating or Metascore aren't avaliable then the copy changed to reflect that.
* #### Interactive Accordion:
    A materialize accordion which keeps additional movie information hidden until the user needs it. By click on each accordian title the information is revealed. This keeps a lot of information packed neatly onto one page.
* #### Mutliple Calls to Sign-up/Login:
    The browse page, search results page, movie page and navbar can all detect if the visitor is a guest or user. If the user isn't logged in then copy appears with links to the login page, encouring users to signin or create an account to access all the websites functions.
* #### Search Bar with Advanced Search Options:
    The browse and search results pages each include a search bar where users can search the database by movie title.
    If they would like to expand that search to include release year, genre or age rating then a dropdown menu can be click which includes these option. By default this is hidden to prevent page cluttering.
    The results page will also flash how many results are found for the user.
* #### Draggable Watchlist, Favourites and Submitted Movies Carousels:
    The user homepage has interactive carousels which will display a card for each movie in that list. 
    The carousels are resposinve to device size so smaller pages have less cards per slide, preventing cluttering. They are also draggable on touch devices (see [credits](#credits) for code]) 
    If no movies are in a list then the carousel turns into a call to action asking the user to browse/input movies to add them into that list.
* #### Add Movie Insert/Update Form:
    Users can add movies into the database using a form provided by materialize (see [credits](#credits)).
    The add movie form will insert a movie into the database and has validation so key fields can't be missed. The new movie is also automatically inserted into that user's submitted list.
    Buttons are provided so users can add/remove input fields for catagories like actors which can have varying numbers of inputs.
    The update form inserts the current data as values so users can know what the default is. This also means users don't have to re-enter information which doesn't change.
* #### Selective Update/Delete buttons:
    Buttons which update or remove a movie from the database are only shown on the movie page to the users who created that film.
    This prevents core movie data being corrupted by malicous users.
* #### Resposive Navbar:
    The Navbar is created so that links are displayed on a dropdown for mobile users to prevent cluttering. The large title is also replaced so just the logo is visible to viewers on smaller devices.
* #### Resposive buttons:
    Link and buttons throughout the website react when hovered so users know they can be clicked.
* #### Responsive Pagination:
    The main browse page and results page are also paginated based on how many movies their are (the browse page always has this feature as the number of movies is always over 36)
    On small devices the pagination reduces so that less pages are avaliable either side of the active page to reduce clutter.

### Features Left to Implement
* #### Comment Functionality on Movie Pages:
    This would help facilitate conversation amoung our users and help expand the userbase.
* #### Admin Functionality for Movie Inserts:
    With a larger team, admins could be used to review inserts to prevent incorrect or unsuitable data from entering the database.
* #### Links to Streaming Platforms:
    In the future we'd like to include links to where the movies are avaliable to add another source of revenue to the site.
* #### Movie Reccomendation based on Users Watchlist/Favourites:
    This feature would be added on the search bar so viewers have reccomendations rather than search for things they would like, increasing engagment. 
* #### Advanced Search Functionality:
    Currently you can search based on four filters, however the movies have more data which coould be searched by (i.e. actors).
* #### Password Reseting:
    Currently users can create accounts but that infomation is lost if the user forgets their password. As we currently save emails it can be retrievable, we just need to add a reset password feature.
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
* [GitHub Pages](https://pages.github.com/) - Used to deploy the website.
* [Google Fonts](https://fonts.google.com/) - Used for website fonts [Cinzel](https://fonts.google.com/specimen/cinzel) for headings and [Montserrat](https://fonts.google.com/specimen/Montserrat) for content text.
* [Font Awesome](https://fo*ntawesome.com/) - This library provided the Icons used across the site.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Key for testing responsive design.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to prefix the css file so that transitions would work across different browsers

## Testing
As Total Tarot has quite a few interactive elements, I wanted to test these on multiple devices to make sure they worked correctly.
To ensure this was the case these features were checked to ensure the following interactions happened:

* #### Navigation Bar
    * When hovered over, the list anchors all underline.
    * When hovered over, the dark/light mode button transitions to it's opposite picture.
    * The active page is highlighted by a different colour.
    * The Navbar collapses once small enough so the page links and mode button is hidden in the dropdown menu.

* #### Dark/Light Mode functionality
    * When clicked, all relevant coloured elements dynamically change to the correct colour.
    * The collapsed Navbar button and text in the footer swap to the opposite mode once clicked.
    * When a new page or the site is reloaded, the same mode is active from your previous visit.
    * Elements generated from JavaScript (i.e. the card info boxes in the online deck) also load with the correct colouring.

* #### Home Page
    * The images in each summary section change to icons once the small breakpoint is highlighted.
    * The copy reduces once the small breakpoint is hit.

* #### Map functionality
    * The map loads over the UK.
    * The map generates markers for all mentor locations.
    * The markers are Total Tarots icons.
    * Once clicked the relevant information appears beneath the map.
    * Once clicked the map zooms in on the marker's location.
    * When a new marker is clicked, any other information is cleared.
    * The map size changes depending on the device viewport.

* #### Online Card Library
    * All 78 cards load.
    * If the API returns an error response, an error message is displayed and the issue is logged to the console.
    * The card flips once clicked, a box loads beneath showing the user the card information.
    * When a card flips, the relevant image is called from the API.
    * If a new card is clicked, any open cards flip back and their information is hidden.

* #### Card Search function
    * All 78 card names are populated by the API.
    * Once a card is selected and the button clicked, the page smooth scrolls to the relevant card.
    * The selected card opens to reveal it's image and information.

* #### Back-To-Top Button
    * The button appears after the user scrolls 30px down.
    * The button, once clicked, instantly takes you back to the top of the page.
    * When in a hover state, the button turns gold.

* #### Learn to Interpret Page
    * The card dealing image changes size to fit different devices.
    * The accordion opens to reveal information about each layout.
    * The current accordion page closes once a new layout page is clicked.
    * The accordion content layout changes depending on the size of the device.

### Responsive Design Testing
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
Total Tarot's website was physically tested on the following browsers:
* Microsoft Edge Version 83.0.478.58 
* Chrome Version 83.0.4103.116 
* Firefox version 74.0.1 
* Safari version 13.0.5 (15608.5.11)

One note is that on FireFox the font Cinzel loads slightly differently (more elongated) but this was not considered a bug.

### Code Validation
* HTML5 code validated using [https://validator.w3.org/](https://validator.w3.org/)
* CSS3 code validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
* JS code validated using [https://jshint.com/](https://jshint.com/)
### User Stories tested
#### As a user, I want to find out more about tarot cards, so I can start using my own deck.
* The card library is easy to navigate to and provides clear information on each card.

#### As a user, I want an online deck, so I don't have to buy my own to view the cards.
* There is an online deck which is one click away from the homepage and clearly signposted.

#### As a user, I want to learn how to place my cards, so I can start doing my own readings.
* There is a page dedicated to spreads with three starter layouts clearly explained.

#### As a user, I want to easily find out where my closest classes are, so I can book a class and learn more.
* The map page has a UK-wide map showing 14 approved mentors across the UK and Ireland.

#### As a user, I want to view the cards easily, so I can browse through the cards.
* The cards are displayed so that they are all viewable and can easily be searched.

#### As the owner, I want links to social accounts, so I can grow our followers.
* Every page has links to social streams.

#### As the owner, I want a clean website, so users aren't put off and go elsewhere.
* Every page only shows the amount of information neccessary, which can be expanded upon. Less useful information is removed on smaller devices to preserve a clean and simple website.

#### As the owner, I want the information to be interactive, so users are hooked and stay on the site.
* Pages have images or interactive maps. Many educational elements respond to user inputs or breakpoints to keep it engaging.

#### As the owner, I want users to be easily directed to affilated sites, so we can get a commission of their revenue.
* The relevant information for tutors is clearly signposted and is two clicks away from the homepage and pertinent to the user.

#### As the owner, I don't want too much information available, so viewers want to get classes.
* Most information is only viewable when clicked. Once a viewer moves on to new information previous pop-ups are closed.

### Bugs
With any project bugs will arise, below is a brief summary of the most site-breaking issues:

* #### Card images wouldn't load on devices using Safari
    This bug was due to the CSS file not including the correct prefixes on transitions for browsers other than Chrome. To fix this the Autoprefixer was used to update the CSS stylesheet.
* #### Card information boxes wouldn't load with the correct dark/light mode colours
    Because the information boxes are created by JavaScript it was difficult coding the correct styling for dynamic colour changes. To fix this, code is added to the show-card-details.js at the beginning which checks the locally cached mode and adds the correct class to the divs displaying the information.
* #### Map markers wouldn't load the custom Total Tarot markers
    This bug is due to the file paths in the classes-map.js file. The relative paths were based on the JS file's location and not the page location. This was changed and now the icons load.
* #### Map Markers would only load the last populated marker information regardless of which marker was clicked.
    This bug arose because the code creating the onclick listeners, which rendered the information for each location for the markers, was outside the for loop creating them. This meant that regardless of the marker, the onclick event would only render the last marker's information because they all share the same variable name. To fix this, the function creating the listeners was moved inside the loop. Now when a marker is created the listener receives the correct location information.
* #### The light mode version of the website would load when a new page was clicked
    As the light-mode is the default version of the site, whenever a new page was clicked it would load in light mode. To solve this, the current mode was cached in the browser's local storage for the script to check before it loads a new page.
* #### The Accordion content spilt out over it's container
    Bootstrap's row class adds a negative margin to it's div elements, which was interfering with the accordion. This was fixed by changing the margin in CSS.

    
## Deployment
Total Tarot's Website was coded using the GitPod IDE. The git repository is stored loacally before being pushed online to the remote repository online at GitHub.
To push the code to the remote repository you follow these steps.
1. Save any local changes made in the GitPod IDE by pressing File -> Save All (or Ctrl+Shift+S).
2. Add these changes to the git staging area by using the ```git add .``` command in a terminal.
3. Commit the changes using the ```git commit -m "changes made"``` command.
4. Push these changes to the remote repository using the ```git push``` command.

To publish a live version of the side I used GitHub Pages, here are the steps I took:
1. Go to the remote repository at [https://github.com/SDGreen/TotalTarot](https://github.com/SDGreen/TotalTarot)
2. Click "Settings"
3. Scroll to "GitHub Pages", select a publishing source (master branch in the drop-down menu)
4. The site is now published at [https://sdgreen.github.io/TotalTarot/](https://sdgreen.github.io/TotalTarot/)

### How to run Total Tarot's website code locally:
1. Go to: [https://github.com/SDGreen/TotalTarot](https://github.com/SDGreen/TotalTarot)
2. Click the "Code" button next to the "Gitpod" button which will have a dropdown including "Clone with HTTPS", "Open with GitHub Desktop" & "Download ZIP"
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the copy to clipboard icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the copy to clipboard icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 2 (https://github.com/SDGreen/TotalTarot.git).

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
* Responsive landscape breakpoints taken from [Responsivedesign.is](https://responsivedesign.is/develop/browser-feature-support/media-queries-for-common-device-breakpoints/)
* Carousels used on user homepage created using [Slick Carousel](https://kenwheeler.github.io/slick/)
* CSS prefixer used: [https://autoprefixer.github.io/](https://autoprefixer.github.io/)
* Original movie information from [Gorochu's data on Kragge](https://www.kaggle.com/gorochu/complete-imdb-movies-dataset)
* Multiple components taken from [Materialize](http://archives.materializecss.com/0.100.2/), including the Navbar, Footer, Pagination, Cards and Form