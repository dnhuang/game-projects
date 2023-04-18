# e7-substat-unit-matcher

Project started on 4/18/2023.

[Epic Seven (E7)](https://epic7.smilegatemegaport.com/) is a mobile gacha game that I've been playing on and off for a while, and as of 4/18/2023, it's been roughly *three years*.

I'm still relatively a new player (noob), and one of the things that I've struggled with is determining whether or not a piece of gear is worth upgrading.

To set up some context, gear in this game drops with random *substats*, and these substats are ultimately what you need to build up a character in the game. To upgrade these substats, currency is required, and sometimes acquiring this currency can be a pain. Thus, knowing beforehand whether or not to upgrade a piece of gear would ultimately save a player plenty of resources and time. Hence, the motivation behind this project.

I've decided to use [Epic7x](https://epic7x.com/), a database maintained by a third-party that contains all the characters released so far in the game as well as their *recommended* substats. From my frequent trips to the [E7 subreddit](https://www.reddit.com/r/EpicSeven/) and [Official E7 discord](https://discord.com/invite/8FeByWG), I am aware that this database may not be run by the most "knowledgeable" third party, and in fact some of the recommendations may be egregiously wrong. But I need to start somewhere, and I would argue being suboptimal with the "wrong" gear is better than not gearing the unit at all. The analogy I can think of is this: better to have a cheap *usable* tool than no tool at all.

For the start of this project, I just want to first figure out how to scrape the data first. But my vision for this project is to eventually turn this into a tool where I can select a *set of substats* and return a set of character(s) that can use these stats. The benefits are twofold; it would helper determine if a gear is worth upgrading AND catch those *odd* or *rare* substat combinations that are used by very nice characters. Maybe one day when I actually put in the effort to learn web development I can create an interactable UI, allowing me to just *click* on things. But until then, I will be working with a spread sheet and the trusty `ctrl` - `f`.

Encountered a very interesting bug while scraping data. My intuition is there's some weird anti-scraping mechanism in place for the site. Will probably put project on pause until then.
