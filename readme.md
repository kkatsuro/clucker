# clucker - Qt application to manage instances and reload plugins for [Redbot Discord](https://github.com/Cog-Creators/Red-DiscordBot)
**DISCLAIMER** - this application is work in progress.

https://github.com/kkatsuro/clucker/assets/80922583/287d69db-3345-4333-a6f9-639f732d0e78

This application is a development tool for plugins for Discord bot - Red.
Previously, I've used rsync to upload code to a server, then, by hand, run reloading code, 
and later, used command line tool for it. All of that with using tail -f over ssh on a logfile to see any tracebacks.

This wasn't very convenient, so I wrote this application to connect all of that workflow.

Clucker runs Redbot locally on your computer and after you develop new plugin, you can simply update it on your production instance from Github repository. Application automates creation of new Python Virtual Environment with new version of Redbot Discord, allows to create different instances and run them. When developing plugins, you can reload them from local directory and see in logs terminal tab if there were any errors. 

### Future features and goals
* Terminal will be real, processes would color output and setup correct width.
* Simple API for implementing editor plugin for Clucker, you will be able to reload plugin from your editor and connect to the terminal - Clucker will remain instance manager, but it will be much better to use just 2 windows for development (editor + browser), rather than 3.
* Platform compability.
* Super simple and working installation of everything so you will be able to focus on programming and not get annoyed by having to fix software.


This is second design/version of Clucker, you can see the old one in the other branch.
