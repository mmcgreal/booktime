from flask import Flask, render_template, request, session, redirect, url_for
from database import Database, format_schema
import user
import json
import urllib2

google_books_API = "https://www.googleapis.com/books/v1/volumes?q=%s&langRestrict=english&maxResults=40&orderBy=relevance&printType=books&showPreorders=true&key=AIzaSyCD5VLpef_d-PeOW7ISL3VsHQCdiuD_T1U" %(query)

def apiCall(n):
    request = urllib2.urlopen(n)
    result = request.read()
    return json.loads(result)

DATABASE = './database.db'
SCHEMA = [
    ('stories', [
        ('title', 'text'),
        ('author', 'int'),
        ('contents', 'text'),
        ('link', 'int'),
        ('istop','int'),
    ]),
    ('users', [
        ('username', 'text'),
        ('password', 'blob'),
    ]),
]

db = Database(DATABASE, SCHEMA)

def id_to_name(user):
    return db.get_user_by_id(user)

app = Flask(__name__)
app.jinja_env.filters['idtoname'] = id_to_name

@app.route('/')
@app.route("/home/")
def home():
    session["logged"] = 0
    return render_template("home.html")

@app.route("/login/", methods=['GET', 'POST'])
def login():
    session["logged"] = 0
    if request.method=="GET":
        return render_template("login.html")
    else:
        if request.form["sub"]=="Cancel":
            return render_template("login.html")
        user = db.check_user_password(request.form["username"], request.form["password"])
        if user > 0:
            session["user"] = user
            session["logged"]=1
            return redirect(url_for("userpage"))
        else:
            error = "You have entered an incorrect username or password.\n"
            return render_template("login.html", error=error)
        return render_template("login.html")

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        session["uname"] = request.form["user"]
        db.add_user(request.form["user"], request.form["pass"])
        return redirect(url_for("confirm"))

@app.route("/confirm/")
def confirm():
    return redirect(url_for("login"))

@app.route("/userpage/")
def userpage():
    if session["logged"]==0:
        return redirect(url_for("login"))
    else:
        return render_template("userpage.html",
        uname=db.get_user_by_id(session["user"]),
        posts=reversed(db.get_top_posts()),
        yourposts=db.get_top_posts_by_user(session["user"]))

@app.route("/newpost/", methods=['GET', 'POST'])
def newpost():
    if session["logged"]==0:
        return redirect(url_for("login"))
    elif request.method=="GET":
        username = db.get_user_by_id(session["user"])
        return render_template("newpost.html", uname=username)
    else:
        title = request.form["title"]
        body = request.form["body"]
        session["title"] = title
        session["body"] = body
        session["author"] = db.get_user_by_id(session["user"])
        return redirect(url_for("story", storyid=db.add_story(title, session["user"], body, 1)))

@app.route("/edit/", methods=["GET","POST"])
def edit():
    if session["logged"]==0:
        return redirect(url_for("login"))
    elif request.method=="GET":
        username = db.get_user_by_id(session["user"])
        return render_template("edit.html", uname=username)
    else:
        title = "<NO TITLE YET>"
        db.update_story_link(db.get_lowest_child(request.args.get('storyid')), db.add_story(title, session["user"], request.form["body"], 0))
        return redirect(url_for('story', storyid=request.args.get('storyid')))

@app.route("/story/")
def story():
    if session["logged"]==0:
        return redirect(url_for("login"))
    return render_template("story.html",
        title="POSTS", author="",
        posts=db.get_top_posts(),
        uname=db.get_user_by_id(session["user"]),
        storyid=request.args.get('storyid'),
        content=db.get_story_content(request.args.get('storyid')))

@app.route("/deletepost/")
def deletepost():
    if session["logged"]==0:
        return redirect(url_for("login"))
    db.remove_story(request.args.get('storyid'))
    return redirect(url_for("userpage"))

@app.route("/deleteline/")
def deleteline():
    if session["logged"]==0:
        return redirect(url_for("login"))
    return redirect(url_for("userpage"))

@app.route("/logout/")
def logout():
    session["username"]=""
    session["logged"]=0
    return redirect(url_for("home"))
    
@app.route("/results",methods=["GET","POST"])
def main():
    query = "Macbeth"
    if request.method == "POST":
        query = request.form["artist"] #rename
    for space in [' ']:
        query = query.replace(space, "%20")
    basic = google_books_API + query + """&results=1""" #double check this
    query = apiCall(basic)

    if query["response"]["books"]:
        query = query["response"]["books"][0]["name"] #check
    else:
	query = "Macbeth"
    artist = query
    
    for space in [' ']:
        query = query.replace(space, "%20")
    print query
    
    #url="""http://developer.echonest.com/api/v4/artist/images?api_key=V9SVA3AEDH6NCGYXY&name=""" + query + """&format=json&results=100"""
    #r = apiCall(url)["response"]["images"]

    #newQuery = apiCall("https://api.spotify.com/v1/search?q=" + query + "&type=artist")["artists"]["items"][0]["id"]
    #track = apiCall("https://api.spotify.com/v1/artists/" + newQuery + "/top-tracks?country=US")

    final = []
    counter = 0
    for image in r:
        ''' 
        multiprocessing might have to run in __name__ == "main", stackoverflow here:
        http://stackoverflow.com/questions/14920384/stop-code-after-time-period 
        multiprocessing code below, good for reference
        '''
        t1 = multiprocessing.Process( target=check_url, name = "check_url", args=(image["url"],))
        t1.start()
        #time.sleep(.2);
        t1.join(.2);
        valid_image = True
        print "\n" + image["url"] + "\n"
        if t1.is_alive():
            t1.terminate()
            t1.join()
            valid_image = False
            print "check_url taking too long, terminated"
    	if counter < 1 and valid_image:
            final.append(image["url"])
            counter = counter + 1
    
    if len(final) > 1:
        final = final[0:1]
    Tracks = []
    for T in track["tracks"]:
    	Tracks.append(T["name"])
    return render_template("Artist.html",images=final,artist=artist,Tracks = Tracks)

if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "BookTime"
    app.run('0.0.0.0',port=8000)
