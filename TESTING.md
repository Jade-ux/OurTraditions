# Testing

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
|**As a new user I want to:**|
| Understand what the purpose of the site is| I expect to find short introduction text explaining the site purpose and for the rest of the site's content to support this purpose|On the home page I find the introduction paragraph under the heading 'Browse & Share' and it explains the site purpose and prompts me to register if I want to add my own traditions.|
| Explore all traditions on the site| I expect to be able to be able to quickly and easily find the list of traditions |  I quickly find the full list of traditions on the home page under the search options|
| Search through the traditions by keyword| When I click on 'Search by keyword', type a keyword into the input box and press 'Search


- be able to return to the page where i can browse 

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