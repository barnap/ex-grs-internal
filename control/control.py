import sys
import random

from dao import dao_user, db_utils
import control.control_exp_conditions as ctrl_exp
import config

from utils import utils
from math import floor
import threading

sys.path.append('../')


def get_session_route(current_session):
    return config.SESSION_ROUTE[current_session]


def get_link_invited():
    return "https://<Host>:5000/consent_form_invited".replace("<Host>", config.HOST)


def get_port():
    return config.PORT


def get_url_for_server_mode(url):
    if config.SERVER_MODE:
        return url.replace('http://', 'https://', 1)
    else:
        return url

def get_percentage_comp(current_state):
    return config.PERCENTAGE_COMP[current_state]


def is_server_mode():
    return config.SERVER_MODE


def manage_quit_user(prolific_id):
    user = dao_user.load_user_data(prolific_id)
    if not user:
        # IF PROLIFIC_ID NOT IN DB: GET USER STATE AND REDIRECT TO CORRESPONDING PAGE

        # Retrieve unassigned experimental conditions
        Agg = ""
        Exp = ""

        # CREATE DB ENTRY - ASSIGN USER TO EXPERIMENTAL CONDITIONS
        dao_user.create_new_user(prolific_id, Agg, Exp, True)

        user = dao_user.load_user_data(prolific_id)

    # GET USER STATE AND REDIRECT TO CORRESPONDING PAGE
    current_state = user["Current_state"]

    # PREPARE PARAMETERS FOR PAGE DISPLAY
    add_to_session = dict()
    add_to_session['PERCENTAGE'] = config.PERCENTAGE_COMP[current_state]

    return config.CURRENT_VIEW_DICT[current_state], add_to_session


def manage_new_user(prolific_id):
    user = dao_user.load_user_data(prolific_id)
    if not user:
        # IF PROLIFIC_ID NOT IN DB: GET USER STATE AND REDIRECT TO CORRESPONDING PAGE

        with threading.Lock():
            # Retrieve unassigned experimental conditions
            Agg, Exp = ctrl_exp.get_available_conditions()
            if Agg and Exp:
                # CREATE DB ENTRY - ASSIGN USER TO EXPERIMENTAL CONDITIONS
                dao_user.create_new_user(prolific_id, Agg, Exp)

                # Update unassigned experimental condition
                ctrl_exp.update_available_conditions(Agg, Exp)

        user = dao_user.load_user_data(prolific_id)

    # GET USER STATE AND REDIRECT TO CORRESPONDING PAGE
    current_state = user["Current_state"]

    # PREPARE PARAMETERS FOR PAGE DISPLAY
    add_to_session = dict()
    add_to_session['PERCENTAGE'] = config.PERCENTAGE_COMP[current_state]

    return config.CURRENT_VIEW_DICT[current_state], add_to_session


def manage_load_age_gender(prolific_id):
    user = dao_user.load_user_data(prolific_id)
    if user:
        # UPDATE USER STATE
        current_state = user["Current_state"]
        next_state = __find_next_state(current_state)
        dao_user.update_user_status(prolific_id, next_state)

        # TODO: LOAD INFO FOR GENDER AND AGE QUESTIONS ??

        # PREPARE PARAMETERS FOR PAGE DISPLAY
        add_to_session = dict()
        add_to_session['PERCENTAGE'] = config.PERCENTAGE_COMP[current_state]

        return config.CURRENT_VIEW_DICT[current_state], add_to_session
    else:
        return config.ERROR_VIEW_DICT["NO_USER"], None


def manage_insert_age_gender(prolific_id, form):
    user = dao_user.load_user_data(prolific_id)
    if user:
        current_state = user['Current_state']

        # Retrieve age and gender
        age = form.get('age')
        gender = form.get('gender')
        name = form.get('name')

        print(age, gender)

        # TODO: IF MISSING PARAMETERS: CREATE MESSAGE AND RETURN CURRENT STATE PAGE
        error_msg = None

        # Find next state and update user info
        next_state = __find_next_state(current_state)
        dao_user.update_demographics(prolific_id, age, gender, name, next_state)

        user = dao_user.load_user_data(prolific_id)
        next_state = user['Current_state']

        # PREPARE PARAMETERS FOR PAGE DISPLAY
        add_to_session = dict()
        add_to_session['PERCENTAGE'] = config.PERCENTAGE_COMP[next_state]

        return config.CURRENT_VIEW_DICT[next_state], add_to_session
    else:
        return config.ERROR_VIEW_DICT["NO_USER"], None


