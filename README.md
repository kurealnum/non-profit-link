# NPL (Non Profit Link)

## Check out the site

_**The site is live! Woo hoo! Check it out [here](https://nonprofitlink.org).**_

If you'd like to make a feature request, please do so! I'd be happy to look into it. 

## Info

Written in Python, HTML, and CSS

Uses Django, DRF (Django Rest Framework), HTMX, and Postgres.

Join the [discord!](https://discord.gg/smTmsCt69W)

**_Layout/Design:_** Look over [this](https://www.figma.com/file/pKaku2N7xVPbCGQb1p6LIJ/NPL?type=design&node-id=0-1&mode=design&t=mc7YWpRIbtvPRkHG-11) if you're trying to understand the frontend of the project. If you're contributing to the frontend, please _do not worry about making everything exactly like the Figma file_.

**_Some extra diagrams (generally unused):_** [Eraser.io](https://app.eraser.io/invite/CMPmi4yayzi3WI2kI1DS)

<a href="https://www.digitalocean.com/?refcode=ed12512a8ea7&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg" alt="DigitalOcean Referral Badge" /></a>
This is a referall link. I pay to host Non Profit Link, and signing up with this referall link can help alleviate some of the costs. 

# Contact information

- Discord: **kureal#0464**
- Email: **oscar.gaske.cs@gmail.com**

# FAQ

## So... React?

React has (as of 11/30/23) been completely removed from this project. I would've liked to have kept it around, but it was really only causing _major_ cramps in my workflow. Other than being "scalable", it served no purpose.

## What is DRF (Django Rest Framework) used for?

Used for the Items API (see apps/items/)!

## (Mission Statement) What am I going to do with this/what is it for?

My mom frequently volunteers for local organizations such as food pantries and homeless shelters. These organizations might seem like they're always in need of every single supply, but that's not exactly right. In my own experience, these organizations often have an excess of some items but a shortage of others. The simple solution to this is just to share, but if there's not a platform to share/advertise these supplies on, then there's no way to know who needs what. The little sharing that is done is normally done through connections that leadership makes. I don't speak for every non-profit in existence, but this seems to be a pretty big problem.

To resolve this, I'd like to develop a web application with the tools listed that will enable these organizations to list what they have and what they need.

## What database will you/are you using?

PostgreSQL (pronounced "post - gree - skew - l")

## Why aren't you using a JS framework for your frontend?

See [this](#so-react). Django doesn't play well with frontend JS frameworks. The only framework that works _really_ well is HTMX, or something on the same level of minimalistic as HTMX.

## How are you hosting this?
Nginx and Gunicorn through a VPS. 

## Folders

- **apps**: All apps, future and present
- **diagrams**: Draw.io files. Just a database diagram at the moment
- **static**: Static files
- **project**: Project folder for Django
- **tests**: Unit tests for Django
- **templates**: Templates for Django
