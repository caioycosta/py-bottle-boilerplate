#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, static_file, template, url, get, post, request
from wtforms import Form, BooleanField, StringField, validators
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import markdown
import logging

Base = declarative_base()


class Artigo(Base):
    __tablename__ = 'artigos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    texto = Column(String)


class ArtigoForm(Form):
    titulo = StringField('titulo')
    texto = StringField('texto')


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


@route('/static/<filepath:path>', name='static')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/create', method=['GET', 'POST'])
def create():
    form = ArtigoForm(request.forms.decode())
    if request.method == 'POST':
        a = Artigo()
        form.populate_obj(a)
        with Session() as session:
            session.add(a)
            session.commit()
    return template('create', form=form)


@route('/')
def home():
    session = Session()
    # session.commit()
    # return markdown.markdown('*ola*') + sqlalchemy.__version__
    return template('create')


run(host='localhost', port=8080, debug=True)
