from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')
    
@app.route("/response")
def render_response():
    f100m = request.args['f100m']
    if  f100m < "47" :
        reply = "You're faster than Micheal Phelps"
    elif f100m > :
        reply = "You're slower than Giovanni Garcia"
    return render_template('response.html', response = reply)
def render_response():
    f200m = request.args['f200m']
    if f200 < "1:42.96":
        reply = "you're faster than Micheal Phelps"
    else:
        reply = "You're slower than Lorenzo Russell"
    return render_template('response.html', response = reply)

if __name__=="__main__":
    app.run(debug=False)
