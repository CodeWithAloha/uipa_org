# Emails

This document describes the email setup process for the UIPA.org project. At the end of this document, you will have a working email setup for the project (be able to send both FOI and general emails).

## Prerequisites

Before you start, you need to have the following:
- A working development environment for the project (Follow the [Getting Started](https://github.com/CodeWithAloha/uipa?tab=readme-ov-file#getting-started) guide to set this up)
- [The required email related environment variables](https://github.com/CodeWithAloha/uipa/blob/3bcbd67a8102b62840128017b4d62112b74e4d4c/uipa_org/settings/development.py#L25) (e.g., `ENABLE_EMAIL`, `SERVER_EMAIL`, `EMAIL_HOST`, ...etc.)
- - You can reach out to @tyliec or in the `#project-uipa` channel for shared values of these environment variables, or you can utilize another email server (using something like https://postmarkapp.com/) and set those values yourself.
- - Setting these values would look something like `export EMAIL_HOST='smtp.postmarkapp.com'` in your terminal.

# Context

There are two types of emails that the project sends:
- General emails: These are emails that are sent for administrative purposes (e.g., account creation, password reset, etc.)
- FOI emails: These are emails that are sent when a form is submitted to send a Freedom of Information (FOI) request to a public agency.

# Walkthrough

After you have the prerequisites set up, you can follow the steps below to verify that your email setup is working.
- **IMPORTANT**: Once you have your email server set up, it is highly possible that you might accidentially send an email to a real email address/public body. To avoid this, you should create a test public body and use that test public body's email address for testing purposes.

## General Emails

To test general emails, you can generate/trigger a data export. This will send a URL to download the data export to the email address of the user who triggered the export. You can trigger a data export by following these steps:
- Go to Profile > Settings
- Click on the "Request Data Export" button

## FOI Emails

- **IMPORTANT**: Once you have your email server set up, it is highly possible that you might accidentially send an email to a real email address/public body. To avoid this, you should create a test public body and use that test public body's email address for testing purposes.

To test FOI emails, you can submit a FOI request to a public body. You can do this by following these steps:
- Go to the public body's page
- Click the "Make a Request to this Public Body!" button
- Fill out the form and submit it
- A FOI email should be sent to the public body's email address (please ensure that the email address is correct and that the email is not sent to a real public body if you are just testing)