#!/usr/bin/env python
'''
Describe the gitlab runner images built by the ETech Flex SRE team.
'''
import os

from datetime import date
from flask import Flask, render_template
from flask_frozen import Freezer

import bios


app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
freezer = Freezer(app)


@app.cli.command()
def freeze():
    '''Freeze the app.'''
    freezer.freeze()


@app.cli.command()
def serve():
    '''Serve the app.'''
    freezer.run()


@app.route('/')
def root():
    '''Generate the HTML'''
    tags = bios.read('./data/tags.json')
    return render_template('index.j2',
        tags=tags,
        date=date.today().strftime('%A, %B  %d, %Y at %X %Z'),
        title=os.getenv('WEB_PAGE_TITLE'))


if __name__ == '__main__':
    freezer.freeze()
