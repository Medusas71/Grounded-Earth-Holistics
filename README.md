<h1 align="center">Grounded Earth Holistics</h1>

<h3>Milestone Four Project - Full Stack Frameworks With Django</h3>
<br>

[View the deployed Grounded Earth Holistics](https://grounded-earth-holistics.herokuapp.com/)

**Please note: To open any links in this document in a new browser tab, press 'CTRL + Click'.**

<a id=#table-of-contents></a>
# Table of Contents
<details open>
<summary><b>(click to expand or hide)</b></summary>
<!-- Markdown TOC -->

1. [Description](#description)
2. [User Experience (UX)](#user-experience-(ux))
   * [User Stories](#user-stories)
   * [5 Planes](#5-planes)
     1. [Strategy](#strategy)
     2. [Scope](#scope)
     3. [Structure](#structure)
     4. [Skeleton](#skeleton)
     5. [Surface](#surface)
3. [Features](#features)
   * [Current Features](#current-features)
   * [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Lessons Learned](#lessons-learned)
7. [Deployment](#deployment)
8. [Credits](#credits)

<!-- /Markdown TOC -->
</details>

<a id="description"></a>
# Description  

I am currently studying the Full Stack Development Course through Code Institute. Part of the course I am required to complete 4 milestone projects. Grounded Earth Holistics is my 4th milestone project which is part of the Full Stack Frameworks with Django.

Grounded Earth Holistics is an e-commerce site that has been created for customers that would like a holistic experience. This experience includes a deeply relaxing session with either Tuning Forks or healing crystals. Customers can purchase various products through a secure checkout.

Some of the content and all images have been copied from [Grounded Earth Holistics](https://www.groundedearthholistics.com.au/) with their permission.

[Back to Table of Contents](#table-of-contents)

<a id="user-experience-(ux)"></a>
# User Experience (UX)

<a id="user-stories"></a>
## User Stories  

First Time Customer Goals

* As a first time customer to the website, I would like to:
  * search for products
  * see the number of products that are available
  * view all products
  * view individual product details
  * sort the list of available products by price
  * sort the list of available products by category
  * read reviews about a product
  * view holistic services
  * increase and decrease the item quantity
  * be able to purchase products through a secure checkout
  * view items in my shopping bag
  * adjust items in my shopping bag
  * receive confirmation that the products have been purchased
  * create an account
  * receive confirmation that the account has been created

Returning Customer Goals

* As a returning customer to the website, I would like to:
  * have the ability to log in so my information is saved
  * be able to log out of the site
  * recover my password in case I forget it
  * create, update and delete my own reviews
  * read other reviews

Site Owner Goals

* As a site owner of the website, I would like to:
  * be able to add products
  * be able to edit products
  * be able to delete products

[Back to Table of Contents](#table-of-contents)

<a id="5-planes"></a>
## 5 Planes

<a id="strategy"></a>
### 1. Strategy

The purpose of this project is to create an e-commerce site where users can purchase holistic products through a secure checkout and view what holistic services are available.

<a id="scope"></a>
### 2. Scope

The features of this project will include:

* The ability to:
  * search for products
  * view products
  * view services
  * register to save their personal information
  * log in and out
  * purchase products through a secure checkout
  * have the site owner add, edit and delete products

<a id="structure"></a>
### 3. Structure

The information is grouped logically for all users. The Interaction Design (IXD) will be consistent between pages where the navigation bar is fixed and tailored to have the priority items displayed first at the top of the screen. The footer will scroll with the page. A user can either search, view or purchase products through a secure checkout or log in to save their information. The site will be consistent with what users expect from an e-commerce store.

<a id="skeleton"></a>
### 4. Skeleton

The [wireframes](./static/documents/wireframes/grounded-earth-holistics.pdf) have been created using [Balsamiq](https://balsamiq.com) and were created for Desktop, Tablet and Phone. 

Here are the individual wireframes:

* [Home Page Wireframe](static/images/readme-images/wireframes/home-page.png)
* [Holistic Services - Tuning Therapy Wireframe](static/images/readme-images/wireframes/holistic-services-tuning-therapy.png)
* [Holistic Services - Grounding Wireframe](static/images/readme-images/wireframes/holistic-services-grounding.png)
* [Products Wireframe](static/images/readme-images/wireframes/products.png)
* [Individual Products Wireframe](static/images/readme-images/wireframes/individual-products.png)
* [About Wireframe](static/images/readme-images/wireframes/about.png)
* [Log In Wireframe](static/images/readme-images/wireframes/login.png)
* [Register Wireframe](static/images/readme-images/wireframes/register.png)
* [Product Management Wireframe](static/images/readme-images/wireframes/product-management.png)
* [Shopping Bag Wireframe](static/images/readme-images/wireframes/shopping-bag.png)
* [Checkout Wireframe](static/images/readme-images/wireframes/checkout.png)
* [Thank You Wireframe](static/images/readme-images/wireframes/thank-you.png)

<a id="surface"></a>
### 5. Surface 

Colour Scheme

* The original colour scheme of the existing website did not pass the accessibility test so I used colours that had an earthy feel about them.
* After googling earthy colours I found [this colour scheme](https://www.schemecolor.com/everything-is-earthy-color-scheme.php) by [schemecolor.com](https://www.schemecolor.com/).
* I used #ECB984 (Middle Yellow Red) as the background colour for the header and footer.
* For the free postage banner I took the colour #D58258 and changed the contrast colour to #765032 (Coffee) so it would pass accessibility. These 2 colours compliment each other.
* The pages have a white #FFFFFF background.
* The text is all in black #000000.

![4 Colours](static/images/readme-images/website-colours.jpg)
Colours were displayed using [Coolors](https://coolors.co/ecb984-765032-000000-ffffff).

* The colours were checked through [WebAIM](https://webaim.org/resources/contrastchecker/) to ensure the final colours were accessible.

![WebAIM Contrast Checker](static/images/readme-images/webaim-contrast-checker.jpg)
![WebAIM Contrast Checker](static/images/readme-images/webaim-contrast-checker1.jpg)

Typography

* The fonts were sourced from [Google Fonts](https://fonts.google.com/).
* The main text font I used the same as the original website which is the font family of Raleway.
* The font from the original website for headings was Jubilat, which is not from Google Fonts.
* I then googled Raleway font pairing and found a match on [Figma](https://www.figma.com/google-fonts/raleway-font-pairings/#:~:text=Raleway%20font%20pairing,PT%20Sans%2C%20and%20Open%20Sans.).
* I selected Merriweather for all headings.
* The backup font for both the headings and the main text is Sans Serif.

Imagery

* All imagery was sourced from [Grounded Earth Holistics](https://www.groundedearthholistics.com.au/) with permission from the site owner.

[Back to Table of Contents](#table-of-contents)

<a id="features"></a>
# Features

<a id="current-features"></a>
**Current Features**

Each page features:

* A header that consists of:
  * Free postage banner
  * The name of the site
  * A search bar
  * My Account icon where you can Register and Login
  * A Shopping Bag icon with the amount spent
  * A navbar consisting of Holistic Services, All Products, Crystals, Candles & Candle Holders, Bath Luxuries, Cacao and Gift Packs
* A footer that consists of About, Copyright and Developed By, a Facebook and Instagram Link

The Home Page features:

* The name of the website
* Information about what the website is about
* An image
* A Shop Now button

The Holistic Services dropdown features:

* Tuning Therapy which directs you to learn all about Tuning Therapy
* Grounding which directs you to learn all about Grounding techniques

The All Products dropdown features:

* All products by price or category - This displays all products by price and the customer can either sort by:
  * Price (low to high)
  * Price (high to low)
  * Name (A-Z)
  * Name (Z-A)
  * Category (A-Z)
  * Category (Z-A)

The other nav items include:

* Crystals, Candles & Candle Holders, Bath Luxuries, Cacao and Gift Packs
* Each individual dropdown displays the appropriate products for that category which include:
  * An image of the product
  * The name of the product
  * The price of the product
  * The category of the product
* All products are able to be sorted as advised above
* The number of products displays for the user

All products you can click the image and the product will display in its own page where you can select the quantity and add to bag.

The My Account icon in the header allows a customer to either Log In or Register.

A logged in user can select My Profile from My Account which will display their default delivery information and order history.

The Shopping Bag:

* The Shopping Bag icon displays the amount that is to be charged, after adding products to the shopping bag
* Gives the customer the option to increase or decrease the quantity and update their shopping bag
* Gives the customer the option to remove an item from the shopping bag
* Advises the bag total, delivery fee, grand total, how much more you can spend to get free delivery
* Gives the customer a link to keep shopping
* Gives the customer a link to the secure checkout

The Checkout displays:

* A form for the customer to complete with their relevant name, email, phone number and postal details of where to send the product to
* An order summary of what the customer is about to purchase
* A payment field where the customer can add their credit card details
* An adjust bag link if the customer needs to adjust their purchase
* A complete order link
* An information prompt that displays how much the customers credit card will be charged

The Complete Order link displays:

* A success message in the top right hand corner
* A thank you page that provides all the order information
* That a confirmation email will be sent to the customer

Super User / Site Owner:

* A Super User / Site Owner will also have the option after logging in to be able to go to the Product Management page
* The Product Management page allows the site owner to add a product
* Can also go to any product and either edit the product or delete the product

<a id="future-features"></a>
**Future Features to implement**

[Back to Table of Contents](#table-of-contents)

<a id="technologies-used"></a>
# Technologies Used

**Languages**

1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
2. [CSS3](https://en.wikipedia.org/wiki/CSS)
3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
4. [Python 3](https://www.python.org/)

**Frameworks and Libraries**

1. [Bootstrap 4.6 CDN](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - to make the website responsive
1. [Django](https://www.djangoproject.com/) - a high-level Python web framework used for development of the site
1. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - used as a templating engine for Python
1. [jQuery](https://developer.mozilla.org/en-US/docs/Glossary/jQuery) - used for the Toasts

**Programs and Resources**

1. [Am I Responsive](https://ui.dev/amiresponsive) - to create a Home Page image on each device for use in the Readme file
1. [Autoprefixer CSS Online](https://autoprefixer.github.io/) - to ensure all vendor prefixes were included in CSS
1. [AWS](https://aws.amazon.com/) - a cloud application to hold media files
1. [Balsamiq](https://balsamiq.com/) - wireframes
1. [Code Institute Course Content](https://learn.codeinstitute.net/login?next=/) - main source of fundamental knowledge including the Boutique Ado walk through project
1. [Coolors](https://coolors.co/) - to display colour palette
1. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) - to generate secret keys
1. [Favicon Generator](https://favicon.io/emoji-favicons/) - to generate the favicon
1. [Figma](https://www.figma.com) - for font pairing
1. [Font Awesome](https://fontawesome.com/v5/search) - for their icons
1. [Git](https://git-scm.com/) - version control
1. [GitHub](https://github.com/) - used to store the project files
1. [Gitpod](https://www.gitpod.io/) - IDE
1. [Google Fonts](https://fonts.google.com/) - typography
1. [Heroku](https://id.heroku.com/login) - a container-based cloud Platform as a Service (PaaS) used to deploy the project
1. [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - to check for issues on all pages
1. [Scheme Color](https://www.schemecolor.com) - for ideas on earthy colours
1. [Slack](https://slack.com/) - main source of assistance from other students, developers and documents/resources
1. [Snagit](https://www.techsmith.com/screen-capture.html) - screen capture and resizing images
1. [Stripe](https://stripe.com/au) - for secure payments in the checkout
1. [TinyPNG](https://tinypng.com/) - efficient compression of images for the site
1. [W3Schools](https://www.w3schools.com/) - to assist with the code
1. [Wave](https://wave.webaim.org/) - to ensure the content was accessible
1. [WebAIM](https://webaim.org/resources/contrastchecker/) - web accessibility contrast checker

[Back to Table of Contents](#table-of-contents)

<a id="testing"></a>
# Testing

[See Testing.md for testing information](TESTING.md)

[Back to Table of Contents](#table-of-contents)

<a id="lessons-learned"></a>
# Lessons Learned

[Back to Table of Contents](#table-of-contents)

<a id="deployment"></a>
# Deployment

**How to Fork a Repository**

**Run this site locally/clone site**

[Back to Table of Contents](#table-of-contents)

<a id="credits"></a>
# Credits

Code

Content  

Media

Acknowledgements

[Back to Table of Contents](#table-of-contents)