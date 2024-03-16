# _*_ coding: utf-8 _*_
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
class Search(FlaskForm):
    keyword = StringField(
        validators=[
            DataRequired("请输入搜索关键词！")
        ],
        description="搜索关键词",
        render_kw={
            "placeholder": "请输入搜索关键词！",
        }
    )
    submit = SubmitField(label="提交")
    