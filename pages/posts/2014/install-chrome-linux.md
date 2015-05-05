title: Installing Chrome on Ubuntu!
date: 2014-12-31
published: true
tags: [chrome, linux]

On the [Google Chrome Help Forum](https://productforums.google.com/forum/#!categories/chrome/linux)
, I usually run into Ubuntu users who sometimes have issues installing 
or reinstalling Google Chrome. This post is to help fill that void.

## Some Prerequisites

    $ sudo apt-get purge google-chrome-stable

and then

    $ sudo apt-get autoremove


Now we'll first install some necessary libraries for Chrome.

    $ sudo apt-get install libxss1 libappindicator1 libindicator7


## Let's download Chrome
** For 64 bit system: **

  Stable:

    $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

  Beta:

    $ wget https://dl.google.com/linux/direct/google-chrome-beta_current_amd64.deb

  Dev/Unstable:

    $ wget https://dl.google.com/linux/direct/google-chrome-unstable_current_amd64.deb


** For 32-bit system: **
 
  Stable:
    
    $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb
 
  Beta:
    
    $ wget https://dl.google.com/linux/direct/google-chrome-beta_current_i386.deb

  Dev/Unstable:
    
    $ wget https://dl.google.com/linux/direct/google-chrome-unstable_current_i386.deb


## Install and Run Chrome:

    $ sudo dpkg -i google-chrome*.deb

Installing it this way ensures that a PPA is added to your system so that 
Google Chrome receives the latest updates whenever you check for system updates.


Now run Chrome with
    
    $ google-chrome-stable 

or 

    $ google-chrome-beta 

or 
    
    $ google-chrome-unstable
    
depending on what you installed.

Happy Browsing!!!
