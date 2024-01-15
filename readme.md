# clucker - Qt application to manage instances and reload plugins for [Redbot Discord](https://github.com/Cog-Creators/Red-DiscordBot)
**DISCLAIMER** - this application is work in progress.

I want to use this application as a help in development of plugins for RedBot. 
Previously, I've been using rsync to upload update code on a server, then running code reloading command by hand, 
or (later) using command line tool. I also used tail -f over ssh on a logfile to see tracebacks.

This wasn't very convenient, so I wrote this application to connect all of that workflow.

Application allows you to easily create new Python Virtual Environment for new version of Redbot Discord, create different instances and run them on your computer. During development, you can reload plugins from local directory and see if there were any errors in logs terminal tab.
