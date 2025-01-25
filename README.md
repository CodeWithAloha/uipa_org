# UIPA.org - Uniform Information Practices Act portal

> This branch is a departure from the main branch. It seeks to satisfy the goal
> of upgrading UIPA.org to currently supported versions of Python and Django
> without upgrading Froide to a newer upstream version.

This started as a Django project forked from the [Froide
Theme](https://github.com/okfde/froide-theme). This is a theme app that plugs
into [Froide](https://github.com/stefanw/froide) and is the recommended way of
creating a FOIA website by the Froide developers.

It will be easier to upgrade and maintain the UIPA project by combining the
Froide code into one Django project. This is due to the following problems:
- Upgrading UIPA to currently supported versions of Django and Python requires
lots of code changes to both UIPA and Froide.
- To satisfy the requirements to request information from Hawaii State and Local
government agencies (called public bodies in Froide), Froide was modified. This
required a fork but it has not been sync'd with the upstream since that point.
- The need to include Froide as an embeddable dependency due to the modified
fork.
- Maintaining a modified fork of an old Froide version (no version number
available) means maintaining two repos.

Going forward, the Froide code is no longer a dependency. It is included in the
source code of this project.

## Get started easily

For developers and others who wish to contribute to this project, see [Getting
Started](docs/getting-started.md).

## License

Froide and the Froide Theme are licensed under the MIT License.
