# Reddit Remake

## Description

Welcome to [Reddit](http://www.reddit.com).  Reddit is a huge forum/social media platform which allows 
users to post whatever they would like and share it with the world.  There are 
millions of people online all the time looking and posting.  Reddit is also 
interesting in that it allows users to up-vote and down-vote basically 
everything on the site.  These votes turn into something called karma which 
people will do most anything for.  All of the posts belong to a subreddit 
which is simply a themed area containing posts.  You are going to create the 
model backend for this system.

## Learning Objectives
* Create Django project and app
* Understand and implement model relationships
* Create Admin pages
* Create helper methods on models using query sets

## Details

### Deliverables
* Django project with models and migrations
* Hard Mode Only: Extra python file detailing functions for sorting

### Requirements
* No pep8 errors
* Unit tests for all models and methods

## Normal Mode

You will need to create and test the following models. How much information 
you add is up to you but minimum requirements are listed. 

Subreddit:
* id
* Name
* Description
* creation date time
* method called `current_count` that returns how many posts
* method called `today_count` that returns posts in the last 24 hours
* method called `daily_average` that gets the average count of posts over the last 7 days

Post:
* id
* title
* description: needs to be longer than 255 characters
* url: which can be null and should use the built in urlfield type
* slug: This is a url friendly version of the title. [SlugField](https://docs.djangoproject.com/en/1.8/ref/models/fields/#slugfield)
* creation time
* modification time
* Relationship to subreddit
* Relationship to a User
* method called `is_recent` that returns True/False depending on if the post is in the last day
* method called `is_hot` that returns True/False if the post has gotten more than 3 comments in the past 3 hours

Comment:
* id
* comment text: needs to be longer than 255 characters
* relationship to User
* relationship to Post
* created time
* modified time


## Hard Mode
* Implement the voting system.  Both comments and posts can be voted up and down it is your choice how this is implemented in the system.  One note is that you probably want to store the up and down votes individually with timestamps

* Comments and Posts should have methods that allow for them to calculate the total value of up-votes - down-votes.

* Implement karma.  Reddit has 2 karma indicators link karma and comment karma.  For this project both karma are calculated as the sum of each item’s total (from previous objective).

* Implement the ManyToMany Relationship with Trophies

* Posts can be sorted in a few ways in reddit.  Implement the following as described.  You will need to do these in the django shell and add a python file with the code as part of your project.
     * New: Chronologically newest to oldest
     * Top: Highest rated for the last 24 hours
     * Hot: Ordered by amount of up-votes in the 3 hours
     * Controversial: Ordered by posts with a high number of both up and down votes

* The User object is part of the core auth library.  There are a few ways to extend its functionality.  Historically, the way it works is that you create a profile object with a OneToOne relationship to User.  Implement this object then create methods on it to retrieve:
* Link karma for the user
* Comment karma for the user
* Average up-votes
* Average down-votes
* Total counts for comments and links