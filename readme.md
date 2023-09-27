# qt app to reload python cogs

 there are configs for a
 * servers:
   * ssh key location
   * ssh credentials

 * bots:
   * related server
   * location of cog directory
   * rpc port number?

 * cogs in development:
   * location

 * application connects to a server
 * gets cog data from your pc
 * sends it trough ssh to a distant server
 * connects to bot trough rpc, reloads cog



 # diagram

 ssh connection:
 * console window? or use main for now?
 * sftp connection
 * for each bot:
   * rpc tunnel for commanding bot
   * bot logfile - tail command output
   * console window


# bot identification
* need to find rpc port (and if its enabled?)
* cog directory
* logfile

all can be done with finding systemctl units?
i could grep redbot in a systemctl units directory
then parse 'ExecStart' line and find out rpc port and directory in which its installed (or it is always the same?)

what if its on different user? -- user unit search path -- communicate ?

System Unit Search Path
    /etc/systemd/system.control/*
    /run/systemd/system.control/*
    /run/systemd/transient/*
    /run/systemd/generator.early/*
    /etc/systemd/system/*
    /etc/systemd/system.attached/*
    /run/systemd/system/*
    /run/systemd/system.attached/*
    /run/systemd/generator/*
    ...
    /usr/lib/systemd/system/*
    /run/systemd/generator.late/*

User Unit Search Path
    ˜/.config/systemd/user.control/*
    $XDG_RUNTIME_DIR/systemd/user.control/*
    $XDG_RUNTIME_DIR/systemd/transient/*
    $XDG_RUNTIME_DIR/systemd/generator.early/*
    ˜/.config/systemd/user/*
    $XDG_CONFIG_DIRS/systemd/user/*
    /etc/systemd/user/*
    $XDG_RUNTIME_DIR/systemd/user/*
    /run/systemd/user/*
    $XDG_RUNTIME_DIR/systemd/generator/*
    $XDG_DATA_HOME/systemd/user/*
    $XDG_DATA_DIRS/systemd/user/*
    ...
    /usr/lib/systemd/user/*
    $XDG_RUNTIME_DIR/systemd/generator.late/*
