import sys

import pickle
import threading
import json
from flask import Flask, redirect, render_template, request, session, flash, jsonify, url_for, Response
from flask_mail import Mail
from flask_session import Session
from oauthlib.oauth2 import WebApplicationClient
import requests

# Local import
import control.control as ctrl
from utils import utils

# client_id, client_secret, google_discovery_url = ctrl.get_google_app_configurations()
redirect_uri = ""

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
# app.config.update(ctrl.get_mail_settings())
mail = Mail(app)

Session(app)
# client = WebApplicationClient(client_id)


@app.route('/consent_form', methods=['GET', 'POST'])
def consent_form():
    '''
    access to the login page with spotify account
    :return:
    '''

    # Recover prolific id

    prolific_id = request.args.get('PROLIFIC_ID')
    session["prolific_id"] = prolific_id

    return render_template('consent.html')


@app.route('/quit_experiment', methods=['GET', 'POST'])
def quit_experiment():
    prolific_id = session["prolific_id"]
    # TODO: MANAGE MISSING PROLIFIC_ID!!!

    next_view, add_to_session = ctrl.manage_quit_user(prolific_id)
    if add_to_session:
        for key in add_to_session:
            session[key] = add_to_session[key]
    return render_template(next_view)


@app.route('/instructions', methods=['GET', 'POST'])
def instructions():
    prolific_id = session["prolific_id"]
    # TODO: MANAGE MISSING PROLIFIC_ID!!!

    next_view, add_to_session = ctrl.manage_new_user(prolific_id)
    if add_to_session:
        for key in add_to_session:
            session[key] = add_to_session[key]
    return render_template(next_view)


@app.route('/insert_age_gender', methods=['GET', 'POST'])
def insert_age_gender():
    prolific_id = session["prolific_id"]
    next_view, add_to_session = ctrl.manage_load_age_gender(prolific_id)
    if add_to_session:
        for key in add_to_session:
            session[key] = add_to_session[key]
    return render_template(next_view)


@app.route('/insert_items_friends', methods=['GET', 'POST'])
def insert_items_friends():
    prolific_id = session["prolific_id"]
    next_view, add_to_session = ctrl.manage_insert_age_gender(prolific_id, request.form)
    # ctrl.manage_load_items_friends(prolific_id)
    if add_to_session:
        for key in add_to_session:
            session[key] = add_to_session[key]
    return render_template(next_view)


@app.route('/evaluate_group_scenario', methods=['GET', 'POST'])
def evaluate_group_scenario():
    prolific_id = session["prolific_id"]

    next_view, add_to_session = ctrl.manage_insert_items_friends(prolific_id, request.form)

    if add_to_session:
        for key in add_to_session:
            session[key] = add_to_session[key]
    return render_template(next_view)


@app.route('/evaluate_final_group', methods=['GET', 'POST'])
def evaluate_final_group():
    prolific_id = session["prolific_id"]

    next_view, add_to_session = ctrl.manage_insert_eval_group_scenario(prolific_id, request.form)

    if add_to_session:
        for key in add_to_session:
            session[key] = add_to_session[key]
    return render_template(next_view)


@app.route('/debriefing', methods=['GET', 'POST'])
def debriefing():
    prolific_id = session["prolific_id"]

    next_view, add_to_session = ctrl.manage_insert_eval_final_group(prolific_id, request.form)

    if add_to_session:
        for key in add_to_session:
            session[key] = add_to_session[key]
    return render_template(next_view)


########## ADMIN ROUTES ##########


@app.route('/download_users', methods=['GET', 'POST'])
def download_users():

    export = ctrl.create_users_export()

    # json_export = jsonify(export_dict)
    return Response(
        export,
        mimetype="text/json",
        headers={"Content-disposition": "attachment; filename=users.json"})


@app.route('/info_expl_features_test')
def info_expl_features_test():
    args = request.args
    dict_args = args.to_dict()
    Scenario = dict_args["Scenario"]

    # Synchronize block
    selected_answer = {
        "PREVIOUS_EXPLANATION": "TEST EXPLANATION",
        "PREVIOUS_FEATURES": "Feature A, B, and C",
        "PREVIOUS_ROLE": "Role Test",
        "PREVIOUS_SCENARIO": Scenario,
        "PREVIOUS_PROLIFIC_PID": "TEST_PID",
        "ASSIGNED": "YES"
    }
    return jsonify(selected_answer)


@app.route('/info_expl_test')
def info_expl_features():
    args = request.args
    dict_args = args.to_dict()
    Scenario = dict_args["Scenario"]

    # Synchronize block
    with threading.Lock():
    # Open file with info for explanations and features
        f = open("../answers.pk", "rb")
        answers_list = pickle.load(f)
        selected_answer = None
        for answer in answers_list:
            if answer["PREVIOUS_SCENARIO"] == Scenario:
                if answer["ASSIGNED"] == "NO":
                    answer["ASSIGNED"] = "YES"
                    selected_answer = answer
                    break
        if not selected_answer:
            print("no available answers")
            return jsonify(dict())
        else:
            f = open("../answers.pk", "wb")
            pickle.dump(answers_list, f)
            return jsonify(selected_answer)


if __name__ == "__main__":
    if ctrl.is_server_mode():
        app.run(host='0.0.0.0', port=ctrl.get_port())
    else:
        app.run(host='0.0.0.0', port=ctrl.get_port(), ssl_context='adhoc') # adhoc creates SSL certificate for HTTPS adhoc, not trusted - use only for beta test
