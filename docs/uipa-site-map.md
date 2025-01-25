# UIPA.org Site Map

This is the site map of UIPA.org based on the source code in the Code With Aloha
repos.

See the [Source Code](#source_code) section for details.

| Item | Working Version | Production Version |
| ---  | ---:            | ---: |
| Django | 1.11 | 1.9 |
| Python | 3.8  | 2.7 |

*NOTE: Python 3.8 is no longer supported as of 10/07/2024.*

The data shown is entirely fictional and any similarity to real life is coincidental.

## Functionality not covered

- Tags (useful for searching for requests).
- Redaction (for hiding personal information or identity). See Hide my name on the web section in
the [New Users Sign Up](#new_users_sign_up) page.
- Requests that created as not public. See [Make a Request](#make_a_request) page.
- How requests are updated from email sent to UIPA.org.
- Periodic background processes.
- Administrative tasks performed by the Public First Law Center.

## Background

The UIPA.org website went live in Sep 2018.
  - https://www.civilbeat.org/2018/09/new-service-helps-public-access-public-records/

The website has not been upgraded to current versions of Python, Django, Linux operating system, and other dependencies.

This site map shows the parts of the website that users can interact with.

| Website | URL |
| ---     | --- |
| UIPA  | http://127.0.0.1:8000/ |
| Admin | http://127.0.0.1:8000/uipa-admin/ |

*NOTE: The above URLs are for a local development server. The production ones
use https://uipa.org/.*

## Logging in

When logging in on the Home page, use an email address and password.

<img src="images/uipa-website-log-in.png" alt="" width=500/>

If logging in on the Admin website, use a username and password.

<img src="images/uipa-admin-website-log-in.png" alt="" width=300/>


## Users

### Roles and Access control

These are the access permissions for the three user roles of UIPA.org.

| User Role     | Search Public Agencies | Search Requests | View a Request | Make a Request | Update a Request | Admin website |
| ---           | ---                    | ---             | ---            | ---            | ---              | ---           |
| anonymous     |  ✓                     |  ✓              |  ✓             |  ✕             |  ✕               |  ✕            |
| regular user  |  ✓                     |  ✓              |  ✓             |  ✓             |  ✓ (originator)  |  ✕            |
| administrator |  ✓                     |  ✓              |  ✓             |  ✓             |  ✕               |  ✓            |

### Users for testing in a development environment

It's useful to have two regular (non-administrative) users to test the access to
requests that they have made versus those that are not theirs.

These users are created when the seed data is loaded.

| Role         | Email Address  | Username  | Full Name        |
| ---          | ---            | ---       | ---              |
| Regular user | lani@uipa.org  | lani      | Lani Aloha       |
| Regular user | joe@uipa.org   | joe       | Joe Aloha        |
| Admin user   | admin@uipa.org | admin     | Adam Ministrator |

### OUT OF SCOPE

In the Admin website, users can be granted "staff" privileges to use part of or
all of the Admin website. This feature is not being investigated for this
document.

## The Site Map

### 1. Home Page

<img src="images/uipa-home-page.png" alt="" width=500/>

#### Navigation Bar

On all pages, you will see a navigation bar across the top. It has:

1. UIPA.org (Home page)
2. [Requests](#request_page)
3. [Public Agencies](#public_agencies)
4. [Make a Request](#make_a_request)
5. [Search box](#search_box_nav_bar)
6. ["Log In / Sign Up" link](#log_in_sign_up)
7. [User's fullname](#user_menu) which you click on to get the User Menu drop-down.

When not logged in, you see the *Log In / Sign Up* link on the right side of the navigation bar:

<img src="images/uipa-nav-bar-log-in.png" alt="" width=600/>

When logged in, you see the *User Menu* on the right side of the navigation bar:

<img src="images/uipa-nav-bar-user-menu.png" alt="" width=600/>


#### Search for Information

On the Home page, you will see on the left side of the page a search box with a button with the
label, "Search for Information".

<img src="images/uipa-search-for-information.png" alt="" width=400/>

See [Search For Information on the Home Page](#search_for_information) for details.

#### Footer

On all pages, you will see a footer across the bottom. It has:
1. [About](#about_page)
2. [FAQ](#faq_page)
3. [Terms of Use](#terms_of_use_page)
4. [Privacy Statement](#privacy_statement_page)

<img src="images/uipa-footer.png" alt="" width=400/>

See [10. Informational Pages](#informational_pages) for details.

<a id="request_page"></a>
### 2. Requests Page

After clicking on the *Requests* link in the navigation bar, you will see the Requests page.

You can access this page anonymously or as a logged in user.

Requests that have be made to public agencies are listed on this page.

<img src="images/uipa-requests-page-logged-in.png" alt="" width=500/>

You can list requests by juridiction or by status.

#### Individual Requests Page

##### Anonymous Users

If you don't have an account or you aren't logged in, you are an anonymous user.

You can look at any request but you can't change or add information in a request.

When the submission message is long, it is truncated. The truncated text has a link to click on to expand the message.

<img src="images/uipa-request-page-viewed-by-anonymous-truncated.png" alt="" width=500/>

After clicking on the link, you will see the full text of the message.

<img src="images/uipa-request-page-viewed-by-anonymous-expanded.png" alt="" width=500/>

##### Regular user that does not own a request

A regular user can look at any request but can change or add information to only their requests.

<img src="images/uipa-request-page-viewed-by-another-user.png" alt="" width=500/>

##### Regular user that owns a request

A regular user that made a request can take these actions:
- `Request`: View the request.
- `Got Mail?`: Add information that they received by post mail or by other means.
- `Send a message`: Send a follow-up message to the public agency that they made the request to.

Additionally, they can download their request in a zip file.

###### View request

To view a request, click on the "Request" button to the left side of the web page below the title of the request.

<img src="images/uipa-request-page-viewed-by-owner-request.png" alt="" width=500/>


###### Add information received by postal mail

To add information received by postal mail, click on the "Got Mail?" button to the left side of the web page below the title of the
request.

<img src="images/uipa-request-page-viewed-by-owner-postal.png" alt="" width=500/>

###### Send a message

To send a reply to the public agency, click on the "Send a message" button to the left side of the web page below the title of the
request.

<img src="images/uipa-request-page-viewed-by-owner-send-msg.png" alt="" width=500/>

###### Download the request information

On the ride side of the web page, if you click on the "Download request as ZIP file" button , the request is downloaded as a zip
file.

This is what's included in the zip file:

```shell
Archive:  /Users/russ/Downloads/1.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
      539  12-17-2024 13:26   2024-11-16_1_requester.txt
   113245  11-15-2024 14:48   2024-11-16_1-form1_records_request.pdf
---------                     -------
   113784                     2 files
```
The plain text form of the request in in the [*requester.txt*](resources/2024-11-16_1_requester.txt) file.

The PDF form of the request is in the [*form1_records_request.pdf*](resources/2024-11-16_1-form1_records_request.pdf) file.

##### Admin users

Admin users can look at any request but, like an anonymous user, can't change or add information in it.

They have administrative actions that they can perform on the request:
- Down the request as a zip file.
- View or change the request on the Admin website.
- Add tags (enter comma-separated list of tags and save them).
- Mark the request as checked.
- Mark the request as not an information request.
- Extend the deadline by months.

<img src="images/uipa-request-page-viewed-by-admin-user.png" alt="" width=500/>

<a id="public_agencies"></a>
### 3. Public Agencies Page

After clicking on the *Public Agencies* link in the navigation bar, you will see the Public Agencies
page.

The top half of the page:

<img src="images/uipa-entities-page-anonymous-top-half.png" alt="" width=500/>

The bottom half of the page:

<img src="images/uipa-entities-page-anonymous-bottom-half.png" alt="" width=500/>

You can also narrow down the list of public agencies by clicking on an item under the Juridiction
list on the right-side of the web page.

For example, the State juridiction:

<img src="images/uipa-entities-page-honolulu-juridiction-anonymous.png" alt="" width=400/>

Or the City and County of Honolulu juridiction:

<img src="images/uipa-entities-page-state-juridiction-anonymous.png" alt="" width=400/>

***NOTE:*** Topics are not used. These are tags that have been marked as a topic. The system
administrator of UIPA.org must do this on the Admin website.

<img src="images/uipa-admin-public-body-tag-as-topic.png" alt="" width=500/>

<a id="make_a_request"></a>
### 4. Make a Request Page

After clicking on the *Make a Request* link in the navigation bar, you will see the Make a Request
page.

<img src="images/uipa-make-request-start.png" alt="" width=500/>

To make a request, you will need to:
- Select a Public Agency.
    <br><img src="images/uipa-make-request-select-public-agency.png" alt="" width=500/>
- Select the type of information you would like to request.
    <br><img src="images/uipa-make-request-type-of-info-wanted.png" alt="" width=500/>
- If you select personal information, you will informed that the UIPA.org website is not appropriate
for requesting personal information.
    <br><img src="images/uipa-make-request-for-personal-info.png" alt="" width=500/>
- If you select general interest (public records), you will see a form to be filled out with your
request.
    <br><img src="images/uipa-make-request-for-public-info-01.png" alt="" width=500/>
    - If you want to request a waiver of the fees for fulfilling your request, you must explain why
    in the section below the line that says, "IF SEEKING PUBLIC INTEREST WAIVER, PROVIDE PUBLIC
    INTEREST STATEMEN BELOW THIS LINE".
    - You can make your request public or not.
        - *NOTE: Non-public requests are not covered by this document.*
    - Click on the "Submit Request" button when you are ready to submit your request.
    <br><img src="images/uipa-make-request-for-public-info-02.png" alt="" width=500/>
- After you click on the "Submit Request" button, you will see a notice telling you that your
request was sent.
    <br>The request is sent via email to the Public Agency that you selected.
    <br><img src="images/uipa-make-request-for-public-info-03.png" alt="" width=500/>



<a id="searches"></a>
### 5. Searching for Requests and Public Agencies

Searching is performed on requests or public agencies.

There are two places where searches can be performed:
- Search Box in the Navigation Bar
- Search For Information on the Home Page and the Search Results pages

<a id="search_box_nav_bar"></a>
#### Search Box in the Navigation Bar

In the navigation bar, you can enter one or more words to search for requests or public agencies.

Press the *Enter* key to start the search.

<img src="images/uipa-search-box-for-kaneohe.png" alt="" width=500/>

After the search is completed, you will see the Search Results page.

<img src="images/uipa-search-results-for-kaneohe.png" alt="" width=500/>

<a id="search_for_information"></a>
#### Search For Information on the Home Page and the Search Results pages

In the main content section on the Home page, there is "Search for Information" section.

You can enter one or more words to search for requests or public agencies.

For example, enter the word, "Kaneohe", in the search field.

<img src="images/uipa-search-for-kaneohe.png" alt="" width=400/>

After you click on the "Search for Information" button, you will see same Search
Results page you did when you used the "Search Box in the Navigation Bar.

On the Search Results page, you also see the Search For Information section. Use this for another
search; adding additional words or using different ones.

Also on the Home Page, below the search field, there are two links provided as examples of searching
for the words, *Budget* or *Criminal*.

If you click on the link to *Budget*, you will see the search results as if you entered that word in
the search field.

<img src="images/uipa-search-results-for-budget.png" alt="" width=500/>

<a id="log_in_sign_up"></a>
### 6. Log In / Sign Up Page

If you have created an account, you can log in. Otherwise, you can request an account.

This web page allows you to do either one of these tasks.

<img src="images/uipa-login-signup.png" alt="" width=650/>

#### Existing Users Log In

If you have an account, you enter your email address and password in the section on the left side of
the page.

After you click on the "Log In" button, you will be taken to the [Account](#account_page) page.

<a id="new_users_sign_up"></a>
#### New Users Sign Up

Enter your information in the section on the right side of the page.

<img src="images/uipa-sign-up.png" alt="" width=400/>

After you click on the "Sign Up" button, you will be sent an email and you should see this notice:

<img src="images/uipa-sign-up-submitted.png" alt="" width=600/>

When you read your email message and click on the link to confirm your account, you will see the
[Account Settings](#settings_page) page with the notice confirming your action.

<img src="images/uipa-sign-up-confirmed-via-email.png" alt="" width=600/>

To change your password, see the [Change your password](#change_pasword) section.

##### Error situations

- If you already have an account, when you try to sign up with the same email address, you will see
this notice.

<img src="images/uipa-sign-up-duplicate-email.png" alt="" width=400/>

- If you click on the confirmation link in your email message while you are
already signed in on the UIPA.org website with someone's account, you will see this notice.
  <br>To fix this error, logout and click on the confirmation link again.

<img src="images/uipa-sign-up-currently-logged-in.png" alt="" width=600/>


<a id="user_menu"></a>
### 7. User Menu Drop-down

On any web page, you can click on your name in the upper right corner to get the User menu drop-down
menu. From there you can select:
- My requests: Takes you to the [Account Page](#account_page).
- Settings: Takes you the [Account Settings Page](#settings_page).
- Logout

<img src="images/uipa-account-user-menu.png" alt="" width=600/>

#### Log out

When you click on the "Logout" item on the User Menu drop-down, you will be returned to the "Log In/Sign Up" page.

<img src="images/uipa-account-page-after-log-out.png" alt="" width=600/>

<a id="account_page"></a>
### 8. Account Page

The Account Page is presented when:
- You first sign in
- You click on the "My requests" drop-down menu item

There are two tabs on the Account page:

#### Your Requests

<img src="images/uipa-account-page-your-requests-have-some.png" alt="" width=650/>

#### Requests You Follow

<img src="images/uipa-account-page-requests-you-follow.png" alt="" width=650/>

<a id="settings_page"></a>
### 9. Account Settings Page

You can get to the Account Settings page by selecting Settings from User Menu drop-down or by
clicking on the "Your account settings" button on the Account page.

On the Account Settings page, you can change you email address or your password. You can also delete
your account. Your name and account privacy can only be changed by an admin user.

<img src="images/uipa-account-settings-page.png" alt="" width=500/>

<a id="change_email"></a>
#### Change email address

After you enter a new email address and click the "Save changes" button in the
"Your email address:" section, you will be sent a confirmation email message.

You will see notices confirming the change and asking you to click on the
confirmation link in the email message that you receive.

<img src="images/uipa-account-changed-email.png" alt="" width=500/>

After clicking on the confirmation link in your email message, you will see
the Account Settings Page with a notice saying that your email address has been
changed.


<img src="images/uipa-account-changed-email-confirm-link-success.png" alt="" width=500/>

<a id="change_pasword"></a>
#### Change your password

Click on the "Change your password" link to show the button to click to take this action.

<img src="images/uipa-account-change-password-link.png" alt="" width=500/>

Click on the "Change password" button to show the new password fields.

<img src="images/uipa-account-change-password-button.png" alt="" width=500/>

After entering a new password in the two fields, click the "Change password" button.

<img src="images/uipa-account-change-password-fields.png" alt="" width=500/>

When the password change is complete, you will see the ["Log in / Sign Up"](#log_in_sign_up) page.

#### Delete your account

To delete your account, click on the "Delete your account" link. You will see the "Password" and
"Confirmation Phrase" fields.

<img src="images/uipa-account-delete-request.png" alt="" width=500/>

Enter your password and the phrase, "Freedom of Information Act". Click the "Delete account" button.

When the account deletion is complete, you will see the "Log in / Sign Up" page with a message confirming your account's deletion.

<img src="images/uipa-account-deleted-notice.png" alt="" width=600/>

<a id="informational_pages"></a>
### 10. Informational Pages

When you are on one of these pages, under the main navigation bar at the top of the page, you will see links to:
- [About UIPA.org](#about_page)
- [Frequently Asked Questions](#faq_page)
- [Privacy Policy](#privacy_statement_page)
- [Terms of Service](#terms_of_use_page)

They are equivalent to the links in footer of the pages.

<a id="about_page"></a>
#### About Page (About UIPA.org)

<img src="images/uipa-info-link-about.png" alt="" width=400/>

<a id="faq_page"></a>
#### FAQ (Frequently Asked Questions)

*FIXME:* Production website had this updated on 01/02/2024.

<img src="images/uipa-info-link-faq.png" alt="" width=400/>

<a id="terms_of_use_page"></a>
#### Terms of Use Page (Terms of Service)

*FIXME:* Production website had this updated on 01/02/2024.

<img src="images/uipa-info-link-terms-of-service.png" alt="" width=400/>

<a id="privacy_statement_page"></a>
#### Privacy Statement Page (Privacy Policy)

*FIXME:* Production website had this updated on 01/02/2024.

<img src="images/uipa-info-link-privacy-policy.png" alt="" width=400/>

## Admin Website

Only users with administrator privileges can access the Admin Website.

If you are logged in as a regular user, you will see this page when you go to the Admin Website.

<img src="images/uipa-admin-not-authorized.png" alt="" width=300/>

The things that a person with administrative privileges can do in the Admin Website are what the
Django Admin app can do. They are covered by the [Admin
actions](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/actions/) documentation.

<a id="source_code"></a>
## Source code

This site map of UIPA.org is based on the source code in russtoku's fork of the Code With Aloha repos.

https://github.com/russtoku/uipa (Branch: update; Commit: 78ecec4)


```shell
$ git remote -v
origin	https://github.com/russtoku/uipa (fetch)
origin	https://github.com/russtoku/uipa (push)

$ git status
On branch update
Your branch is up to date with 'origin/update'.

$ git log --pretty=ref -n 40
78ecec4 (Add site map documentation, 2025-01-11)
a038397 (Add filename comment to account/settings template., 2025-01-11)
6c07431 (Remove another part of django-overextends, 2024-12-23)
f2a557d (Fix missing results in public body search, 2024-12-23)
262f88f (Don't propagate log messages for all loggers, 2024-12-23)
1fff231 (Remove django-overextends because included since Django 1.9, 2024-12-22)
b5889b1 (Set DOCKER_DEFAULT_PLATFORM environment variable for docker compose, 2024-12-21)
9af9326 (Ignore missing key error in foirequest/list.html for Requests, 2024-12-21)
1791b44 (Fix footer on Account Settings to FAQ instead of Help, 2024-12-19)
112cc6e (Python 3.8 requires digestmod argument for hmac.new(), 2024-12-19)
c38b431 (Add fixture for another regular user, 2024-12-17)
2eccec2 (Fix errors with publicbody/list.html and pagination.html, 2024-12-17)
e7a0830 (Clarify why Froide source is included, 2024-12-13)
6ac48e3 (Update README to reflect inclusion of Froide source, 2024-12-13)
8aa9ca7 (Add fixture for a regular user, 2024-11-15)
606b906 (Include froide source instead of being dependency, 2024-11-15)
91979ad (Add requirements-test.txt for testing with pytest; fix TEST_SELENIUM_DRIVER for Dev, 2024-11-14)
f6ec112 (Works with Python 3.8 and Django 1.11., 2024-10-14)
51adda8 (Set search service to use elasticsearch 2.x., 2024-10-08)
595a33f (Log all request URLs during dev, 2024-10-08)
7d12742 (Elasticsearch work. Still have search problems., 2024-10-07)
8940337 (Remove pysolr dependency., 2024-10-06)
f26ad21 (Remove solr as search engine choice. Hide elasticsearch container., 2024-10-06)
e4b2632 (Run 2to3 on all, 2024-10-05)
7e895d9 (Haystack connection for elasticsearch works with authN, 2024-10-05)
f5cf450 (Fix can't add public body and make request, 2024-10-03)
5a9a728 (Works with Python 3.7., 2024-10-03)
c0cd057 (Remove unused requirement for raven, 2024-10-02)
4b299bd (Update README.md for Python 3.5, 2024-08-08)
024b3f7 (Update to Python 3.5, 2024-08-08)
73cc661 (Updated raven client - this will be phased out at some point, so need to upgrade, 2018-10-11)
e530776 (Added ccs into the formated message, 2018-10-11)
11f1630 (Updated settings to send admins error messages from uipa/froide loggers, 2017-12-06)
d4cfc44 (Fixed settings.ADMINS not parsing to the appropriate emails, 2017-12-06)
5d864a9 (Added in submit if nothing was touched in the form, 2017-11-26)
cf5b979 (Added in function to catch submission of form and check for ALL CAPS, 2017-11-26)
82c9be7 (Added logic to redirect someone to a new request if cancel is selected, 2017-11-24)
16ade2a (Changed the ALL CAPS notice to the appropriate href, 2017-11-24)
bb90de6 (Upgraded psycopg2 to 2.7.1 because of https://github.com/psycopg/psycopg2/issues/594, 2017-11-23)
f542f5c (Added note to faq about ALL CAPS text. Added confirm button when leaving text area., 2017-11-23)
```

### Code With Aloha repos

- UIPA
    - https://github.com/CodeWithAloha/uipa.git (renamed from https://github.com/CodeforHawaii/uipa_org.git)
        - Branch: master
        - Commit: 73cc661 (Updated raven client)
        - Commit Date: 10/10/2018
        - By: ryankanno (Ryan Kanno)
    - Forked: https://github.com/russtoku/uipa 
        - Branch: update
        - Commit: e7a0830
        - Commit Date: 12/13/2024

- Froide
    - https://github.com/CodeWithAloha/froide.git (renamed from https://github.com/CodeforHawaii/froide.git)
        - Branch: master
        - Commit: 03c6a1f
        - Commit Date: 10/10/2018
        - By: ryankanno (Ryan Kanno)
    - Merged into https://github.com/russtoku/uipa (Branch: update; Commit: 606b906) on 11/15/2024.

