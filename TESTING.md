# Testing

<a href="/README.md">Back to main README file</a>

<span id="index"></span>

## Index

- <a href="#tech">Technologies used</a>
- <a href="#ux">User stories</a>
- <a href="#func">Functionality</a>
- <a href="#resp">Responsive design and cross-browser testing</a>
- <a href="#code">Code validity</a>
- <a href="#bugs">Bugs and bugs fixed</a>

<span id="tech"></span>

## Technologies used for testing:

- [W3C Markup Validation Service](https://validator.w3.org/) - used to validate HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - used to test CSS code validation
- [JSHint](https://jshint.com/) - used to test for JavaScript code validity
- [Lighthouse](https://developers.google.com/web/tools/lighthouse_) - used for testing front-end best practice
- [Pep8 checker](http://pep8online.com/) - used for testing Python code against Pep8 guidelines

<div style="align: right"><a href="#index"><button>Back to index &#8593;</button></a></div>

<span id="ux"></span>

## User stories


|**User story**|**Expected outcome**|**Actual outcome**|
|:-----|:-----|:-----|
|**As a user I want to:**|||
|Understand what the purpose of the site is|I expect to find short introduction text explaining the site purpose and for the rest of the site's content to support this purpose|On the home page I find the introduction paragraph under the heading 'Browse & Share' and it explains the site purpose and prompts me to register if I want to add my own traditions.|
|Explore all traditions on the site| I expect to be able to be able to quickly and easily find the list of traditions |  I quickly find the full list of traditions on the home page under the search options|
| Search through the traditions by keyword| When I click on 'Search by keyword', type a keyword into the input box, eg. 'birthday' and press 'Search' I expect to see a list of traditions related to birthdays. | When I search the keyword 'birthdays' results appear under the search accordions and the results all contain the keyword searched, either in their title, description, or one of the categories. Or, a message appears telling me that there are no results for my search if no traditions contain the keyword I searched.|
|Reset the search to show all traditions again| When I press the 'reset' button I expect to see all traditions again.| When I press the 'reset' button all traditions now show under the search accordions.|
|Search by country| When I select an option from the country select field and press enter, I expect to see traditions that match my search appear| When I click on the accordion for country and then click the field to see the options, I can see a limited list of options. This is showing me only the countries for which traditions exist on the site. I select the country I want to search by and the results that show are only for that country.|
|Search by group| When I select an option from the group select field and press enter, I expect to see traditions that match my search appear| When I click on the accordion for group and then click the field to see the options, I can see a limited list of options. This is showing me only the countries for which traditions exist on the site. I select the group I want to search by and the results that show are only for that group.|
|Search by category| When I select an option from the category select field and press enter, I expect to see traditions that match my search appear| When I click on the accordion for category and then click the field to see the options, I can see a limited list of options. This is showing me only the countries for which traditions exist on the site. I select the category I want to search by and the results that show are only for that category.|
|Register an account to be able to add content | I expect to find the register link/menu item easily and be able to register quickly| I find the 'Register' navigation item at the top of the page easily. On the 'Register' page I am prompted to add a username and password with hints for the format for each. Once I have entered my details and pressed 'Register' I am taken to a 'Profile' page where I see a message telling me that my registration has been successful. There is a message telling me what the page is for and a button to 'Add a tradition.'|
|Add a tradition| I expect to be able to easily find where to add a tradition and to be able to add the details required easily and with prompts along the way. Once I have added my tradition I expect to see it appear in the list of traditions on the home page and on my profile page. | I find the 'Add tradition' link in the navigation bar. Once on the 'Add tradition' page I see a form which tells me what to enter into each field. I enter the tradition name, choose a category, group and country, each from pre-defined lists and then write a description for my tradition. I upload an image of any size. If I try to click 'Add tradition' before completing any of the fields an error shows on the empty field telling me to fill it in. If I have not entered enough information in any of the fields the line under the field shows as red, showing me that the field has not been completed correctly. When I have completed all fields correctly and click 'Add tradition' I see a message telling me that my tradition has been added. My tradition now shows on the home page in the traditions list and on my profile page, with all the details I entered. |
| Edit a tradition I have added | I expect to easily see how I can edit one of my traditions. I expect to be able to edit every section of my traditions and save the changes, then see the edited tradition in the traditions list. | When I am logged in I see an 'Edit' button on my traditions. If I click it I am taken to a page which shows all my tradition's information in a form. I can edit each field and then click 'Save changes'. I see a message that tells me my tradition has been updated. When I navigate to the 'Browse' page I see my tradition with the updated information.|
|Delete a tradition|I expect to easily see how I can delete a tradition and be able to permenantly delete any tradition that belongs to me. I do not expect to be able to delete other people's traditions. |When I am logged in I see a 'delete' button on traditions I have added. When I click it a model pops up, asking me whether I am sure I want to delete the item. If I click 'No' the tradition is not deleted. If I click 'Yes' the tradition is deleted and I no longer see it in the list of traditions on the home page and on my profile page.|
|Logout| I expect to easily find a way to logout| I find the 'logout' item in the menu and when I click it I see a message telling me that I have been logged out.|


<div style="align: right"><a href="#index"><button>Back to index &#8593;</button></a></div>

<span id="func"></span>

## Functionality 



### Search form



<div style="align: right"><a href="#index"><button>Back to index &#8593;</button></a></div>

<span id="resp"></span>

## Responsive design and cross-browser testing

<div style="align: right"><a href="#index"><button>Back to index &#8593;</button></a></div>

<span id="code"></span>

## Code validity


<div style="align: right"><a href="#index"><button>Back to index &#8593;</button></a></div>

<span id="bugs"></span>

## Bugs and bugs fixed

- Add tradition form select field validation - the Materialize select field does not show an error when left blank, this is a known bug that the validation does not work. I fixed this with help from the Tasks Manager project in this course.
- Select field on forms: The materialize class adds a white dot under the select items. This was fixed by setting it as 'display: none'
- Select field on mobile: on mobile Materialize bug shows a down arrow on select fields for the validate message. [Fixed this with help from the Stackexchange resource here](https://stackoverflow.com/questions/52850091/materialize-select-and-dropdown-touch-event-selecting-wrong-item/52851046#52851046) 
- The valid_images() function should check the file type and not upload the file if it is not one of the allowed types. It should then not allow the upload,however this is currently not working and a user is able to upload a file that is not an image file. This bug is oustanding, however, to handle this I have set the form field in the HTML to only accept files with the extensions: .jpg, .jpeg, .png, .gif
- Tradition titles: Jinja does not have a sentence case function, only capitalize() and upper(). I wanted to make sure the tradition titles would appear in sentence case if added that way, to allow for proper nouns. I used Python's string manipulation syntax to achieve this. [I found this guide helpful.](https://shubhamjain.co/til/capitalizing-first-letter-in-jinja/)

<div style="align: right"><a href="#index"><button>Back to index &#8593;</button></a></div>


In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.