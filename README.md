# Flask Web App
Written in Python, Jinja2, HTML, CSS, and SQLite3

Layout/Design: Read this if you're trying to understand the project: https://docs.google.com/drawings/d/1nvq48tW1w0B1AnsZFVPUc0GktWn2xSzwuHfUjbxIF3M/edit?usp=sharing

Database design: Keep in mind that this platform doesn't support SQLITE flavors, so production code will look a teensy bit different. Database currently meets: Second Normal Form; 2NF (This may be deprecated, I'll likely forget about it). https://drawsql.app/teams/da-best-team-in-da-world/diagrams/main

# How can I help?
If you're interested in contributing, please do! I will take all the help I can get, but here's what I'm really confused on/really need right now:

-Frontend: (as in CSS, and styling). I'm completely lost on this stuff.

-Documentation: I probably make enough comments myself for readability, but the README feels really light. 

-Names/ideas: I need names for the project itself, and ideas for what I should do with this.

-Database design: I have a decent grasp on this, but getting keys/normalization right is tricky

# FAQ
#### What am I going to do with this?
I will do my best to explain this, but no promises that it'll make sense. My mom frequently volunteers for local organizations such as food pantries and homeless shelters. Despite the assumption that these organizations always require more supplies, however in my own experience, I have observed that they often have an excess of some items but a shortage of others. The simple solution to this is just to share, but if there's not a platform to share/advertise these supplies on, that creates a problem since there is no communication between them, thus hindering them from sharing resources. To resolve this, I'd like to develop a web application with Flask that will enable these establishments to list what they have and what they need. There are a few other things that I want to do with this that I'll make note of over time, but for now, that's the main goal.

#### What database will you/are you using?
SQLite, I'm lazy. I do of course have a database file, but I'm adding it to .gitignore. There might be multiple db files at somepoint.

#### Why are there so many "Lorem ipsums"?
I just want to simulate having to scroll down a page, just to make sure everything scrolls properly. The actual text here probably won't be longer than a paragraph.

#### What do you need help with?
See "[How can I help?](https://github.com/kurealnum/FlaskWebApp#how-can-i-help)"

# TODO LIST (I might forget to update this, just FYI)
#### Login page + Register page + SSID's (Session ID's)
-Reference most of this from CS50 DONE

-Finalize/fix DB files (for login/register at least) DONE 

-Logout button DONE

-Add flask flashes 

-Required password length, required type of email

-Use https://memegen.link for some apologies 

-Signup right now will just be for a user, but when I'm ready for "non-profit" users I'll add them too

#### Finish search function 
-Can take from CS50, but I'll have to tweak it a little bit 

-Try and use a faster algorithm mayhaps?

-Populate database with fake non-profits

-Database work; indexing, make sure it fits 3rd normal form

-This will of course require more HTML files, just a reminder to myself

# Constant TODO's
#### PRG (Post, request, get)
#### Keep working on the front end, meaning CSS, and information on pages
#### Find a nice place to host this when I'm done, or host it myself
#### Keep circling back on CSS, making little tweaks until I like it
 