def manage_insert_items_friends(prolific_id, form):
    user = dao_user.load_user_data(prolific_id)
    if user:

        btn = form.get('s1_submit')
        if btn:
            current_state = user['Current_state']

            # Retrieve friends name and restaurants
            friends_agr = list()
            friends_dis = list()
            rest_1 = list()
            rest_2 = list()
            rest_3 = list()
            rest_4 = list()
            rest_5 = list()
            for i in range(4):
                friends_agr.append(form.get('friend_agr_' + str(i + 1)))
                friends_dis.append(form.get('friend_dis_' + str(i + 1)))
            for i in range(3):
                rest_1.append(form.get('rest_1_' + str(i)))
                rest_2.append(form.get('rest_2_' + str(i)))
                rest_3.append(form.get('rest_3_' + str(i)))
                rest_4.append(form.get('rest_4_' + str(i)))
                rest_5.append(form.get('rest_5_' + str(i)))

            # TODO: IF MISSING PARAMETERS: CREATE MESSAGE AND RETURN CURRENT STATE PAGE
            error_msg = None

            # Find next state and update user friends and restaurants
            next_state = __find_next_state(current_state)
            dao_user.update_user_items_friends(prolific_id, friends_agr, friends_dis, rest_1, rest_2, rest_3, rest_4, rest_5, next_state)

        user = dao_user.load_user_data(prolific_id)
        next_state = user['Current_state']

        # Load info for evaluations of group scenarios
        personalized_scenarios = __manage_load_group_scenario(user)

        # PREPARE PARAMETERS FOR NEXT PAGE DISPLAY
        add_to_session = dict()
        add_to_session['PERCENTAGE'] = config.PERCENTAGE_COMP[next_state]
        add_to_session['SCENARIOS'] = personalized_scenarios

        return config.CURRENT_VIEW_DICT[next_state], add_to_session
    else:
        return config.ERROR_VIEW_DICT["NO_USER"], None


