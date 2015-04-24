title: Chromoting 101
date: 2015-04-24
published: true

> Chrome Remote Desktop allows you to remotely access one computer from another
> over the Internet. For example, you can use the app to securely access your
> files or applications from another computer problem.
- [Chrome Help Center](https://support.google.com/chrome/answer/1649523?hl=en)

Computers can be made available on a short-term basis such as when you need
remote support, or on a more long-term basis for remote access to your
applications and files. All connections are fully secured. Chrome Remote Desktop
is cross-platform. (Windows, Mac and Linux).
You can access your Windows, Mac and Linux devices at any time from your 
Chrome browser. Chromebooks and Androids are included.

For emphasis CRD works in *2* basic ways.
 
 1. <h4>Remote Assistance</h4>
User-to-user screen sharing best utilized in remote
assistance tasks. It allows someone to access your computer, for those cases
where you're having issues with your pc and you think a friend might be in the
position to come to your aid. You first begin by sharing
your computer. This is done when you generate an access code that you pass on
to the other party. Once they have entered the code, your sharing session will
begin.
 2. <h4>Unattended access</h4>
To allow for longer periods of unattended access, there's this 2nd option where
you get to add your computers to Chrome Remote Desktop so you can 
access them from anywhere.
It's not really complicated to set up but can be a bit intimidating 
and not as straightforward, at least not on Linux devices(still in beta for a
couple of reasons).
For Windows and Mac users, this is fairly straightforward, so you can just skip
ahead to the next instructions whenever the current ones do not apply to you.

The following apply to all 3 platforms. Ignore that I'm focusing on Linux users
primarily. I'll say when it's time to branch off and go do your own thing :)

First, you should have the [Chrome Remote Desktop App from the webstore](https://chrome.google.com/webstore/detail/chrome-remote-desktop/gbchcmhmhahfdphkhkmpfmihenigjmpp?hl=en) 
enabled on each of your computers. 

Also if you'll be accessing your computers from an android
device, you'll need to install the [Chrome Remote Desktop Android App](https://play.google.com/store/apps/details?id=com.google.chromeremotedesktop)
, open the app and select any of your online computers to start chromoting. It's
that easy :) although you first need to make sure your computers are ready. The
next parts will ensure they are.

You must be running the official Google Chrome browser, not Chromium. 
The Debian package installs some `manifest.json` files in 
`/etc/opt/chrome/native-messaging-hosts/` but Chromium looks in 
`/etc/chromium/native-messaging-hosts/`. That said, you could probably try 
symlinking the appropriate files into place. For example:

    $ sudo ln -s /etc/opt/chrome /etc/chromium

