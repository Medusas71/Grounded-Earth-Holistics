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

<details open>
<summary><b>(click to expand or hide)</b></summary>
  

### User not logged in

| Page      | Section       | Action        | Expected Behaviour     | Result   |  
| --------- | ------------- | ------------- | ---------------------- | -------- |
| Home Page | Tab at top of page | On a desktop go to https://grounded-earth-holistics.herokuapp.com/ | The Home Page displays; there is a favicon displaying in the tab and the tab is named Grounded Earth Holistics | Pass |
|           | Navigation Bar (User is not logged in) | The name “Grounded Earth Holistics” displays on the left hand side and when clicked returns you to the Home Page | The Home Page displays | Pass |
|           |   | There is a search field where you can search the site. Type in “crystals” | All products that have Crystal in the name display | Pass |
|           |   | There is a Review link and when clicked you are taken to the Review Page | The Review Page displays | Pass |
|           |   | There is a My Account link and when clicked you have an option to either Register or Login | The 2 options display | Pass |
|           |   | Click Register | The Sign Up page displays | Pass | 
|           |   | Click Login | The Sign In page displays | Pass | 
|           |   | There is a shopping bag link and when clicked takes you to the shopping bag | The Shopping Bag page displays | Pass | 
|           |   | There are 8 navigation menu links | Home, Holistic Services, All Products, Crystals, Candles & Candle Holders, Bath Luxuries, Cacao & Gift Packs display | Pass | 
|           |   | Click the Home Page link | The Home Page displays | Pass | 
|           |   | Click the Holistic Services link | 2 options display being Tuning Therapy and Grounding | Pass | 
|           |   | Click the All Products link | 3 options display being By Price, By Category, All Products | Pass | 
|           |   | Click the Crystals link | 9 options display being Slabs, Carvings, Spheres, Towers, Clusters, Geodes, Roughs, Accessories, All Crystals | Pass | 
|           |   | Click the Candles & Candle Holders link | 2 options display being Candles, Candle Holders | Pass | 
|           |   | Click the Bath Luxuries link | 2 options display being Bath Salts, Body Scrubs | Pass | 
|           |   | Click the Cacao link | 1 option displays being Cacao | Pass | 
|           |   | Click the Gift Packs link | 1 option displays being Gift Packs | Pass | 
|           | Main | Confirm the Home Page text displays | The home page text displays with 2 images, wording, a Shop Now button and a Read More button | Pass | 
|           |   | Click the Shop Now button | The Products page displays | Pass | 
|           |   | Click the Read more link | The Biofield Tuning page displays | Pass | 
|           | Footer | Confirm there is an “About” link and click the link | The About Us page displays | Pass | 
|           |   | Confirm the “copyright” information and “developed by” information and a spiel about the site being made for educational purposes display | Copyright, Developed By and a spiel about the site being made for educational purposes display | Pass |
|           |   | Confirm there is a Facebook link, click the link | The Facebook page for Grounded Earth Holistics displays in a new tab | Pass | 
|           |   | Confirm there is an Instagram link, click the link | The Instagram page for Grounded Earth Holistics displays in a new tab | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
|           |   | Change the pixels to 992px | The hamburger menu displays | Pass | 
|           |   | Click the hamburger menu and check that the correct menu displays | Home, Holistic Services, All Products, Crystals, Candles & Candle Holders, Bath Luxuries, Cacao and Gift Packs display | Pass | 
|           |   | Click each menu item to confirm the appropriate drop-down menus display | The appropriate drop-down menu displays | Pass | 
| Holistic Services – Tuning Therapy | Main | On a desktop click the Tuning Therapy in the drop-down menu on the navigation bar | The Biofield Tuning page displays | Pass |
|           |   | Confirm the text displays and there are 2 images on the page | The text displays and there are 2 images displaying | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| Holistic Services – Grounding | Main | On a desktop click Grounding in the drop-down menu on the navigation bar | The Grounding page displays | Pass | 
|           |   | Confirm the text displays and 6 images display at the bottom of the page | The text displays and there are 6 images displaying at the bottom of the page | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| All Products – By Price | Main | Click the By Price in the drop-down menu on All Products on the navigation bar | All 39 products display | Pass | 
|           |   | Confirm that all products are displaying by price | All products are displaying by Price | Pass | 
|           |   | Confirm there is a drop-down menu where you can sort by various options | Drop-down menu displays where you can sort by Price (low to high), Price (high to low), Name (A-Z), Name (Z-A), Category (A-Z), Category (Z-A) | Pass | 
|           |   | Confirm there are no missing images | There are no missing images | Pass | 
|           |   | Confirm that each product has a name, price, a category and a review | Each product has a name, price, category and a review | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| All Products- By Category | Main | Click the By Category in the drop-down menu on All Products on the navigation bar | All 39 products display | Pass | 
|           | Confirm that all products are displaying by category order | All products are displaying by Category order | Pass | 
|           |   | Confirm there is a drop-down menu where you can sort by various options | Drop-down menu displays where you can sort by Price (low to high), Price (high to low), Name (A-Z), Name (Z-A), Category (A-Z), Category (Z-A) | Pass | 
|           |   | Confirm there are no missing images | There are no missing images | Pass | 
|           |   | Confirm that each product has a name, price, a category and a review | Each product has a name, price, category and a review | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| All Products – All Products | Main | Click the All Products in the drop-down menu on the All Products on the navigation bar | All 39 products display | Pass | 
|           |   | Confirm there is a drop-down menu where you can sort by various options | Drop-down menu displays where you can sort by Price (low to high), Price (high to low), Name (A-Z), Name (Z-A), Category (A-Z), Category (Z-A) | Pass | 
|           |   | Confirm there are no missing images | There are no missing images | Pass | 
|           |   | Confirm that each product has a name, price, a category and a review | Each product has a name, price, category and a review | Pass | 
|           |   | Click the Category link under the product image | You are taken to that particular category where the products display | Pass | 
|           |   | Click the Review link | The Review page displays | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| Crystals  | Main | Click Slabs from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Carvings from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Spheres from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Towers from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Clusters from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Geodes from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Roughs from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Accessories from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click All Crystals from the Crystals drop-down menu on the navigation bar | The products display | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| Candles & Candle Holders | Main | Click Candles from the Candles & Candle Holders drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Candle Holders from the Candles & Candle Holders drop-down menu on the navigation bar | The products display | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| Bath Luxuries | Main | Click Bath Salts from the Bath Luxuries drop-down menu on the navigation bar | The products display | Pass | 
|           |   | Click Body Scrubs from the Bath Luxuries drop-down menu on the navigation bar | The products display | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| Cacao     | Main | Click Cacao from the Cacao drop-down menu on the navigation bar | The products display | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| Gift Packs | Main | Click Gift Packs from the Gift Packs drop-down menu on the navigation bar | The products display | Pass | 
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The page displays correctly | Pass | 
| Review    | Main | Click Review from the header | The Welcome to the Review Page displays | Pass | 
|           |   | Search for a product and click Review under the product name | The Welcome to the Review Page displays | Pass | 
|           |   | Click New Post | You are prompted to Sign In | Pass | 
| My Account | Register | Click Register | The Sign Up page displays | Pass | 
|           |   | Sign Up for Account | An alert displays on the right hand side of the screen and a Verify your e-mail address displays | Pass | 
|           |   |   | You also receive an email to verify your account | Pass | 
|           |   | Click the link in the email | The confirm email address screen displays | Pass | 
|           |   | Click Confirm | A success alert displays on the right hand side of the screen and the Sign In page displays | Pass | 
|           | Login | Click Login | The Sign In page displays | Pass | 
|           |   | Sign In | A success alert displays on the right hand side of the screen | Pass | 
|           | Logout | Click Logout from the My Account drop-down menu | A Sign Out page displays | Pass | 
|           |   | Click Sign Out | A success alert displays on the right hand side of the screen | Pass | 
| Shopping Bag | Shopping Bag | Click the Shopping Bag icon from the header | The Shopping Bag displays advising your bag is empty | Pass | 
|           | Quantity of Item | Search for an item and confirm that you can use the plus and minus to either increase or decrease the quantity | The quantity either increases of decreases | Pass | 
|           | Add to Bag | Click Add to Bag | A success message displays with what the item is in your bag, how much more money you need to spend to get free delivery and a link to the Secure Checkout | Pass | 
|           | Confirming the item has been added to the bag | Click Secure Checkout | The Shopping Bag displays with the item/s displayed | Pass | 
|           | Quantity of Item | Confirm that you can increase and decrease the quantity and click Update | A success message displays stating that your purchase has been updated | Pass | 
|           |   | Click Remove | A success message displays stating that your purchase has been removed | Pass | 
| Secure Checkout | Checkout | Click Secure Checkout | The checkout page displays | Pass | 
|           |   | Click Complete Order | A prompt advises you to complete the fields | Pass | 
|           |   | Complete each field | All fields can be completed | Pass | 
|           | Payment | Enter only part of the testing card number of 42424242 | A prompt displays stating your card number is incomplete | Pass | 
|           |   | Enter the testing card number, month, year, CVC and ZIP and click Complete Order | A blue screen displays as the payment is processing and then a Thank You Page displays | Pass | 
| Thank You | Thank You | Confirm the order information | A success message displays in the top right hand corner of the screen, a confirmation email is sent to the customer, all of the order information is complete | Pass | 

