# Twitch IRC Server mock
This program mimics the behaviour of the IRC server from Twitch.

You can use it to stress test your Twitch bot by combining this code with ncat (the one from Nmap project).


## Requirements
To execute this in your system you only need:

* Python3.6 or newer
* [Ncat](https://nmap.org/ncat/)

These are usually available in the repos of your favourite Linux distro.


## Usage
Inside a terminal execute:

```
# ncat -l 0.0.0.0 6667 -e '/bin/bash -c /path/to/twitch_test.py' --keep-open
```

You can customize the command above with your desired port and use an specific listen address to bind to instead of using all available addresses in your system.

By default you will receive a message every 1ms. If you want to customize you can specify the number of miliseconds when sending the password. See below examples of valid passwords:

```
# This will set the interval between messages to 500ms
PASS foo500
# This will set the interval between messages to 1000ms
PASS 1000
```

