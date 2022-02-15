from flask import Flask, redirect,render_template,request,send_file
from forms import DownloadForm
from yt_download import download
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route("/",methods=["GET","POST"])
def home():
    form = DownloadForm(request.form)
    if request.method == "POST" and form.validate():
        title,buffer = download(form.url.data)
        file_name = title + ".mp3"  
        return send_file(buffer,as_attachment=True,download_name=file_name,mimetype="audio/mpeg")
    return render_template("index.html",form=form)


@app.route("/how-to",methods=["GET"])
def how_to():
    return render_template("howto.html")


if __name__ == "__main__":
    app.run(debug=False)

