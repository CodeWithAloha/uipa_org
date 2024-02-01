<h1 align="center">UIPA.org</h1>
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<div align="center">
	:envelope: :rainbow: :office:
</div>

<div align="center">
  <strong>A Freedom Of Information Portal for the State of Hawaii</strong>
</div>

> Note: This is a forked repo with a custom README. For the original document/repo, check out - https://github.com/okfde/froide

# Philosophy

Getting information from the government is our right under the Freedom of Information Act, however the process is more opaque than you might expect. The Uniform Information Practices Act 92F (UIPA) is Hawaii's adoption of the FOIA. This portal is a way to help individuals through the process of submitting a FOIA request, as well as open sourcing the requests and responses for others to view - all for free!

# News Articles

- https://www.civilbeat.org/2018/09/new-service-helps-public-access-public-records/
- https://www.civilbeat.org/2021/06/we-need-to-improve-government-transparency-in-hawaii/

# Development

There are three main things that people have to stand up in order to start developing UIPA. These things are:

1. The Databases (Elasticsearch & Postgres)
2. The Backend (Django development server)
3. The Frontend (vite)

At the end of setting up your development environment, you should have three terminal windows running each of these separately.

## The Databases

### Prerequisites

- [Docker](https://docs.docker.com/engine/install/) (for the databases)

### Instructions

The databases can be stood up together with one command using the provided [`docker-compose.yml`](https://github.com/CodeWithAloha/uipa/blob/08ce6d39bd9434f739117c801a7b8d442322455e/docker-compose.yml)

After running `docker-compose up` successfully, the output in your terminal should look something like:

![Image](https://github.com/CodeWithAloha/uipa/assets/15609358/d5cc6b6a-afbb-4b6b-bc98-35461d7523a5)

## The Backend

### Prerequisites

- [Python 3.8+](https://github.com/CodeWithAloha/uipa/blob/08ce6d39bd9434f739117c801a7b8d442322455e/setup.cfg#L35-L36) (for the backend server)

### Instructions

To run the Django development server, we need to run the following commands:

```
# Installing dev-dependencies
pip install -r requirements-test.txt 

# To initialise the database:
python manage.py migrate --skip-checks

# Create a superuser
python manage.py createsuperuser

# Create and populate search index
python manage.py search_index --create
python manage.py search_index --populate

# Run the Django development server
python manage.py runserver
```

After running these, you should see something like this in your terminal:

![Image](https://github.com/CodeWithAloha/uipa/assets/15609358/98b0c91e-c540-4309-95f9-313e1d4234ad)

## The Frontend

### Prerequisites

- [NodeJS & npm](https://nodejs.org/en/download) (for the frontend)
- [Yarn](https://classic.yarnpkg.com/en/docs/install)

### Instructions

```
# Install the dependencies
yarn install

# Run the front-end server (vite)
yarn dev
```

After performing these steps, the application should be available at http://127.0.0.1:8000/ and look like:

![Image](https://github.com/CodeWithAloha/uipa/assets/15609358/f2e58505-418e-4747-83f9-96ecb02abd3f)

# Attribution

Many thanks to the [Open Knowledge Foundation Germany](https://www.okfn.de/) for their work on [Froide](https://github.com/okfde/froide). Their docs on the project are [available here](http://froide.readthedocs.org/en/latest/) including a [Getting Started Guide](http://froide.readthedocs.org/en/latest/gettingstarted/).

Thanks to the [Public First Law Center](https://www.publicfirstlaw.org/) for providing guidance and hosting for the UIPA.org project.
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/avenmia"><img src="https://avatars.githubusercontent.com/u/17712276?v=4?s=100" width="100px;" alt="avenmia"/><br /><sub><b>avenmia</b></sub></a><br /><a href="https://github.com/CodeWithAloha/uipa/commits?author=avenmia" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!