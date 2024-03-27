<div align="center">
  <img src="./docs/logos/uipa.org/vertical/UIPA-vertical-logo-transparent-background.png" alt="UIPA.org Logo" width="200" />
</div>

<div align="center">
	:envelope: :rainbow: :office:
</div>

<div align="center">
  <strong>A Freedom Of Information Portal for the State of Hawaii</strong>
</div>

> Note: This repository works in conjunction with the [CodeWithAloha/froide](https://github.com/CodeWithAloha/froide) repository. This repository is the "theme", while the froide repository is the "engine".

# Philosophy

Getting information from the government is our right under the Freedom of Information Act, however the process is more opaque than you might expect. The Uniform Information Practices Act 92F (UIPA) is Hawaii's adoption of the FOIA. This portal is a way to help individuals through the process of submitting a FOIA request, as well as open sourcing the requests and responses for others to view - all for free!

# News Articles

- https://www.civilbeat.org/2018/09/new-service-helps-public-access-public-records/
- https://www.civilbeat.org/2021/06/we-need-to-improve-government-transparency-in-hawaii/

# Getting Started

There are three main things that people have to stand up in order to start developing UIPA. These things are:

1. The Databases (Elasticsearch & PostgreSQL)
2. The Backend (Django server)
3. The Frontend (Vite)

At the end of setting up your development environment, you should have three terminal windows running each of these separately. Do not run these one after the other, as they all need to be running at the same time.

## The Databases

### Prerequisites

- [Docker](https://docs.docker.com/engine/install/) (for the databases)

### Instructions

The databases can be stood up together with one command using the provided [`docker-compose.yml`](https://github.com/CodeWithAloha/uipa/blob/08ce6d39bd9434f739117c801a7b8d442322455e/docker-compose.yml)

After running `docker-compose up` successfully, the output in your terminal should look something like:

![Image](https://github.com/CodeWithAloha/uipa/assets/15609358/d5cc6b6a-afbb-4b6b-bc98-35461d7523a5)

## The Backend

### Prerequisites

- [Python 3.10](https://github.com/okfde/fragdenstaat_de/blob/21faa6893a582a02f2a96f4ccce96fddab13bec6/requirements.txt#L2) (for the backend server)

> Note: You can use [pyenv](https://github.com/pyenv/pyenv) to manage your Python versions.

### Instructions

To run the Django server, you will need to run the following commands:

> Note: If you have already ran the following commands, you can skip them and just run a `python manage.py runserver` to start the server.

```
# Install the needed Python packages
pip install -r requirements.txt 

# To initialise the database
python manage.py migrate

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

To run the Vite server, you will need to run the following commands:

```
# Install the dependencies
yarn install

# Build the front-end
yarn build

# Run the front-end server (vite)
yarn run serve
```

After performing these steps, the application should be available at http://127.0.0.1:8000/ and look like:

![Image](https://github.com/CodeWithAloha/uipa/assets/15609358/f2e58505-418e-4747-83f9-96ecb02abd3f)

# Attribution

Many thanks to the [Open Knowledge Foundation Germany](https://www.okfn.de/) for their work on [Froide](https://github.com/okfde/froide). Their docs on the project are [available here](http://froide.readthedocs.org/en/latest/) including a [Getting Started Guide](http://froide.readthedocs.org/en/latest/gettingstarted/).

Thanks to the [Public First Law Center](https://www.publicfirstlaw.org/) for providing guidance and hosting for the UIPA.org project.