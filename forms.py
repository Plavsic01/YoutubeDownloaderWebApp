from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class DownloadForm(Form):
    url = StringField(
        label="Url:",
        default="",
        validators=[DataRequired(),],
        render_kw={"placeholder": "Enter URL:"}
    )

    submit = SubmitField("Download")
