
# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]


# [START form]
@app.route('/')
def landing():
    return render_template('create-project.html')
# [END form]


# [START created-project]
@app.route('/created-project', methods=['POST'])
def create_project_form():
    name = request.form['name']
    advertisers = request.form.getlist('advertisers')
    logging.info('Name: %s', name)

    # [END created-project]
    # [START render_template]
    return render_template(
        'show-project.html',
        name=name,
        advertisers=advertisers
    )
    # [END render_template]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
