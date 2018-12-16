# YourFlix
YourFlix is (hopefully) a easy to use and to install Media Server/Web Application so you can stream movies and TV shows from your own media collection/HDD

If you want to build your own YourFlix Server I will have a link to the Image File used for my own Pi which needs some configurations to work with your setup, if you want to build it from scratch I will walk you through how I built mine, and tutorials I used and the source code for the Server, however I never inteded on making this replicatable so be warned if you want to do this from scratch it might not be that replicatbale.

What you'll need:
  0) Wifi router/modem/Anything with internet and a ethernet cable
  I) Raspberry Pi (any with an ethernet I'd recomend a Pi 3)
  II) MicroSD Card +8GB
  III) UL Listed Power Supply 5V DC / 2.5A
  IV) External HDD (recomend +2TB however any will work)
  V) Enclosure for the Pi
  VI) A display for the Pi (with cables)


***BUILDING YOUR PI***

Step 1) Installing Raspbain

YourFlix runs off of Raspbain I have not tested it with anything else so you can use any version on linux but I cannot say weither it will work or not.

1a) If you want to start from scratch download Raspbain Here: https://www.raspberrypi.org/downloads/raspbian/

1b) If you want to just have YourFlix without codeing anything download it here: https://archive.org/details/YourFlixV3
  
Now that Raspbain is downloaded follow this tutorial from Raspberrypi.org so you can install and get your pi ready

2) https://www.raspberrypi.org/documentation/installation/installing-images/

Step 2) Physically Connecting your Pi

	I can now assume that your Raspberry Pi's SD card is ready to go. Plug it into your Pi, put your Pi into it's case connect it to your internet via ETHERNET (wifi wont work), plug in your HDD, Plug in the Display and plug in the power.
 
Congratulations you have a computer with Rasbain on it.

***GETTING THE FILES, FOLDERS, and HDD READY READY***

So now it is time to get YourFlix working. Right now we need to set up 2 things.

I) We need to make the IP Address of YourFlix to be static
II) We need to Mount the HDD to the videos folder

Let start with making the IP Address Static
Step 1) Setting up Static IP

	1) We need to get you IP Addess
		0) Connect You Pi to the internet via the ethernet NOT WIFI (max connections is 3 or 4) 
		a) Open the Teminal
		b) Type in the Terminal
			ifconfig
		c) Write Down the IP Address
			It should look like 192.168.0.5

	2) Now we net to configure your IP address so it doesn't change
		a) On the top bar look for and Up aro and a down arow flashing
			5 icons fom the left next to the speaker
		b) LEFT Click it then Right click "Wireless and Wired Network Settings"
		c) next to Interface press the button and select eth0
		d) Set the IP Address to the first 3 number in the one you wrote down
			i.e. 192.168.0.
		e) Now for the last number type in any number which is easy to remember but is less than 250 like 155
			you IP address should no look like 192.168.0.155
		f) Press Apply
		g) Now reboot your PI

Now that our Pi isn't going to change it's IP Address we now need to set up the HDD.

Step 2) Configuring the Pi's HDD
	
	1) On this GitRepository there is a zip called 'EXAMPLE HDD.rar' extract it into the HDD you are going to use for your movies
		
		It should now look like
			HDD:\ 	-> DIR
				-> css
	
	Do not change it! DIR is for the images and css is so you can change the way the site looks on the fly
	
	2) Now if you want to add Movies just put the movie (in a web compatible format like .mp4) into a folder on the HDD and if you want the graphics to work name a png image the same as the folder name. Lets use Star Wars as an example!
      
	Star Wars need to be put into a folder called "Star Wars IV"
		Note: The video can be called anything it's the folder name that is important
        
	We will create an image for it (320x180 is recomended) called "Star Wars IV.png"
      	Now our HDD should now look like
		HDD:\ 	-> DIR
				-> Star Wars IV.png
			-> css
			-> Star Wars IV
				-> Star Wars episode IV A New Hope.mp4
                  
      If you want to do a TV Show it is pretty much the same process however if you have many episodes it will look like
      HDD:\ 	-> DIR
                    -> Star Wars IV.png
                    -> Star Wars Rebels.png
                -> css
                -> Star Wars IV
                  -> Star Wars episode IV A New Hope.mp4
                -> Star Wars Rebels
                  -> Season 01
                    -> E01.mp4
                    -> E02.mp4
                    -> ...
                    -> E'n'.mp4