Next do these in Chrome installed on Ubuntu or any other 
[Debian derivatives](http://distrowatch.com/search.php?basedon=Debian&status=Active).

At the time of writing this, there's no official rpm installable. But there's
an [open issue](http://code.google.com/p/chromium/issues/detail?id=343329) 
tracking this and it might be here sooner than you know... It'll be best if you
star it so you're among the first to know. 

Anyway, on to the next one.

### Chrome Remote Desktop App
You'll have to open the Chrome Remote Desktop app or "extension"

 1. Open a new tab.
 2. Open the Chrome Remote Desktop app from the Apps tab, [chrome://apps](chrome://apps)
or from your
[Chrome Launcher](https://support.google.com/chrome_webstore/answer/3060053?hl=en.)
 3. If the `Get Started` button appears in the "My Computers" box, click it to 
 display remote connection options.
 4. Click `Enable remote connections`.

### Chrome Remote Desktop Host Service
Next we'll install the Chrome Remote Host Service.

For Mac and Windows users, you'll need not do anything. The CRD host service will
offer to install when you click `Enable remote connections` from  the previous
step.

For Linux users(deb systems), you should also be offered the install but I've
found that it's probably better to install using [dpkg](http://en.wikipedia.org/wiki/Dpkg)
so I'll rather you download the host service
 
 - For 64bit systems: [http://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb](http://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb)
 - For 32bit systems: [http://dl.google.com/linux/direct/chrome-remote-desktop_current_i386.deb](http://dl.google.com/linux/direct/chrome-remote-desktop_current_i386.deb)

So let's install with `dpkg`

    $ sudo dpkg -i /path/to/chrome-remote*.deb

OK nice. You now have the Chrome Remote Host Service installed.


Do you have a preferred editor? Use it for the following instructions. I'll be 
using [Vim](http://en.wikipedia.org/wiki/Vim_(text(editor)), not that it makes 
any difference.

### Create a Virtual Session (For Linux users only)

Not everyone will need these steps. Things are not quite stable at the moment,
so if you find yourself facing issues trying to get CRD to work out of the box
I'll strongly recommend that you do not skip this section.

There are so many [window managers](http://xwinman.org) out there and everyone will try to sell
you on why you should try out theirs. I cannot cover all the various WMs in this
post.

For example I use [i3wm](http://i3wm.org/) and it's [great](https://github.com/jeffgodwyll/dotfiles/blob/master/.i3/config)
, [really](https://github.com/jeffgodwyll/dotfiles/blob/master/.i3status.conf) 
[great](https://github.com/jeffgodwyll/dotfiles/blob/master/i3-exit)... 
but I'm yet to be convinced I can be as productive with it on a 
touchscreen as I usually will since I 'chromote' from my nexus 7 quite often. 
So instead I prefer to install a lightweight desktop environment before
continuing. I'll be using [XFCE](http://www.xfce.org/).
    
    $ sudo apt-get install xfce4 xfce4-terminal

Edit your `.profile` file in your home directory and add 
`export CHROME_REMOTE_DESKTOP_DEFAULT_DESKTOP_SIZES=1024x768` to the end of 
the file. (Or better the resolution of your android device or the device you'll
be using so that things fit into screen. It's frustrating scrolling around) 

So if Vim is your editor, just open your `~/.profile` with it: 
    
    $ vim ~/.profile

And add the following to the end of that file and save

    export CHROME_REMOTE_DESKTOP_DEFAULT_DESKTOP_SIZES=1024x768

Create a file called `.chrome-remote-desktop-session` in your home directory. 
This should be a shell script that starts our preferred desktop environment, 
XFCE.

For example:

    $ vim ~/.chrome-remote-desktop-session

Edit the file to contain this line at the beginning
    
    exec /usr/sbin/lightdm-session "startxfce4"

Remember to save your changes.

### Start the Host Service
Again for the other platforms, the service should already be running in the
background.

For windows this info might be helpful:

> Upon being installed, the package adds a service which is designed to run 
> continuously in the background. Manually stopping the service has been seen to 
> cause the program to stop functioning properly. It adds a background controller 
> service that is set to automatically run. Delaying the start of this service is
> possible through the service manager. The software is designed to connect to 
> the Internet and adds a Windows Firewall exception in order to do so without 
> being interfered with. The primary executable is named `remoting_host.exe`.
- [Should I Remove It](http://www.shouldiremoveit.com/Chrome-Remote-Desktop-Host-13249-program.aspx)


For Linux folks let's now stop and start the session with the following still
in the terminal:

    $ sudo /etc/init.d/chrome-remote-desktop stop
    $ sudo /etc/init.d/chrome-remote-desktop start

### Enable Remote Connections

Open the Chrome Remote Desktop web app.
  
  1. Click `Enable remote connections`
  2. Enter a PIN and re-type the PIN. Then click OK.
  3. Dismiss the confirmation dialog.

Now, we've set up our machines to be accessed from literally anywhere. All 
we'll do from there is fire up the Android app or Chrome app from the 
device we'll be using, connect to our box we've just set up, key in the PIN 
and voilà. You can start using your remote machine :)
