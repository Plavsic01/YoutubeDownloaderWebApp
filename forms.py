from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class DownloadForm(Form):
    url = StringField(
        label="Url:",
        default="Enter URL:",
        validators=[DataRequired()]
    )

    submit = SubmitField("Download")
