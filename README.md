# Our Traditions

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.

## UX

As a user I want to...

- explore traditions from around the world
- search traditions to see if any are similar to traditions I share with my family, friends, colleagues or other group
- add traditions I share with my family, friends, colleagues or other group

### wireframes

[See my wireframes here](wireframes+mockups/wireframesv1.pdf)

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Design 

- Cards - I chose to make each tradition card span the full width of the screen on any device instead of four thirds of the page width on desktop (as I had originally planned). My main reason for this is that as users create the content there will more often than not be a number of cards that is not divisable by 3 and this would make the design look uneven if the layout broke the content into three quarters. 
- For my logo text I have used a gradient background and I wanted to make sure this would be compatable in all browsers. On researching this I found the only browser that does not support the background colour for text is Internet Explorer, [see documentation here.](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-text-fill-color) Therefore I have added a fallback color for that browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

### Existing Features
- Register - allows users register so that they can create content and update or delete content they have created.
- Log in - allows users who have already registered to log in to the site and manage the traditions they have added. (Also allows them to vote on other traditions)
- Add tradition - allows logged in users to add new traditions
- File upload - allows logged in users to add images to illustrate their traditions by uploading an image. The uploaded image is stored on Amazon AWS and the link retrieved and added to the image element.
- Choose an image - allows users to choose from a library of available images already uploaded and available on the site, in cases where they do not have their own image to upload. Only images relevant to teh category the user has chosen will show as available in order to provide the most relevant choices to the user.
- Edit - Allows a logged in user to edit any of the details of a tradition she has created by clicking the 'Edit' button on the tradition card and then changing the details.
- Delete - Allows a logged in user to delete any of the traditions she has created by clicking the 'Delete' button on the tradition card. When the 'Delete' button the tradition is not deleted immediately but a modal pops up asking the user to confirm that they wish to delete it. Only once they have confirmed they want to delete the tradition it is deleted.
- Read more button on card - reveals the full description of the tradition when the user clicks the 'Read more' link. If the description overflows the height of the card a scroll bar will be visible to allow the user to scroll through the content.
- Profile page - allows logged in users to see the traditions they have added and manage them by editing or deleting.

- ...allows users X to achieve Y, by having them fill out Z

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

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

### Bug fixes

- Add tradition form select field validation - the Materialize select field does not show an error when left blank, this is a known bug that the validation does not work. I fixed this with help from the Tasks Manager project in this course.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The background image for this site is from https://www.toptal.com/ 
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X