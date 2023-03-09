#!/usr/bin/env python
'''
Generate a summary page for a youtube playlist
'''
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
    meta = bios.read('./meta.json')

    return render_template('index.j2',
        meta=meta,
        playlist_title=meta['title'],
        date=date.today().strftime('%A, %B  %d, %Y at %X %Z'))


if __name__ == '__main__':
    freezer.freeze()
