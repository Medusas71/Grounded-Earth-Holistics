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
  * This is achieved by having a search field on every page.

![1-search-for-products](/static/images/testing-images/user-stories/1-search-for-products.jpg)

* As a first time customer to the website, I would like to see the number of products that are available.
  * This is achieved by clicking any of the product pages and the number or products display.

![2-number-of-products](/static/images/testing-images/user-stories/2-number-of-products.jpg)

* As a first time customer to the website, I would like to view all products.
  * This is achieved by clicking the All Products link in the navigation bar and selecting All Products.

![3-view-all-products](/static/images/testing-images/user-stories/3-view-all-products.jpg)

* As a first time customer to the website, I would like to view individual product details.
  * This is achieved by clicking the image of the product and the product details display.

![4-view-product-details](/static/images/testing-images/user-stories/4-view-product-details.jpg)

* As a first time customer to the website, I would like to sort the list of available products by price.
  * This is achieved by clicking the All Products link in the navigation bar and selecting By Price. 
  * Once the products display, you can either sort by Price (low to high) or (high to low).

![5-view-by-price](/static/images/testing-images/user-stories/5-view-by-price-1.jpg)
![5-view-by-price](/static/images/testing-images/user-stories/5-view-by-price-2.jpg)

* As a first time customer to the website, I would like to sort the list of available products by category.
  * This is achieved by clicking the All Products link in the navigation bar and selecting By Category.
  * One the products display, you can either sort by Category (A-Z) or (Z-A).

![6-view-by-category](/static/images/testing-images/user-stories/6-view-by-category1.jpg)
![6-view-by-category](/static/images/testing-images/user-stories/6-view-by-category2.jpg)

* As a first time customer to the website, I would like to read reviews about a product.
  * This is achieved by clicking Review underneath each product which takes you to the Review page, 
  or clicking Review at the top of the Header.

![7-review](/static/images/testing-images/user-stories/7-review.jpg)
![7-review](/static/images/testing-images/user-stories/7-view-review.jpg)

* As a first time customer to the website, I would like to view holistic services.
  * This is achieved by clicking the Holistic Services link in the navigation bar and selecting either Tuning Therapy or Grounding.

![8-holistic-services](/static/images/testing-images/user-stories/8-holistic-services.jpg)

* As a first time customer to the website, I would like to increase and decrease the item quantity.
  * This is achieved by clicking the product and selecting the quantity.
  * This feature is also in the Shopping Bag in case a customer changes their mind about the quantity.

![8-quantity](/static/images/testing-images/user-stories/8-quantity.jpg)
![8-quantity](/static/images/testing-images/user-stories/8-quantity-bag.jpg)

* As a first time customer to the website, I would like to be able to purchase products through a secure checkout.
  * This is achieved by adding a product to your bag and clicking Go to Secure Checkout through the pop up screen 
  or by clicking the Shopping Bag icon and clicking Secure Checkout.
  * The user is taken to the Checkout page.

![9-secure-checkout](/static/images/testing-images/user-stories/9-secure-checkout.jpg)
![9-secure-checkout](/static/images/testing-images/user-stories/9-secure-checkout-bag.jpg)
![10-secure-checkout](/static/images/testing-images/user-stories/10-secure-checkout-complete.jpg)

* As a first time customer to the website, I would like to view items in my shopping bag.
  * This is achieved by clicking the Shopping Bag icon at the top of the Header.

![11-view-shopping-bag](/static/images/testing-images/user-stories/11-view-shopping-bag.jpg)

* As a first time customer to the website, I would like to adjust items in my shopping bag.
  * This is achieved by updating or removing the item in the Shopping Bag.

![12-adjust-shopping-bag](/static/images/testing-images/user-stories/12-adjust-shopping-bag.jpg)

* As a first time customer to the website, I would like to receive confirmation that the products have been purchased.
  * This is achieved by completing the steps through the Checkout and a Thank You page displays and a success 
  message displays in the top right hand corner of the screen.
  * The user also receives an email confirming their order.

![13-order-confirmation](/static/images/testing-images/user-stories/13-order-confirmation.jpg)
![13-order-confirmation](/static/images/testing-images/user-stories/13-order-confirmation-email.jpg)

* As a first time customer to the website, I would like to create an account.
  * This is achieved by clicking the My Account link in the header and selecting Register.

![14-register](/static/images/testing-images/user-stories/14-register.jpg)

* As a first time customer to the website, I would like to receive confirmation that the account has been created
  * This is achieved by completing the registration form so a verification message displays on the screen and on the right hand side 
  of the screen stating that a verification email has been sent.
  * The customer receives an email and clicks the link to confirm their details which takes them to the website where they can 
  confirm their email address.
  * Once confirmed the customer receives a Success notification on the right hand side of the header.

