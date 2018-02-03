
# FIRST PowerUP! Strategy Game


This is a simple web-based game based on the FIRST Robotics Challenge
(https://www.firstinspires.org/)  Power Up! Game for 2018.

This game requires an HTTP server that can serve "CGI" files. This means that
when a client(browser) requests a "CGI" page, the HTTP server executes the CGI
script locally with any given arguments and then serves the "standard output"
(stdout) of the CGI script to the client. You can run any of the CGI files on
the command-line and you will see the HTML output for the start of the game.

This game consists of a single CGI file and a couple of images. The CGI file
produces a web page that displays the state of the game using the images. The
web page also displays user selections in HTML "form" format. When the user
submits their selections, they are passed as arguments to the CGI file, which
then produces an updated web page with a new game state.


### FILE DESCRIPTION

Here is a description of the files for this game. The game has been evolving
as I continue to develop it, so there are a couple of iterations:

- cube.png        : image of a single power cube
- field.png       : image of a PowerUp! field, taken from the game manual
- template.html   : the original html layout for the game	
- powerup_v1.cgi  : the first iteration/prototype of the game
- powerup_v2.cgi  : the second iteration/prototype of the game
- alliance.cgi    : the third iteration/prototype of the game


### WEB SERVERS

Apache (https://httpd.apache.org/) is the most common HTTP server for Linux,
but can be a little intimidating to setup and configure for first-time users.
I recommend and use thttpd (https://acme.com/software/thttpd/) for its ease-
of-use. Simply download and unpack the thttpd tar file, and build it:

	# tar zxf thttpd-2.27.tar.gz
	# cd thttpd-2.27
	# ./configure
	# make

Run 'make install' or copy the thttpd binary to a location. I launch it with
a simple script that I create:

  root@MrRobot:/usr/local/sbin/www# cat ../startweb
  #!/bin/bash

  /usr/local/sbin/thttpd -d /usr/local/sbin/www -c "**.cgi"
  root@MrRobot:/usr/local/sbin/www#

The two arguments are pretty intuitive. The `-d /usr/local/sbin/www` tells
thttpd to serve web pages located in the given directory, /usr/local/sbin/www/.
The `-c "**.cgi"` argument specifies a wildcard pattern for for CGI files,
in this case telling thttpd to treat all files that end in '.cgi' as CGI files.


### GAME NOTES

Changes and improvements are welcome! I'm too busy to spend as much time as I
would like on this, so please feel free to run with your own ideas on this.
There's plenty of room for improvement!

There are many ways to develop this game. If I was more fluent in Javascript,
I might have tried to do that so that the game just runs on a browser, without
the need for a server. However, one advantage to a server-based approach is
that this game could eventually be written such that two players can play each
other from their own screens in their own locations, and the server keeps the
game in sync. It's not there yet, but that's the current goal.

The first iteration, powerup_v1.cgi, was limited to cube placement, to focus
on this aspect of the game. After playing the first iteration a few times I
realized that each player could instantly react to the others selection. So the
second iteration, powerup_v2.cgi, tried to limit that by forcing each player to
move one robot at a time, and we would take turns on who would go first. I also
added support for invoking the the power-ups, and I switched from drop-down
menus to radio buttons to reduce the total number of clicks needed to play the
game.

The third iteration, 'alliance.cgi' attempts to move the game further towards
splitting the actions of the players, so that each player doesn't immediately
know what the other player is doing until after a round of selections are made.
The goal is to make this version game closer to the ultimate goal of splitting
the client into two separate instances so that they could be played from
independent locations.

Scoring is likely to be buggy in any iteration, but should be fair to both
sides. For example, the "end game" climbing score is currently only applied in
version 2. In 'alliance.cgi' I added a scoring table so that players could see
how they scored each round.

I'm still struggling with the amount of time each round takes. In version 1
and 3 the time is currently 10 seconds per round. In version 2 I experimented
with 12 seconds per round, but that introduced some challenges in computing
the 10-second power-up advantages, especially when they are "queued". In fact,
I punted on the queuing in both version 2 and 3 and just came up with a default
priority that I hope is fair. If one alliance "power up" activation is bumped
in favor of the other, the user just has to reactivate the bumped 'power up" in
the next round. I hope to clean this up and figure out a good timing strategy
in future versions of the game.

One thought I have for the timing is to configure a 5-second round, but assign
variable durations to each selection. For example, a user can choose to move a
cube from their pyramid to the exchange or switch and that would take 5
seconds. But if a user choose to get a cube from a portal and place it on their
switch it would take 15 seconds, so for the next two rounds after that action
was selected, that robot is unavailable for other tasks. This could make the
game a little more realistic. As part of implementing this, I may also want to
track and plot each robots location on the field as well, to reflect why some
selections will take longer than others.

Enjoy!

Chris Holmes
