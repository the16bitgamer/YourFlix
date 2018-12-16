from flask import Flask, render_template
from os import walk
import socket, os

app = Flask(__name__)

@app.route('/')
def index():
    newText = getFolder('')
    newText.sort()
    root = "/"
    return render_template('listpage.html',root=root,toList=newText)

@app.route('/<name>')
def contentName(name):
    newText = getFolder(name)
    if name == "update_server":
        os.system("minidlnad -R")
        os.system("service minidlna restart")
        newText = getFolder('')
        newText.sort()
        root = "/"
        return render_template('listpage.html',root=root,toList=newText)
    root = "/"+name+"/"
    if not newText:
        newText = getFile(name)
        newText.sort()
        if not newText:
            newText = getFile('')
            newText.sort()
            loc = name
            return render_template('VideoPlayer.html',loc=loc,toList=newText,root="/",vid="Test")
        elif len(newText) == 1:
            return render_template('VideoPlayer.html',loc=name+"/"+newText[0],toList=newText,root="/",vid="/")
        else:
            return render_template('YourFlixShow.html',showName=name,seasonNum="",root=root,toList=["!",""],toEpisode=newText)
    else:
        newEpisodes = getFile(name+"/"+newText[0]+"/")
        newText.sort()
        return render_template('YourFlixShow.html',showName=name,seasonNum=newText[0],root=root,toList=newText,toEpisode=newEpisodes)
        

@app.route('/<name>/<season>')
def contentSeasons(name, season):
    newText = getFile(name)
    root = "/"+name+"/"
    if not newText:
        newText = getFile(name+"/"+season)
        if not newText:
            loc = name+"/"+season
            newText = getFile(name)
            return render_template('VideoPlayer.html',loc=loc,toList=newText,root="/"+name,vid=season)
        else:
            newText = getFolder(name)
            newEpisodes = getFile(name+"/"+season+"/")
            return render_template('YourFlixShow.html',showName=name,seasonNum=season,root=root,toList=newText,toEpisode=newEpisodes)
    else:
        return render_template('YourFlixShow.html',showName=name,seasonNum="",root=root,toList=["!",""],toEpisode=newText)

@app.route('/<name>/<season>/<episode>')
def contentEpisode(name, season, episode):
    loc = name+"/"+season+"/"+episode
    newText = getFile(name+"/"+season)
    return render_template('VideoPlayer.html',loc=loc,toList=newText,root="/"+name+"/"+season,vid=episode)

def getFolder(currLoc):
    for (dirpath, dirnames, filenames) in walk("/home/pi/Videos/"+currLoc):
        return(dirnames)
def getFile(currLoc):
        for (dirpath, dirnames, filenames) in walk("/home/pi/Videos/"+currLoc):
            return(filenames)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