![15-confirm-account](/static/images/testing-images/user-stories/15-confirmation-account.jpg)
![15-confirm-account](/static/images/testing-images/user-stories/15-confirmation-account-email.jpg)
![15-confirm-account](/static/images/testing-images/user-stories/15-confirmation-account-email-confirm.jpg)
![15-confirm-account](/static/images/testing-images/user-stories/15-confirmation-account-success.jpg)

### Returning Customer Goals

* As a returning customer to the website, I would like to have the ability to log in so my information is saved.
  * This is achieved by clicking the My Account link in the Header and selecting Login.
  * Once the customer has logged in a Success message displays in the top right hand corner of the screen.

![16-login](/static/images/testing-images/user-stories/16-login.jpg)
![16-login](/static/images/testing-images/user-stories/16-login-success.jpg)

* As a returning customer to the website, I would like to be able to log out of the site.
  * This is achieved by clicking the My Account link in the Header and selecting Logout.
  * Once the customer has logged out a Success message displays in the top right hand corner of the screen.

![17-logout](/static/images/testing-images/user-stories/17-logout.jpg)
![17-logout](/static/images/testing-images/user-stories/17-logout-success.jpg)

* As a returning customer to the website, I would like to recover my password in case I forget it.
  * This is achieved by clicking Forgot Password on the Log In page.

![18-forgot-password](/static/images/testing-images/user-stories/18-forgot-password.jpg)

* As a returning customer to the website, I would like to create, update and delete my own reviews.
  * This is achieved by clicking the Review link in the Header and clicking New Post on the Review page.
  * Once the customer has added a review, they can simply click Edit Post to edit the Review.
  * Upon clicking Edit Post, the customer is taken to the Edit a Review page and an Alert confirmation 
  displays in the right hand side of the screen.
  * A customer can click Delete on their own post to delete their post. They cannot delete another users 
  post.
  * A deleting prompt displays confirming if the customer would like to delete their post.
  * A success message displays in the top right hand corner of the screen confirming the deletion.

![19-add-review](/static/images/testing-images/user-stories/19-add-review.jpg)
![19-add-review](/static/images/testing-images/user-stories/19-add-new-review.jpg)
![19-edit-review](/static/images/testing-images/user-stories/19-edit-review.jpg)
![19-edit-review](/static/images/testing-images/user-stories/19-edit-review-alert.jpg)
![19-delete-review](/static/images/testing-images/user-stories/19-delete-review.jpg)
![19-delete-review](/static/images/testing-images/user-stories/19-delete-review-confirmation.jpg)
![19-delete-review](/static/images/testing-images/user-stories/19-delete-review-success.jpg)

* As a returning customer to the website, I would like to read other peoples reviews.
  * This is achieved by clicking the Review link in the Header and the review displays.
  * The customer can then click the Name of the Review and read the full review.
  * It is also noted that only the author can edit this review.

![20-read-review](/static/images/testing-images/user-stories/20-read-review.jpg)
![20-read-review](/static/images/testing-images/user-stories/20-read-review-full.jpg)

### Site Owner Goals

* As a site owner of the website, I would like to be able to add products.
  * This is achieved by logging into the website and clicking the My Account menu and 
  selecting Product Management.
  * The site owner can then Add a Product to the database.
  * Upon completion of adding a product a Success message displays on the right hand corner of 
  the screen advising that the product has been added successfully.

![21-product-management](/static/images/testing-images/user-stories/21-product-management.jpg)
![21-product-management](/static/images/testing-images/user-stories/21-add-product.jpg)
![21-product-management](/static/images/testing-images/user-stories/21-add-product-success.jpg)

* As a site owner of the website, I would like to be able to edit products.
  * This is achieved by clicking Edit on the product description.
  * The Edit a Product screen displays where the site owner can edit the product and an alert 
  displays in the right hand side of the screen advising the site owner that they are editing a product.
  * Once the product has been updated a Success message displays on the right hand side of the screen advising 
  that the product has been successfully updated.

![22-edit-product](/static/images/testing-images/user-stories/22-edit-product.jpg)
![22-edit-product](/static/images/testing-images/user-stories/22-edit-product-alert.jpg)
![22-edit-product](/static/images/testing-images/user-stories/22-edit-product-success.jpg)

* As a site owner of the website, I would like to be able to delete products.
  * This is achieved by clicking Delete on the product description.

![23-delete-product](/static/images/testing-images/user-stories/23-delete-product.jpg)

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

