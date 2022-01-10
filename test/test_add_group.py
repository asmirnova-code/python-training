# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="my new group", header="some header", footer="some footer"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

