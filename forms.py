from flask.ext.wtf import Form
from wtforms import StringField, SubmitField


class ProblemForm(Form):
    link = StringField('问题链接')
    submit = SubmitField('提交')