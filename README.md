![image](https://user-images.githubusercontent.com/62659009/107788929-deebcb80-6d48-11eb-89c4-f7e147eb17bc.png)

[View live site](https://our-traditions.herokuapp.com/)

# Our Traditions

<span id="index"></span>

## Index

- <a href="#overview">Project Overview</a>
- <a href="#ux">UX</a>
- <a href="#userstories">User stories</a>
- <a href="#wireframes">Wireframes</a>
- <a href="#design">Design</a>
- <a href="#designelements">Design elements</a>
- <a href="#colours">Colours</a>
- <a href="#database">Database design</a>
- <a href="#features">Features</a>
- <a href="#existingfeatures">Existing features</a>
- <a href="#futurefeatures">Features left to implement</a>
- <a href="#technologies">Technologies used</a>
- <a href="/TESTING.md">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>
- <a href="#contents">Contents</a>
- <a href="#media">Media</a>
- <a href="#acknowledgements">Acknowledgements</a>

...

<span id="overview"></span>

## Overview 

Our Shared Traditions is a site which showcases traditions that people from all around the world follow, whether they are traditions followed by large groups, entire countries, or even traditions only followed within one family or group of friends.

The aim of the site is to allow people to learn more about other cultures and people and share some parts of their own lives. 

As the site owner, I have always been interested to learn about other cultures and customs. I would like to find out what traditions other people follow and how they are different, or perhaps even the same, as those I follow.


<div style="align: right"><a href="#index"><button>Back to index &#8593;</button></a></div>

<span id="ux"></span>

## UX



                This is a code snippet

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>


<span id="userstories"></span>

### User stories

As a user my goals are to learn more about the traditions of others and to share my own traditions.

As a **new** user I want to:

- explore all traditions on the site
- search traditions by keyword, country, category or group to see if any traditions on the site are similar to traditions I share with my family, friends, colleagues or other group
- register an account on the site in order to create content

As a user with an **existing account** I want to:

- log in easily
- add traditions I follow and categorise each by group, category and country. 
- view all the traditions I have added in one place
- edit all sections of the traditions I have added 
- delete a tradition if I no longer want it on the site
- logout when I have finished managing my traditions

As a site owner my goals is to encourage users to add their traditions so that all users can enjoy the content. My aim is to have the site filled with user-created content from around the world, from a diverse range of cultures and a wide range of categories and groups.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="wireframes"></span>

### Wireframes

[See my wireframes here](wireframes+mockups/wireframes.pdf)

data schema? Sitemap? 

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="design"></span>

## Design 

How I came to the decision of dark colours and 

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="designelements"></span>

### Design elements

- Cards - I chose to make each tradition card span the full width of the screen on any device instead of four thirds of the page width on desktop (as I had originally planned). My main reason for this is that as users create the content there will more often than not be a number of cards that is not divisable by 3 and this would make the design look uneven if the layout broke the content into three quarters. 
- For my logo text I have used a gradient background and I wanted to make sure this would be compatable in all browsers. On researching this I found the only browser that does not support the background colour for text is Internet Explorer, [see documentation here.](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-text-fill-color) Therefore I have added a fallback color for that browser.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="colours"></span>

### Colours

I chose a warm colour palette to elicit feelings of warmth and comfort. When I decided on the colours I was imagining telling stories around the camp fire, which is one of the earliest traditions I can think of. The following colours remind me of fire and warmth:

[See colour accessibility here](wireframes+mockups/colour-accessibility.pdf)colour-accessibility.pdf

#D2430F

Accessibility:

White text on #D2430F background on .orange-button meets 


### Fonts
?? (required?)

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="database"></span>

## Database design 

I chose to limit what users can add to the site to their traditions. There is no way to add new countries because I wanted to make sure that the list remained accurate. There is also no way to add new groups or categories as I wanted to keep those lists concise and I believe they cover all groups/categories needed.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="collections"></span>

## Collections

The database is called 'ourTraditions' and contains the following collections:

### Traditions

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId|Auto-generated by MongoDB when a new tradition is added.|
|tradition_name|string|Name the user chooses for their tradition, must be between 3-50 characters.|
|category_name|string|Category user chooses, limited by list from categories collection.|
|group_name|string|Group user chooses, limited by list from group collection.|
|country|string|Country user chooses, limited by list from country collection.|
|tradition_description|string|Description that the user adds, must be between 10-300 characters.|
|created_by|string|Group user chooses, limited by list from group collection.|

### Categories

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId|Auto-generated by MongoDB when categories were added.|
|category_name|string|Pre-defined in development and cannot be changed.|

### Countries

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId|Auto-generated by MongoDB when countries were added.|
|country_name|string|Pre-defined in development and cannot be changed.|

### Groups

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId|Auto-generated by MongoDB when groups were added.|
|group_name|string|Pre-defined in development and cannot be changed.|

### Users

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId|Auto-generated when a new user registers on the site.|
|username|string|Name the user chooses when they register.|
|password|string|Hashed password.|

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="features"></span>

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

<span id="existingfeatures"></span>

### Existing Features

1. Register - allows users register so that they can create content and update or delete content they have created.

2. Log in - allows users who have already registered to log in to the site and manage the traditions they have added. (Also allows them to vote on other traditions)

3. Add tradition - allows logged in users to add new traditions

4.  File upload - allows logged in users to add images to illustrate their traditions by uploading an image. The uploaded image is stored on Amazon AWS and the link retrieved and added to the image element.

5.  Choose an image - allows users to choose from a library of available images already uploaded and available on the site, in cases where they do not have their own image to upload. Only images relevant to teh category the user has chosen will show as available in order to provide the most relevant choices to the user.

6. Edit - Allows a logged in user to edit any of the details of a tradition she has created by clicking the 'Edit' button on the tradition card and then changing the details.

7. **Country field** allows users to choose which country they are in when adding a tradition. This will allow users to see which traditions exist in each country.

7. **The delete feature** allows a logged in user to delete any of the traditions she has created by clicking the 'Delete' button on the tradition card. When the 'Delete' button the tradition is not deleted immediately but a modal pops up asking the user to confirm that they wish to delete it. Only once they have confirmed they want to delete the tradition it is deleted.

8. **The read more button on card** reveals the full description of the tradition when the user clicks the 'Read more' link. If the description overflows the height of the card a scroll bar will be visible to allow the user to scroll through the content.

9. **The profile page** allows logged in users to see the traditions they have added and manage them by editing or deleting.

- ...allows users X to achieve Y, by having them fill out Z

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

<span id="futurefeatures"></span>

### Features Left to Implement
- Voting
- Pagination 

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="technologies"></span>

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) - the front-end structure of this app is written in HTML
- [CSS](https://en.wikipedia.org/wiki/CSS) - this app is styled with CSS
- [JavaScript](https://www.javascript.com/) - used for DOM manipulation
- [JQuery](https://jquery.com) - used to simplify DOM manipulation
- [Python](https://www.python.org/) - the app functionality and data manipulation is written in Python.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - the app uses the Flask microframework to simplify the website build. Flask depends on Jinja and Werkzeug.
- [Jinja](https://werkzeug.palletsprojects.com/en/1.0.x/) - the Jinja templating engine is used to inject data onto the website pages.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - this provides tools required by Flask. It is also used to generate a password hash for registered users and to ensure secure file names for uploaded images.
- [Materialize 1.0.0](https://materializecss.com/) - this front-end framework was used to speed us the front-end development of this app.
- [Balsamiq](https://balsamiq.com/) - wireframes for this app were created with the Balsamiq wireframing tool.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - this is a helper for Python Imaging Library which I used to manipulate and resize images.
- [Amazon S3](https://docs.aws.amazon.com/s3/index.html?nc2=h_ql_doc_s3) - this project uses Amazon S3 to store images uploaded by users 
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - this is the Amazon AWS software development kit for Python, this is used for uploading images from user input to Amazon S3.
- [BytesIO](https://docs.python.org/3/library/io.html) - is used in the image uploading function to manipulate string and bytes data in memory
- [Mongo DB](https://www.mongodb.com/) - is the database management system used for this app's non-relational database.
- [Heroku](https://dashboard.heroku.com/apps) - is the cloud platform used to host the deployed app.
- Testing - for technologies used for testing, please see my <a href="/TESTING.md">Testing file</a>

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

## Testing

For testing please see my testing page here: <a href="/TESTING.md">Testing</a>.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>


<span id="deployment"></span>

## Deployment

**Differences between development site and deployed site:**

There are no differences between the development site and deployed site. The development site is deployed on the Master branche and I have tested each section on the deployed site to ensure each looks the same and functions in the same way as the development site.

....

<span id="mongo"></span>

**For MongoDB:**

- Use SCRAM method to create a username and password
- Make sure to not use any special characters in your password 
- Make sure your user priviledges are set to 'Read and write to the database'.
- Click 'Add user'
- In the 'Network access' tab, click 'Add IP address' and then select 'Allow access from anywhere' because you will be accessing the DB from your IDE and Heroku. OR, for added security, restrict this to the IP address of your hosts.
- Once your cluster has been provisioned click 'collections' and then 'Add My Own Data'.
- Add your database name and the name of your first collection. 
- Once your database is created you can add the rest of the collections, [see all the collections you will need here](#collections). 
- Access your MONGO_URI for your env.py file and Heroku config vars by clicking 'Connect' (in your cluster), then select 'Connect your application', choose Python and the correct version and then copy your connection string
- Back in your IDE add this to your env.py file and replace `<password>` with your password and `<dbname>` with your database name.

**In Heroku**

1. In Heroku add your config vars (in the 'settings' tab > click 'Reveal config vars')

|**Key**|**Value**|
|IP|`0.0.0.0`|   
|PORT|`5000`|
|SECRET_KEY| `<your secret key from MongoDB>`|
|MONGO_URI|`<your MongoDB URI>`|
|MONGO_DBNAME|| `<your database name>`
|S3_BUCKET|`<your bucket name>`|
|S3_KEY|`<your S3 bucket key>`|
|S3_SECRET_ACCESS_KEY|`<your S3 secret key>`|
|S3_LOCATION|`<your S3 location URL>`|

2. Add your env.py file to your .gitignore file to ensure none of your secret keys are pushed to your repository. 

<span id="amazonaws"></span>

## Setting up your Amazon S3 account to host uploads

I used Amazon S3 to allow users to upload images to the site to accompany their traditions. These are the steps I took and the steps you can take when cloning my site:

1. Create an Amazon AWS account
2. Create a bucket within your account
3. Under your name (top right of the management console) click 'My security credentials' Open 'Access keys...'
3. Click 'Create New Access Key'.
4. Save the file to your computer
5. From the main menu select 'IAM' and then 'Create new user'
5. In your app install boto3: <code>pip install flask boto3</code>
6. Add the following to your env.py file and your app's config vars in Heroku:

|**Key**|**Value**|
|S3_BUCKET|`<your bucket name>`|
|S3_KEY|`<your S3 bucket key>`|
|S3_SECRET_ACCESS_KEY|`<your S3 secret key>`|
|S3_LOCATION|`<your S3 location URL>`|

7. You should now be able to connect to your Amazon S3 bucket.


**If you would like to run my code locally you can clone the site by following these steps:**

1. Visit the main page of my repository on [GitHub here](https://github.com/Jade-ux/OurTraditions).
2. Click 'Clone or download'
3. Click the icon to the right of the URL. This will allow you to clone the repository using HTTPS.
4. If you would like to clone it using SSH, click 'Use SSH'
5. On your computer open Git Bash
6. Change the directory to the folder where you would like to run the cloned directory
7. Type 'Git clone' and then paste the URL you copied from my repository in GitHub
8. Press enter and your local clone of my site will be created.
9. Install each of the requirements from the requirements.txt file or run the following code:

                pip -r requirements.txt

10. You will then need to create your own database on MongoDB, please follow the <a href="#mongo">steps for MongoDB</a> above
11. Add your Mongo DB configuration variables to your env.py file
12. Set up your Amazon AWS account <a href="#amazonaws">following the steps above</a>.
13. Add your S3 access key, secret key, location and bucket name to your env.py file.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="credits"></span>

## Credits

- [This tutorial helped me build an image uploader](https://www.youtube.com/watch?v=6WruncSoCdI) 
- I also recieved help from Ed Bradley to create the image uploader
- [Documentation for how to create an Amazon AWS policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-policies-s3.html#iam-policy-ex4)
- [To set up my Amazon account I used this tutorial.](https://www.youtube.com/watch?v=v33Kl-Kx30o)
- [For help with Python's string manipulation syntax in Jinja I used this guide.](https://shubhamjain.co/til/capitalizing-first-letter-in-jinja/)

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="content"></span>

### Content
- All content is written by me

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="media"></span>

### Media
- The background image for this site is from [Toptal](https://www.toptal.com/) 
- The photo used on this site was obtained from Laura Riviera on [Unsplash](https://unsplash.com/) and edited to remove the background.
- For testing purposes I have uploaded a few images to the tradition cards, these are also from [Unsplash](https://unsplash.com/)
- All other photos on the site are uploaded by users.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>


<span id="acknowledgements"></span>

### Acknowledgements

- I received inspiration for this project from my team at Hexagon when we were discussing the different traditions we all celebrate over Christmas and New Year.
<<<<<<< HEAD
- Thank you to the Code Institute Tutors for help with a snagging issue
- Thank you to Ed Bradley and Chris Palmer for their invaluable help through some of my coding questions
- Thank you to my mentor Dick Vlaanderen for guidance on my project
=======
- Thank you to the Code Institute Tutors for help with a coding question
- Thank you to Ed Bradley, Chris Palmer and Jose for their invaluable help testing my site
- Thank you to my mentor Dick Vlaanderen for guidance on my project
>>>>>>> 251bbc3 (Updated README and TESTING files.)