Step 3) Mouting the HDD to the Videos Folder
	
	I) Open Terminal
	II) type in Terminal
	sudo lsblk -o UUID,NAME
	III) write down the UUID fo your Drive
		it should look like 74D2B2F0D2B2B5A8
	IV) type in Terminal
		sudo nano /etc/fstab
	IV.5) There is example code here if you need help
	V) Look fo UUID and replace it with the new one
		Only 1 Drive can be mounted on a file at one time
	VI) If you want to add any additional dives type in
		UUID=**YOU UUID** /home/pi/Videos **THE DRIVES FILE FORMATE** defaults,auto,nofail,umask=000,user0,users,Susers,rw,0,0
	VII)press CTRL and X to quit
		press Y then ENTER to save
	VIII) type reboot in the terminal

Congratulations YourFlix is ready to run. If you installed the YourFlix Variant of Raspbain you can type in the Pi's IP Address and it will work! However if you want to use the Database functionality remember to refress the server.

Step 4) Building the Media Server database (MiniDlna)

	I) Via Terminal
		a) Open a Terminal
		b) type in the terminal
			sudo service minidlna restart

	II) Via Web Browser
		a) Type in your Pi's IP Address on any web Browser
		b) Once the page has loaded scroll to the bottom
		c) look for BLACK TEXT that says
			Update Server
		d) Click Update Server

***BUILDING YOURFLIX FROM SCRATCH***
This is for those who want yourflix but already have raspbain or want to make it themselves

So you've mounted your HDD and you've set a static IP. Lets get under the metaphorical hood and get working on this Pi.

To Build YourFlix you need 3 programs to install

1) Apache2 Web Server (For file hosting and as a default gateway in)
2) Flask Python Server (for all your Python Server needs, although I think Apache2 has python never figgured it out)
3) MiniDLNA (for all your Media Server Needs)

If you just want a Media Server do step 3, if you want just a website with movies just steps 1 & 2.

Step 1) Apache2 Web Server

	1) Follow This Tutorial from raspberrypi.org
    		https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md
  	2) You need to GIVE PERMISSION Apache2 so it can access the folder you used for the mounted HDD
    		note: I do not remember how but it can be Googled
  	3) create a Sybiotic Lync from the folder you mounted the HDD into the /var/www/html/ folder so you can access the files via the web browser
  
Step 2) Flask

The purpose of Flask is to construct the website since HTML/Javascript cannot do it on it's own

	1) Follow this tutorial on Flask and how it works
    		https://projects.raspberrypi.org/en/projects/python-web-server-with-flask
  	
	2) If you want to keep your code you can however my Flask code is attached in this git in the 'webapp' folder
  	
	3) Place the webapp folder where you setup the flask server
  	
	4) Add code to auto start Flask (cannot remember how I did this)
  
Step 3) MiniDLNA

    1) Follow this tutorial for MINIDLNA
      https://www.raspberrypi.org/forums/viewtopic.php?t=16352
    2) Attach the folder you mounted the HDD to so MiniDLNA can read it
    
Congrats you now have YourFlix

Minor conviences I place in is
1) A update server button on the YourFlix Home Page so I didn't have to manually go in and update the MINIDNLA every time I added a new video
2) I made the apache2 default webpage redirect you to the FLASK port so I didn't have to
3) Install a DNS Server so I didn't have to remember my IP, however I never got this to work

Have fun with YourFlix!
