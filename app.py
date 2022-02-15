from crypt import methods
from flask import Flask, redirect,render_template,request, url_for,flash
from forms import DownloadForm
from yt_download import download
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route("/",methods=["GET","POST"])
def home():
    title = None
    form = DownloadForm(request.form)
    if request.method == "POST" and form.validate():
        title = download(form.url.data)
        flash(f"{title} Has Been Downloaded Successfully!")  
    return render_template("index.html",form=form,title=title)


@app.route("/how-to",methods=["GET"])
def how_to():
    return render_template("howto.html")


if __name__ == "__main__":
    app.run(debug=True)

