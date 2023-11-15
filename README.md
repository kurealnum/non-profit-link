# NPL (Non Profit Link)

**Important:** Apparently I have been misspelling "organization" as "orginization". This is the most embarassing moment of my entire life. If you see a misspelled word, please change it.

Written in Python, Django, React (at some point)/JS, HTML, CSS, and SQLite3 (Postgres at some point)

**_Layout/Design:_** Look over [this](https://www.figma.com/file/pKaku2N7xVPbCGQb1p6LIJ/NPL?type=design&node-id=0-1&mode=design&t=mc7YWpRIbtvPRkHG-11) if you're trying to understand the project. However, everything will **_eventually be on .drawio files_**.

**_Database design:_** Keep in mind that this platform doesn't support SQLITE flavors, so production code will look a teensy bit different. Database currently meets: Third Normal Form (3NF); (This may be deprecated, I'll likely forget about it).

If you clone this project and create your own superuser, **_your email_** is your username on the Django Admin page.

# Contact information

- Discord: **kureal#0464**
- Email: **oscar.gaske.cs@gmail.com**

# FAQ

#### So... React?

Using React (and even JS) feels very overbearing and unnecessary for the current state of this project. That doesn't mean I won't use it in the future, but for now, I will be moving everything back to/writing everything in raw HTML/CSS, and I'll add in React when I _need_ it.

**Important:** the current files, components, etc. will all remain in this repository. I just won't be using them.

If you're looking to do something with React in this project, run `npm install`, and then `npm run dev` to build your project.

I've set up React so that you can use different files to control page renders, in other words, you can pick and choose which _compiled_ JS files you'd like to use.

Make sure to add your new TS/TSX files to `webpack.config.js`.

#### What am I going to do with this/what is it for?

I will do my best to explain this, but no promises that it'll make sense. My mom frequently volunteers for local organizations such as food pantries and homeless shelters. These organizations might seem like they're always in need of every single supply, but that's not quite correct. In my own experience, I have observed that they often have an excess of some items but a shortage of others. The simple solution to this is just to share, but if there's not a platform to share/advertise these supplies on, that creates a problem since there's no communication between them, thus hindering them from sharing resources.

To resolve this, I'd like to develop a web application with Django that will enable these organizations to list what they have and what they need. There are a few other things that I want to do with this that I'll make note of over time, but for now, that's the main goal.

#### What database will you/are you using?

SQLite. PostgreSQL (pronounced "post - gree - skew - l") in the future.