### Logged in User

| Page      | Section       | Action        | Expected Behaviour     | Result   |  
| --------- | ------------- | ------------- | ---------------------- | -------- |
| Shopping Bag Details | Confirm email address is populated | Add a product & Go to the checkout | The email address is populated | Pass | 
|           | Save the delivery information to My Profile | Complete the checkout process and ensure that “Save this delivery information to my profile” is ticked | The checkout process is completed and the checkbox is ticked | Pass | 
| My Profile | My Profile | Click My Profile from the My Account drop-down menu | My Profile page displays | Pass | 
|           |   | Confirm the Default Delivery Information is populated | The Default Delivery Information is populated with my details | Pass | 
|           |   | Confirm the Order History displays | The Order History displays | Pass | 
|           |   | Click an Order Number | The Thank You page displays and an Alert displays in the top right hand corner of the screen | Pass | 
|           |   | Click Back to Profile button | The My Profile page displays | Pass | 
| Review    | Add a Review | Click Review from the header | The Review page displays | Pass | 
|           |   | Click New Post button | The Add a New Review page displays | Pass | 
|           |   | Click Cancel | The Welcome to the Review page displays | Pass | 
|           |   | Click New Post button again and add a title and some content and click Add Post button | The added post displays | Pass | 
|           | Edit a Review | Click Edit Post button | The Edit a Review page displays | Pass | 
|           |   | Click Cancel | You are taken back to your post | Pass | 
|           |   | Click Edit Post button, make a change to your post and click Update Post | The changes have taken effect | Pass | 
| Comments  | Add a Comment | Add a comment that is next to the review and click Reset | The comment is removed | Pass | 
|           |   | Add a comment and click Submit | The comment is added | Pass | 
| Review    | Delete a Review | On your review click Delete | A confirmation modal displays | Pass | 
|           |   | Click the Cancel button | You are taken back to your post | Pass | 
|           |   | Click Delete and click Delete on the confirmation modal | You are taken back to the Review Page, a success message displays on the top right hand corner of the screen and your review is deleted | Pass | 

### Site Owner

| Page      | Section       | Action        | Expected Behaviour     | Result   |  
| --------- | ------------- | ------------- | ---------------------- | -------- |
| Product Management | Add a Product | Once the site owner is logged in, go to My Account from the header and select Product Management | The Add a Product page displays | Pass | 
|           |   | Complete the form | The form is completed | Pass | 
|           |   | Click Add Product | The product is added to the appropriate category | Pass | 
|           | Edit a Product | Click Edit on the product details page | The Edit a Product page displays and an alert displays in the top right hand corner of the screen | Pass | 
|           |   | Make a change to the product and click Update Product | The change is displayed and a success message displays in the top right hand corner of the screen | Pass | 
|           | Delete a Product | Click Delete Product | The product is deleted | Pass | 

</details> 

[Back to Table of Contents](#table-of-contents)

<a id="bugs-fixes"></a>
## Bugs/Fixes  