def __manage_load_group_scenario(user):
    # Control Conditions assigned to the user
    Agg = user["AGGREGATION"]
    Exp = user["EXPLANATION"]

    # Information to personalize the scenario
    friends_agr = [user["Friend_agree_" + str(i+1)] for i in range(4)]
    friends_dis = [user["Friend_disagree_" + str(i+1)] for i in range(4)]

    print(friends_agr)
    print(friends_dis)

    rest_1 = [user["Rest_1_" + str(i)] for i in range(3)]
    rest_2 = [user["Rest_2_" + str(i)] for i in range(3)]
    rest_3 = [user["Rest_3_" + str(i)] for i in range(3)]
    rest_4 = [user["Rest_4_" + str(i)] for i in range(3)]
    rest_5 = [user["Rest_5_" + str(i)] for i in range(3)]

    print(rest_1)
    print(rest_2)
    print(rest_3)
    print(rest_4)
    print(rest_5)

    # Get info for configurations from the config and create personalized scenarios for the user

    group_configurations = config.GROUP_CONF
    explanations = config.EXPLANATIONS

    personalized_scenarios = dict()
    num = 1
    group_conf_list = list(group_configurations.keys())
    random.shuffle(group_conf_list)
    for group_conf_name in group_conf_list:
        group_conf = group_configurations[group_conf_name]
        print(group_conf_name)
        user_ratings = group_conf["USER_RATINGS"]
        agr_ratings = group_conf["AGR_RATINGS"]
        dis_ratings = group_conf["DIS_RATINGS"]
        rec_lists = group_conf["REC_LISTS"]
        previous_rec_text = config.PREVIOUS_REC_TEXT

        # Select restaurants considering user ratings
        restaurant_names = dict()
        selected_1 = set()
        selected_2 = set()
        selected_3 = set()
        selected_4 = set()
        selected_5 = set()

        agr_names = list()
        dis_names = list()
        fairness_turn = None
        for rest_id, user_rating in user_ratings.items():
            rest_name = None
            if user_rating == 1:
                # select from rest_1
                rest_name = random.choice(list(set(rest_1).difference(selected_1)))
                selected_1.add(rest_name)
            elif user_rating == 2:
                # select from rest_2
                rest_name = random.choice(list(set(rest_2).difference(selected_2)))
                selected_2.add(rest_name)
            elif user_rating == 3:
                # select from rest_3
                rest_name = random.choice(list(set(rest_3).difference(selected_3)))
                selected_3.add(rest_name)
            elif user_rating == 4:
                # select from rest_4
                rest_name = random.choice(list(set(rest_4).difference(selected_4)))
                selected_4.add(rest_name)
            elif user_rating == 5:
                # select from rest_5
                rest_name = random.choice(list(set(rest_5).difference(selected_5)))
                selected_5.add(rest_name)

            restaurant_names[rest_id] = rest_name
            print(rest_name)

        # Select friend names considering the scenario
        if group_conf_name == "UNIFORM":
            # select all names from agreement
            agr_names = [n for n in friends_agr]
            dis_names = []
            fairness_turn = agr_names[2]
        elif group_conf_name == "DIVERGENT":
            # select all names from disagreement
            agr_names = []
            dis_names = [n for n in friends_dis]
            fairness_turn = dis_names[2]
        elif group_conf_name == "MINORITY_MIN":
            # select all names from disagreement
            agr_names = []
            dis_names = [n for n in friends_dis]
            fairness_turn = dis_names[2]
        elif group_conf_name == "MINORITY_MAJ":
            # select one name from disagreement and 3 names from agreement
            agr_names = random.sample(friends_agr, 3)
            dis_names = random.sample(friends_dis, 1)
            fairness_turn = agr_names[2]
        elif group_conf_name == "COALITIONAL_SMALL":
            # select one name from agreement, 3 from disagreement
            agr_names = random.sample(friends_agr, 1)
            dis_names = random.sample(friends_dis, 3)
            fairness_turn = dis_names[2]
        elif group_conf_name == "COALITIONAL_BIG":
            # select 2 names from agreement and 2 names from disagreemnt
            agr_names = random.sample(friends_agr, 2)
            dis_names = random.sample(friends_dis, 2)
            fairness_turn = agr_names[1]

        # Previous rec text
        previous_rec_text = previous_rec_text\
            .replace("[REST_1]", restaurant_names[rec_lists[Agg][0]])\
            .replace("[REST_2]", restaurant_names[rec_lists[Agg][1]])\
            .replace("[REST_3]", restaurant_names[rec_lists[Agg][2]])

        # Explanation text
        explanation_text = explanations[Agg][Exp]\
            .replace("[ITEM]", restaurant_names[rec_lists[Agg][3]]).replace("[USER]", fairness_turn)

        # Compose the final scenario
        scenario_info = {
            "USER_RATINGS": user_ratings,
            "AGR_RATINGS": agr_ratings,
            "DIS_RATINGS": dis_ratings,
            "REST_NAMES": restaurant_names,
            "USER_NAME": user["Name"],
            "AGR_NAMES": agr_names,
            "DIS_NAMES": dis_names,
            "PREVIOUS_REC_TEXT": previous_rec_text,
            "EXPLANATION_TEXT": explanation_text,
            "AGG": Agg,
            "EXP": Exp,
            "NUM": num
        }
        num = num + 1

        print(scenario_info)

        personalized_scenarios[group_conf_name] = scenario_info
    return personalized_scenarios


def __manage_load_understandability_scenario(user):
    Agg = user["AGGREGATION"]
    previous_rec_text = config.PREVIOUS_REC_TEXT_UNDERST
    restaurant_names = config.UNDERSTANDABILITY_SCENARIO["REC_LIST"][Agg]

    previous_rec_text = previous_rec_text \
        .replace("[REST_1]", restaurant_names[0]) \
        .replace("[REST_2]", restaurant_names[1]) \
        .replace("[REST_3]", restaurant_names[2])

    personalized_scenario = dict()
    personalized_scenario["MEMBERS_RATINGS"] = config.UNDERSTANDABILITY_SCENARIO["MEMBERS_RATINGS"]
    personalized_scenario["PREVIOUS_REC_TEXT"] = previous_rec_text
    return personalized_scenario


