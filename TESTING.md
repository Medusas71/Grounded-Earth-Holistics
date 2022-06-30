<h1 align="center">Grounded Earth Holistics - Testing Details</h1>

[View the main README.md document](README.md)

[View the deployed Grounded Earth Holistics](https://grounded-earth-holistics.herokuapp.com/)

**Please note: To open any links in this document in a new browser tab, press 'CTRL + click'.**

<a id=#table-of-contents></a>
# Table of Contents
<details open>
<summary><b>(click to expand or hide)</b></summary>
<!-- MarkdownTOC -->

[Testing](#testing)
* [Validators](#validators)
* [Lighthouse](#lighthouse)
* [Wave Report](#wave)
* [User Stories](#user-stories)
* [Manual Testing](#manual-testing)
* [Bugs/Fixes](#bugs-fixes)

<!-- /MarkdownTOC -->
</details>

<a id="testing"></a>
# Testing

Testing was conducted manually and through different validator services on each page of the website.

<a id="validators"></a>
## Validators

* [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) was used on each page to ensure 
that there were no errors or warning in my HTML document. I have a few errors and warnings display as per the below screenshot:

![W3C HTML Validation Results1](/static/images/testing-images/w3c/warning1.jpg)

* This warning is to do with not having headers in the correct place. This has been ignored as the area it is referring to 
doesn't have headings.

![W3C HTML Validation Results2](/static/images/testing-images/w3c/errors_warnings.jpg)

* The error and warnings that display are due to being able to decrease the quantity value in the shopping bag.  
Unfortunately due to time restraints I haven't been able to fix this. This will be fixed after completing the course.

![W3C HTMl Validation Results3](/static/images/testing-images/w3c/error.jpg)

* This error I have found very confusing. I don't understand how to fix it, even after researching it on Stack Overflow. 
Unfortunately due to time restraints this error will get looked into more closely after I have completed the course.

*[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to ensure that there were no errors or warnings in my CSS document and validated by direct input. I had no errors or warning display.

![W3C CSS Validation Results](/static/images/testing-images/w3c/css-validation-results.jpg)

* [Autoprefixer CSS Online](https://autoprefixer.github.io/) was used to ensure that all vendor prefixes 
were included in CSS. the results were copied into the style.css file.

* [Pep8](http://pep8online.com/) was used to check every .py file. No errors or warnings displayed.

![pep8](/static/images/testing-images/pep8.jpg)

[Back to Table of Contents](#table-of-contents)

<a id="lighthouse"></a>
## Lighthouse 

Lighthouse was used to check for any problems on all pages. Unfortunately the scores were not as high as I would have liked. My heart sunk, especially as due to time restraints I haven't been able to look into these issues. It is something that will be addressed once the course is finished and I have more time to spend on each issue. 

Below is the lighthouse score for each page on mobile and desktop:

<details open>
<summary><b>(click to expand or hide)</b></summary>

### index.html - mobile

![index-mobile-lh](/static/images/testing-images/lighthouse/index-mobile-lh.jpg)

### index.html - desktop

![index-desktop-lh](/static/images/testing-images/lighthouse/index-desktop-lh.jpg)

### Holistic Services - Tuning Therapy - mobile

![tuning-therapy-mobile-lh](/static/images/testing-images/lighthouse/tuning-therapy-mobile-lh.jpg)

### Holistic Services - Tuning Therapy - desktop

![tuning-therapy-desktop-lh](/static/images/testing-images/lighthouse/tuning-therapy-desktop-lh.jpg)

### Holistic Services - Grounding - mobile

![grounding-mobile-lh](/static/images/testing-images/lighthouse/grounding-mobile-lh.jpg)

### Holistic Services - Grounding - desktop

![grounding-desktop-lh](/static/images/testing-images/lighthouse/grounding-desktop-lh.jpg)

### All Products - mobile

![all-products-mobile-lh](/static/images/testing-images/lighthouse/all-products-mobile-lh.jpg)

### All Products - desktop

![all-products-desktop-lh](/static/images/testing-images/lighthouse/all-products-desktop-lh.jpg)

### Crystals - mobile

![all-crystals-mobile-lh](/static/images/testing-images/lighthouse/all-crystals-mobile-lh.jpg)

### Crystals - desktop

![all-crystals-desktop-lh](/static/images/testing-images/lighthouse/all-crystals-desktop-lh.jpg)

### Bath Salts - mobile

![bath-salts-mobile-lh](/static/images/testing-images/lighthouse/bath-salts-mobile-lh.jpg)

### Bath Salts - desktop

![bath-salts-desktop-lh](/static/images/testing-images/lighthouse/bath-salts-desktop-lh.jpg)

### Cacao - mobile

![cacao-mobile-lh](/static/images/testing-images/lighthouse/cacao-mobile-lh.jpg)

### Cacao - desktop

![cacao-desktop-lh](/static/images/testing-images/lighthouse/cacao-desktop-lh.jpg)

### Gift Packs - mobile

![gift-packs-mobile-lh](/static/images/testing-images/lighthouse/gift-packs-mobile-lh.jpg)

### Gift Packs - desktop

![gift-packs-desktop-lh](/static/images/testing-images/lighthouse/gift-packs-desktop-lh.jpg)

### About - mobile

![about-us-mobile-lh](/static/images/testing-images/lighthouse/about-us-mobile-lh.jpg)

### About - desktop

![about-us-desktop-lh](/static/images/testing-images/lighthouse/about-us-desktop-lh.jpg)

### Review - Add a review - mobile

![add-review-mobile-lh](/static/images/testing-images/lighthouse/add-review-mobile.lh.jpg)

### Review - Add a review - desktop

![add-review-desktop-lh](/static/images/testing-images/lighthouse/add-review-desktop-lh.jpg)

### Review - Delete a review - mobile

![delete-review-mobile-lh](/static/images/testing-images/lighthouse/delete-review-mobile-lh.jpg)

### Review - Delete a review - desktop

![delete-review-desktop-lh](/static/images/testing-images/lighthouse/delete-review-desktop-lh.jpg)

### Comments - Add a comment - mobile

![add-comment-mobile-lh](/static/images/testing-images/lighthouse/add-comment-mobile-lh.jpg)

### Comments - Add a comment - desktop

![add-comment-desktop-lh](/static/images/testing-images/lighthouse/add-comment-desktop-lh.jpg)

### Shopping Bag - mobile

![shopping-bag-mobile-lh](/static/images/testing-images/lighthouse/shopping-bag-mobile-lh.jpg)

### Shopping Bag - desktop

![shopping-bag-desktop-lh](/static/images/testing-images/lighthouse/shopping-bag-desktop-lh.jpg)

### Checkout - mobile

![checkout-mobile-lh](/static/images/testing-images/lighthouse/checkout-mobile-lh.jpg)

### Checkout - desktop

![checkout-desktop-lh](/static/images/testing-images/lighthouse/checkout-desktop-lh.jpg)

### Thank You Page / Checkout Success - mobile

![checkout-success-mobile-lh](/static/images/testing-images/lighthouse/checkout-success-mobile-lh.jpg)

### Thank You Page / Checkout Success - desktop

![checkout-success-desktop-lh](/static/images/testing-images/lighthouse/checkout-success-desktop-lh.jpg)

### Login Page - mobile

![Login-mobile-lh](/static/images/testing-images/lighthouse/login-mobile-lh.jpg)

### Login - desktop

![Login-desktop-lh](/static/images/testing-images/lighthouse/login-desktop-lh.jpg)

### Log Out Page - mobile

![Logout-mobile-lh](/static/images/testing-images/lighthouse/sign-out-mobile-lh.jpg)

### Log Out Page - desktop

![Logout-desktop-lh](/static/images/testing-images/lighthouse/sign-out-desktop-lh.jpg)

### Register / Sign Up - mobile

![register-mobile-lh](/static/images/testing-images/lighthouse/sign-up-mobile-lh.jpg)

### Register / Sign Up - desktop

![register-desktop-lh](/static/images/testing-images/lighthouse/sign-up-desktop-lh.jpg)

### My Profile - mobile

![my-profile-mobile-lh](/static/images/testing-images/lighthouse/my-profile-mobile-lh.jpg)

### My Profile - desktop

![my-profile-desktop-lh](/static/images/testing-images/lighthouse/my-profile-desktop-lh.jpg)

### Add a Product - mobile

![add-product-mobile-lh](/static/images/testing-images/lighthouse/add-product-management-mobile-lh.jpg)

### Add a Product - desktop

![add-product-desktop-lh](/static/images/testing-images/lighthouse/add-product-management-desktop-lh.jpg)

### Edit a Product - mobile

![edit-product-mobile-lh](/static/images/testing-images/lighthouse/edit-product-mobile-lh.jpg)

### Edit a Product - desktop

![edit-product-desktop-lh](/static/images/testing-images/lighthouse/edit-product-desktop-lh.jpg)

</details>

[Back to Table of Contents](#table-of-contents)

<a id="wave"></a>
## Wave Report  



[Back to Table of Contents](#table-of-contents)

<a id="user-stories"></a>
## User Stories 

### Testing User Stories from the UX section of [the main README.md document](README.md)

Each screenshot displays a red square around each item that is needed to achieve the testing criteria.

### First Time Customer Goals

* As a first time customer to the website, I would like to search for products.
  * This is achieved by 


* As a first time customer to the website, I would like to see the number of products that are available.
  * This is achieved by

* As a first time customer to the website, I would like to view all products.
  * This is achieved by


* As a first time customer to the website, I would like to view individual product details.
  * This is achieved by


* As a first time customer to the website, I would like to sort the list of available products by price.
  * This is achieved by


* As a first time customer to the website, I would like to sort the list of available products by category.
  * This is achieved by


* As a first time customer to the website, I would like to read reviews about a product.
  * This is achieved by


* As a first time customer to the website, I would like to view holistic services.
  * This is achieved by


* As a first time customer to the website, I would like to increase and decrease the item quantity.
  * This is achieved by


* As a first time customer to the website, I would like to be able to purchase products through a secure checkout.
  * This is achieved by


* As a first time customer to the website, I would like to view items in my shopping bag.
  * This is achieved by


* As a first time customer to the website, I would like to adjust items in my shopping bag.
  * This is achieved by


* As a first time customer to the website, I would like to receive confirmation that the products have been purchased.
  * This is achieved by


* As a first time customer to the website, I would like to create an account.
  * This is achieved by

* As a first time customer to the website, I would like to receive confirmation that the account has been created
  * This is achieved by


### Returning Customer Goals

* As a returning customer to the website, I would like to have the ability to log in so my information is saved.
  * This is achieved by


* As a returning customer to the website, I would like to be able to log out of the site.
  * This is achieved by



* As a returning customer to the website, I would like to recover my password in case I forget it.
  * This is achieved by




* As a returning customer to the website, I would like to create, update and delete my own reviews.
  * This is achieved by



* As a returning customer to the website, I would like to read other reviews.
  * This is achieved by



### Site Owner Goals

* As a site owner of the website, I would like to be able to add products.
  * This is achieved by


* As a site owner of the website, I would like to be able to edit products.
  * This is achieved by


* As a site owner of the website, I would like to be able to delete products.
  * This is achieved by



<details open>
<summary><b>(click to expand or hide)</b></summary>

</details>

[Back to Table of Contents](#table-of-contents)

<a id="manual-testing"></a>
## Manual testing of all elements and functionality on every page 

<details open>
<summary><b>(click to expand or hide)</b></summary>

### Browsers tested:

* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Opera
* Safari

No errors were found on the above browsers

### Devices tested:

iPhone 12
* iPhone 11
* iPhone XR
* iPhone 7
* Samsung Tablet S6
* Samsung S20 Plus
* Samsung Galaxy S10
* Samsung A3
* Motorola G9 Plus

No errors were found when testing on the above devices.


| Page      | Section       | Action        | Expected Behaviour     | Result   |  
| --------- | ------------- | ------------- | ---------------------- | -------- |

</details> 

[Back to Table of Contents](#table-of-contents)

<a id="bugs-fixes"></a>
## Bugs/Fixes  

