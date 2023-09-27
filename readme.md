# clucker - Qt application to reload plugins for [Redbot Discord](https://github.com/Cog-Creators/Red-DiscordBot)
**DISCLAIMER** - this application is work in progress, some things are done very poorly, some do not work at all.. but I think its already quite a good example.

![image](https://github.com/kkatsuro/clucker/assets/80922583/a530e650-2749-4f96-ad73-58ff5589633b)

I want to use this application as a help in development of plugins for RedBot. 
Previously, I've been using rsync to upload update code on a server, then running code reloading command by hand, 
or (later) using [command line tool](old-src/clucker). I also used tail -f over ssh on a logfile to see tracebacks.

This wasn't very convenient, so I wrote this application to connect all of that workflow.

Application is threaded and it can work for different servers and bots at once.
Reload cog button is using data from currently chosen cog, server and bot in gui, and it: 
1. uploads plugin from local directory to remote server
2. forwards local port to server, bots use RPC
3. connects to a websocket on a forwarded server to run reloading RPC command

Information about reloading plugin is visible in console, in bot's log tab. If there are any errors we will see them immediately.
