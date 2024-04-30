# Emails

This document describes the steps to configure the UIPA.org project for sending email. After completing the steps, the UIPA.org website will be able to send both general and UIPA (Uniform Information Practices Act) emails.

> **IMPORTANT**: To avoid accidentially sending an email to a real email address and/or public agency, create a test public agency and its email address for testing purposes.

## Prerequisites

Before you start, you need:
- A working development environment for the project (Follow the [Getting Started](Getting-Started.md) guide to set this up)
- To set the environment variables for the email configuration before starting the Django web server. See [uipa_org/settings/development.py](https://github.com/CodeWithAloha/uipa/blob/3bcbd67a8102b62840128017b4d62112b74e4d4c/uipa_org/settings/development.py#L25) for what they are.
  - You can reach out to @tyliec on Slack in the `#project-uipa` channel for shared values of these environment variables, or you can use another email server (such as https://postmarkapp.com/) and set those values yourself.
  - Set these using something like `export EMAIL_HOST='smtp.postmarkapp.com'` in your terminal.

# Context

There are two types of emails that the project sends:
- **General emails** are sent for administrative purposes (e.g., account creation, password reset, etc.)
- **UIPA emails** are sent when a form is submitted to send a Uniform Information Practices Act (UIPA) request to a public agency.

# Test Sending Email

After you have the prerequisites set up, follow the steps below to verify that your email configuration is working.

## General Emails

Generate or trigger a data export. This will send a URL to download the data export to the email address of the user who triggered the export. Use these steps:
- Go to Profile > Settings
- Click on the "Request Data Export" button

## UIPA Emails

Submit a UIPA request to a public agency. Use these steps:
- Go to the public agency's page
- Click the "Make a Request to this Public Body!" button
- Fill out the form and submit it
- A UIPA email should be sent to the public agency's email address.