def manage_insert_eval_group_scenario(prolific_id, form):
    user = dao_user.load_user_data(prolific_id)

    if user:

        btn = form.get('s1_submit')
        if btn:
            current_state = user['Current_state']

            # Retrieve evaluations provided
            evaluations = dict()

            times = str(form.get('hidden_times')).split('_')
            print(times)
            for group_conf in list(config.GROUP_CONF.keys()):
                order = int(form.get(group_conf + '_ORDER'))
                print(order)
                start_time = times[order]
                evaluations[group_conf] = {
                    "IND_consensus": form.get(group_conf + '_INDconsensus'),
                    "IND_satisfaction": form.get(group_conf + '_INDsatisfaction'),
                    "IND_fairness": form.get(group_conf + '_INDfairness'),
                    "Attention": form.get(group_conf + '_Attention'),
                    "GRP_consensus": form.get(group_conf + '_GRPconsensus'),
                    "GRP_satisfaction": form.get(group_conf + '_GRPsatisfaction'),
                    "GRP_fairness": form.get(group_conf + '_GRPfairness'),
                    "Feedback": form.get(group_conf + '_Feedback'),
                    "Start_timestamp": start_time
                }

            # TODO: IF MISSING PARAMETERS: CREATE MESSAGE AND RETURN CURRENT STATE PAGE
            error_msg = None

            # Find next state and update user friends and restaurants
            next_state = __find_next_state(current_state)
            dao_user.update_group_conf_evaluations(prolific_id, evaluations, next_state)

        user = dao_user.load_user_data(prolific_id)
        next_state = user['Current_state']

        # Load info for understandability scenario evaluation
        understandability_scenario = __manage_load_understandability_scenario(user)

        # PREPARE PARAMETERS FOR NEXT PAGE DISPLAY
        add_to_session = dict()
        add_to_session['PERCENTAGE'] = config.PERCENTAGE_COMP[next_state]
        add_to_session['UND_SCENARIO'] = understandability_scenario

        return config.CURRENT_VIEW_DICT[next_state], add_to_session
    else:
        return config.ERROR_VIEW_DICT["NO_USER"], None


def manage_insert_eval_final_group(prolific_id, form):
    user = dao_user.load_user_data(prolific_id)

    if user:

        btn = form.get('s1_submit')
        if btn:
            current_state = user['Current_state']

            # Retrieve evaluations provided
            underst_system_choice = form.get('Underst_system_choice')
            underst_system_choice_feedback = form.get('Underst_system_choice_feedback')
            underst_best_choice = form.get('Underst_best_choice')
            underst_best_feedback = form.get('Underst_best_feedback')
            underst_attention = form.get('Underst_Attention')
            general_feedback = form.get('General_feedback')

            # TODO: IF MISSING PARAMETERS: CREATE MESSAGE AND RETURN CURRENT STATE PAGE
            error_msg = None

            # Find next state and update user friends and restaurants
            next_state = __find_next_state(current_state)
            dao_user.update_underst_evaluations(prolific_id,
                                                underst_system_choice, underst_system_choice_feedback,
                                                underst_best_choice, underst_best_feedback, underst_attention,
                                                general_feedback, next_state)

        user = dao_user.load_user_data(prolific_id)
        next_state = user['Current_state']

        # Load info for understandability scenario evaluation
        # understandability_scenario = __manage_load_understandability_scenario(user)

        # PREPARE PARAMETERS FOR NEXT PAGE DISPLAY
        add_to_session = dict()
        add_to_session['PERCENTAGE'] = config.PERCENTAGE_COMP[next_state]
        # add_to_session['UND_SCENARIO'] = understandability_scenario

        return config.CURRENT_VIEW_DICT[next_state], add_to_session
    else:
        return config.ERROR_VIEW_DICT["NO_USER"], None


def manage_load_debriefing(prolific_id):
    user = dao_user.load_user_data(prolific_id)
    if user:
        None
        # TODO: GET USER STATE AND REDIRECT TO CORRESPONDING PAGE
    else:
        None
        # TODO: ERROR PAGE MISSING USER
    return None


def __retrieve_required_parameters_values(params, required_parameters):
    required_parameters_values = list()
    for param in required_parameters:
        required_parameters_values.append(params[param])
    return required_parameters_values


def __find_next_state(current_state):
    print("===== FIND NEXT STATE =====")
    current_state_index = config.STATUSES.index(current_state)
    next_state_index = current_state_index + 1

    print("current state: ", current_state)
    print("current state index: ", current_state_index)

    if next_state_index >= len(config.STATUSES):
        next_state_index = len(config.STATUSES)

    next_state = config.STATUSES[next_state_index]
    print("next state: ", next_state)
    print("next state index: ", next_state_index)
    print("============================")
    return next_state


def __create_missing_parameters_msg(missing_parameters):
    if not missing_parameters:
        return None
    else:
        return "Please insert all the required information"


def create_users_export():
    return dao_user.load_users_table_as_json()
