import os

#################### GENERAL CONFIG TO SET UP IN ENVIRONMENTAL VARIABLES ############################

HOST = os.environ['HOST']
PORT = os.environ['PORT']
main_page_uri = "http://"+HOST+":"+PORT

SERVER_MODE = os.environ['SERVER_MODE'] == 'True'

# DB

user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
database = os.environ['DB_DATABASE']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']

PREFERENCE_DELIMITER = '$$'

TEST_MODE = os.environ['TEST_MODE'] == 'True'


STATUSES = (
    'START',
    'INSERT_AGE_GENDER',
    'INSERT_ITEMS_FRIENDS',
    'EVALUATE_GROUP_CONF',
    'EVALUATE_UNDERSTAND',
    'END'
)


PERCENTAGE_COMP = dict()
PERCENTAGE_COMP['START'] = 100 * (0 / (len(STATUSES)-1))
PERCENTAGE_COMP['INSERT_AGE_GENDER'] = 100 * (1 / (len(STATUSES)-1))
PERCENTAGE_COMP['INSERT_ITEMS_FRIENDS'] = 100 * (2 / (len(STATUSES)-1))
PERCENTAGE_COMP['EVALUATE_GROUP_CONF'] = 100 * (3 / (len(STATUSES)-1))
PERCENTAGE_COMP['EVALUATE_UNDERSTAND'] = 100 * (4 / (len(STATUSES)-1))
PERCENTAGE_COMP['END'] = 100 * (5 / (len(STATUSES)-1))

CURRENT_VIEW_DICT = dict()
CURRENT_VIEW_DICT['START'] = "start.html"
CURRENT_VIEW_DICT['INSERT_AGE_GENDER'] = "insert_age_gender.html"
CURRENT_VIEW_DICT['INSERT_ITEMS_FRIENDS'] = "insert_items_friends.html"
CURRENT_VIEW_DICT['EVALUATE_GROUP_CONF'] = "evaluate_group_conf.html"
CURRENT_VIEW_DICT['EVALUATE_UNDERSTAND'] = "evaluate_understand.html"
CURRENT_VIEW_DICT['END'] = "end.html"

ERROR_VIEW_DICT = dict()
# ERROR_VIEW_DICT['INVALID_USER'] = "login.html"
# ERROR_VIEW_DICT['NO_ADMIN_USER'] = "error_no_admin.html"
ERROR_VIEW_DICT['NO_USER'] = "error_no_user.html"
# ERROR_VIEW_DICT['INCOMPLETE_USER'] = "error_incomplete_user.html"
#
# ADMIN_VIEW_DICT = dict()
# ADMIN_VIEW_DICT['PROCESS_COMPLETED'] = "process_completed.html"
# ADMIN_VIEW_DICT['ADMIN_DASHBOARD'] = "admin_dashboard.html"
# ADMIN_VIEW_DICT['ADMIN_STATS'] = "admin_statistics.html"


################### TODO: SPECIFY REQUIRED PARAMETERS FOR STATUSES ##################

# REQUIRED_PARAMETERS = dict()
# REQUIRED_PARAMETERS['START_SESSION_1'] = ()
# REQUIRED_PARAMETERS['INSERT_EMAIL_NICK'] = ('email', 'nickname', 'pronoun')
# REQUIRED_PARAMETERS['INSERT_EMAIL_NICK_FRIEND'] = ('friend_email', 'friend_nickname', 'friend_pronoun')
# REQUIRED_PARAMETERS['INSERT_AGE_GENDER'] = ('age', 'gender')
# REQUIRED_PARAMETERS['INSERT_SELF_FFM'] = ('agreeableness', 'agreeableness_swap', 'conscentiousness',
#                                           'conscentiousness_swap', 'extraversion', 'extraversion_swap',
#                                           'emotional_stability', 'emotional_stability_swap', 'openess', 'openess_swap',
#                                           'attention_check', 'attention_check_swap')
# REQUIRED_PARAMETERS['INSERT_SELF_ROCI'] = ("question_" + str(i) for i in list(range(1, 29)))
#
# REQUIRED_PARAMETERS['START_SESSION_2'] = ()
# REQUIRED_PARAMETERS['INSERT_FRIEND_FFM'] = ('agreeableness', 'agreeableness_swap', 'conscentiousness',
#                                           'conscentiousness_swap', 'extraversion', 'extraversion_swap',
#                                           'emotional_stability', 'emotional_stability_swap', 'openess', 'openess_swap')
# REQUIRED_PARAMETERS['INSERT_FRIEND_ROCI'] = ("question_" + str(i) for i in list(range(1, 29)))
# # REQUIRED_PARAMETERS['EVALUATE_SONGS_INDIVIDUAL'] = list("SONG_"+ str(i) for i in list(range(3*TRACK_TO_SELECT))) +\
# #                                                    list("SONG_" + str(i) + "_SONG_ID" for i in list(range(3 * TRACK_TO_SELECT)))
# REQUIRED_PARAMETERS['EVALUATE_SONGS_INDIVIDUAL'] = list("SONG_"+ str(i) for i in list(range(TRACK_NUMBER))) +\
#                                                    list("SONG_" + str(i) + "_SONG_ID" for i in list(range(TRACK_NUMBER)))
#
# REQUIRED_PARAMETERS['START_SESSION_3'] = ()
# # REQUIRED_PARAMETERS['EVALUATE_SONGS_GROUP_FRIEND'] = list("SONG_"+ str(i) for i in list(range(2*TRACK_TO_SELECT))) +\
# #                                                    list("SONG_" + str(i) + "_SONG_ID" for i in list(range(2 * TRACK_TO_SELECT)))
# # REQUIRED_PARAMETERS['EVALUATE_SONGS_GROUP_STRANGER'] = list("SONG_"+ str(i) for i in list(range(2*TRACK_TO_SELECT))) +\
# #                                                    list("SONG_" + str(i) + "_SONG_ID" for i in list(range(2 * TRACK_TO_SELECT)))
# REQUIRED_PARAMETERS['EVALUATE_SONGS_GROUP_FRIEND'] = list("SONG_"+ str(i) for i in list(range(TRACK_NUMBER))) +\
#                                                    list("SONG_" + str(i) + "_SONG_ID" for i in list(range(TRACK_NUMBER)))
# REQUIRED_PARAMETERS['EVALUATE_SONGS_GROUP_STRANGER'] = list("SONG_"+ str(i) for i in list(range(TRACK_NUMBER))) +\
#                                                    list("SONG_" + str(i) + "_SONG_ID" for i in list(range(TRACK_NUMBER)))

PRONOUNS = dict()

PRONOUNS[1]= {
    'SUBJECT' : 'he',
    'OBJECT' : 'him',
    'POSSESSIVE_ADJ' : 'his',
    'POSSESSIVE' : 'his',
    'REFLEXIVE' : 'himself',
    'TO_BE_CON' : 'is',
    'TO_HAVE_CON' : 'has',
    'TO_CARRY_CON' : 'carries',
    'TO_WORRY_CON' : 'worries',
    'TO_TRY_CON' : 'tries',
    'VERB_CON' : 's',
    'IRR_VERB_CON' : 'es'
}

PRONOUNS[2]= {
    'SUBJECT' : 'she',
    'OBJECT' : 'her',
    'POSSESSIVE_ADJ' : 'her',
    'POSSESSIVE' : 'hers',
    'REFLEXIVE' : 'herself',
    'TO_BE_CON' : 'is',
    'TO_HAVE_CON' : 'has',
    'TO_CARRY_CON' : 'carries',
    'TO_WORRY_CON' : 'worries',
    'TO_TRY_CON' : 'tries',
    'VERB_CON' : 's',
    'IRR_VERB_CON' : 'es'
}

PRONOUNS[3]= {
    'SUBJECT' : 'they',
    'OBJECT' : 'them',
    'POSSESSIVE_ADJ' : 'their',
    'POSSESSIVE' : 'theirs',
    'REFLEXIVE' : 'themselves',
    'TO_BE_CON' : 'are',
    'TO_HAVE_CON' : 'have',
    'TO_CARRY_CON' : 'carry',
    'TO_WORRY_CON' : 'worry',
    'TO_TRY_CON' : 'try',
    'VERB_CON' : '',
    'IRR_VERB_CON' : ''
}


# ====================== GROUP CONFIGURATIONS ===================

GROUP_CONF = dict()

# UNIFORM

# user is Bob in the table on pre-registration:
#     Bob & 1 & 5 & 1 & 4 & 3 & 4 & 3 & 5 & 1 & 3 \ \
user_ratings = {
    "Rest_1": 1,
    "Rest_2": 5,
    "Rest_3": 1,
    "Rest_4": 4,
    "Rest_5": 3,
    "Rest_6": 4,
    "Rest_7": 3,
    "Rest_8": 5,
    "Rest_9": 1,
    "Rest_10": 3
}

# all the other users are in agreement
#   Alex & 4 & 5 & 4 & 5 & 4 & 4 & 3 & 2 & 1 & 1 \ \
agr_1_ratings = {
    "Rest_1": 4,
    "Rest_2": 5,
    "Rest_3": 4,
    "Rest_4": 5,
    "Rest_5": 4,
    "Rest_6": 4,
    "Rest_7": 3,
    "Rest_8": 2,
    "Rest_9": 1,
    "Rest_10": 1
}

#     Carl & 2 & 4 & 2 & 2 & 5 & 5 & 2 & 5 & 1 & 1 \ \
agr_2_ratings = {
    "Rest_1": 2,
    "Rest_2": 4,
    "Rest_3": 2,
    "Rest_4": 2,
    "Rest_5": 5,
    "Rest_6": 5,
    "Rest_7": 2,
    "Rest_8": 5,
    "Rest_9": 1,
    "Rest_10": 1
}

#     David & 1 & 4 & 1 & 2 & 5 & 5 & 2 & 2 & 2 & 1 \ \
agr_3_ratings = {
    "Rest_1": 1,
    "Rest_2": 4,
    "Rest_3": 1,
    "Rest_4": 2,
    "Rest_5": 5,
    "Rest_6": 5,
    "Rest_7": 2,
    "Rest_8": 2,
    "Rest_9": 2,
    "Rest_10": 1
}

#     Elle & 3 & 5 & 2 & 3 & 4 & 5 & 1 & 3 & 1 & 2 \\
agr_4_ratings = {
    "Rest_1": 3,
    "Rest_2": 5,
    "Rest_3": 2,
    "Rest_4": 3,
    "Rest_5": 4,
    "Rest_6": 5,
    "Rest_7": 1,
    "Rest_8": 3,
    "Rest_9": 1,
    "Rest_10": 2
}

rec_lists_uniform = dict()
rec_lists_uniform["MAJ"] = ["Rest_2", "Rest_6", "Rest_5", "Rest_8", "Rest_4", "Rest_1", "Rest_3", "Rest_7", "Rest_10", "Rest_9"]
rec_lists_uniform["APP"] = ["Rest_2", "Rest_6", "Rest_5", "Rest_4", "Rest_8", "Rest_1", "Rest_3", "Rest_7", "Rest_9", "Rest_10"]
rec_lists_uniform["ADD"] = ["Rest_2", "Rest_6", "Rest_5", "Rest_8", "Rest_4", "Rest_1", "Rest_7", "Rest_3", "Rest_10", "Rest_9"]
rec_lists_uniform["FAI"] = ["Rest_2", "Rest_8", "Rest_5", "Rest_6", "Rest_1", "Rest_4", "Rest_7", "Rest_3", "Rest_9", "Rest_10"]
rec_lists_uniform["LMS"] = ["Rest_2", "Rest_6", "Rest_5", "Rest_4", "Rest_8", "Rest_1", "Rest_3", "Rest_7", "Rest_9", "Rest_10"]
rec_lists_uniform["MPL"] = ["Rest_2", "Rest_4", "Rest_5", "Rest_6", "Rest_8", "Rest_1", "Rest_3", "Rest_7", "Rest_10", "Rest_9"]

uniform_group_conf = dict()

uniform_group_conf["USER_RATINGS"] = user_ratings
uniform_group_conf["AGR_RATINGS"] = [agr_1_ratings, agr_2_ratings, agr_3_ratings, agr_4_ratings]
uniform_group_conf["DIS_RATINGS"] = []
uniform_group_conf["REC_LISTS"] = rec_lists_uniform


GROUP_CONF["UNIFORM"] = uniform_group_conf



# DIVERGENT

# user is FRAN in the table on pre-registration:
#     Fran & 5 & 4 & 3 & 2 & 2 & 1 & 2 & 3 & 5 & 1 \ \
user_ratings = {
    "Rest_1": 5,
    "Rest_2": 4,
    "Rest_3": 3,
    "Rest_4": 2,
    "Rest_5": 2,
    "Rest_6": 1,
    "Rest_7": 2,
    "Rest_8": 3,
    "Rest_9": 5,
    "Rest_10": 1
}

# all the other users are in disagreement
#     Gene & 1 & 4 & 5 & 4 & 5 & 1 & 4 & 3 & 1 & 5 \ \
dis_1_ratings = {
    "Rest_1": 1,
    "Rest_2": 4,
    "Rest_3": 5,
    "Rest_4": 4,
    "Rest_5": 5,
    "Rest_6": 1,
    "Rest_7": 4,
    "Rest_8": 3,
    "Rest_9": 1,
    "Rest_10": 5
}

#     Hilary & 2 & 4 & 1 & 5 & 1 & 5 & 3 & 1 & 3 & 4 \ \
dis_2_ratings = {
    "Rest_1": 2,
    "Rest_2": 4,
    "Rest_3": 1,
    "Rest_4": 5,
    "Rest_5": 1,
    "Rest_6": 5,
    "Rest_7": 3,
    "Rest_8": 1,
    "Rest_9": 3,
    "Rest_10": 4
}

#     Izzy & 4 & 2 & 2 & 1 & 4 & 5 & 1 & 5 & 1 & 4 \ \
dis_3_ratings = {
    "Rest_1": 4,
    "Rest_2": 2,
    "Rest_3": 2,
    "Rest_4": 1,
    "Rest_5": 4,
    "Rest_6": 5,
    "Rest_7": 1,
    "Rest_8": 5,
    "Rest_9": 1,
    "Rest_10": 4
}

#     Jess & 1 & 1 & 4 & 4 & 5 & 5 & 4 & 4 & 5 & 1 \ \
dis_4_ratings = {
    "Rest_1": 1,
    "Rest_2": 1,
    "Rest_3": 4,
    "Rest_4": 4,
    "Rest_5": 5,
    "Rest_6": 5,
    "Rest_7": 4,
    "Rest_8": 4,
    "Rest_9": 5,
    "Rest_10": 1
}

rec_lists_divergent = dict()
rec_lists_divergent["MAJ"] = ["Rest_6", "Rest_5", "Rest_9", "Rest_3", "Rest_4", "Rest_8", "Rest_10", "Rest_1", "Rest_2", "Rest_7"]
rec_lists_divergent["APP"] = ["Rest_2", "Rest_4", "Rest_5", "Rest_6", "Rest_10", "Rest_1", "Rest_3", "Rest_7", "Rest_8", "Rest_9"]
rec_lists_divergent["ADD"] = ["Rest_5", "Rest_6", "Rest_4", "Rest_8", "Rest_2", "Rest_3", "Rest_9", "Rest_10", "Rest_7", "Rest_1"]
rec_lists_divergent["FAI"] = ["Rest_1", "Rest_3", "Rest_4", "Rest_6", "Rest_5", "Rest_9", "Rest_10", "Rest_2", "Rest_8", "Rest_7"]
rec_lists_divergent["LMS"] = ["Rest_1", "Rest_2", "Rest_3", "Rest_4", "Rest_5", "Rest_6", "Rest_7", "Rest_8", "Rest_9", "Rest_10"]
rec_lists_divergent["MPL"] = ["Rest_1", "Rest_3", "Rest_4", "Rest_5", "Rest_6", "Rest_8", "Rest_9", "Rest_10", "Rest_2", "Rest_7"]

divergent_group_conf = dict()

divergent_group_conf["USER_RATINGS"] = user_ratings
divergent_group_conf["AGR_RATINGS"] = []
divergent_group_conf["DIS_RATINGS"] = [dis_1_ratings, dis_2_ratings, dis_3_ratings, dis_4_ratings]
divergent_group_conf["REC_LISTS"] = rec_lists_divergent

GROUP_CONF["DIVERGENT"] = divergent_group_conf



# MINORITY - MIN

#    Kris & 3 & 3 & 5 & 5 & 3 & 1 & 4 & 5 & 1 & 3 \ \
#    Leslie & 2 & 5 & 5 & 1 & 3 & 1 & 5 & 3 & 3 & 4 \ \
#    Max & 4 & 4 & 3 & 1 & 3 & 1 & 4 & 5 & 2 & 5 \ \
#    Noel & 4 & 4 & 5 & 4 & 2 & 1 & 3 & 2 & 1 & 5 \ \
#    Pat & 4 & 2 & 1 & 3 & 2 & 5 & 4 & 2 & 5 & 1 \\

# PAT is the member in minority position, in this case is the user

#    Pat & 4 & 2 & 1 & 3 & 2 & 5 & 4 & 2 & 5 & 1 \\
user_ratings = {
    "Rest_1": 4,
    "Rest_2": 2,
    "Rest_3": 1,
    "Rest_4": 3,
    "Rest_5": 2,
    "Rest_6": 5,
    "Rest_7": 4,
    "Rest_8": 2,
    "Rest_9": 5,
    "Rest_10": 1
}

# all the other users are in disagreement
#    Kris & 3 & 3 & 5 & 5 & 3 & 1 & 4 & 5 & 1 & 3 \ \
dis_1_ratings = {
    "Rest_1": 3,
    "Rest_2": 3,
    "Rest_3": 5,
    "Rest_4": 5,
    "Rest_5": 3,
    "Rest_6": 1,
    "Rest_7": 4,
    "Rest_8": 5,
    "Rest_9": 1,
    "Rest_10": 3
}

#    Leslie & 2 & 5 & 5 & 1 & 3 & 1 & 5 & 3 & 3 & 4 \ \
dis_2_ratings = {
    "Rest_1": 2,
    "Rest_2": 5,
    "Rest_3": 5,
    "Rest_4": 1,
    "Rest_5": 3,
    "Rest_6": 1,
    "Rest_7": 5,
    "Rest_8": 3,
    "Rest_9": 3,
    "Rest_10": 4
}

#    Max & 4 & 4 & 3 & 1 & 3 & 1 & 4 & 5 & 2 & 5 \ \
dis_3_ratings = {
    "Rest_1": 4,
    "Rest_2": 4,
    "Rest_3": 3,
    "Rest_4": 1,
    "Rest_5": 3,
    "Rest_6": 1,
    "Rest_7": 4,
    "Rest_8": 5,
    "Rest_9": 2,
    "Rest_10": 5
}

#    Noel & 4 & 4 & 5 & 4 & 2 & 1 & 3 & 2 & 1 & 5 \ \
dis_4_ratings = {
    "Rest_1": 1,
    "Rest_2": 1,
    "Rest_3": 4,
    "Rest_4": 4,
    "Rest_5": 5,
    "Rest_6": 5,
    "Rest_7": 4,
    "Rest_8": 4,
    "Rest_9": 5,
    "Rest_10": 1
}

rec_lists_minority = dict()
rec_lists_minority["MAJ"] = ["Rest_3", "Rest_8", "Rest_10", "Rest_2", "Rest_1", "Rest_4", "Rest_7", "Rest_5", "Rest_9", "Rest_6"]
rec_lists_minority["APP"] = ["Rest_7", "Rest_1", "Rest_2", "Rest_3", "Rest_10", "Rest_4", "Rest_8", "Rest_6", "Rest_9", "Rest_5"]
rec_lists_minority["ADD"] = ["Rest_7", "Rest_3", "Rest_2", "Rest_10", "Rest_1", "Rest_8", "Rest_4", "Rest_5", "Rest_9", "Rest_6"]
rec_lists_minority["FAI"] = ["Rest_3", "Rest_2", "Rest_8", "Rest_10", "Rest_6", "Rest_4", "Rest_7", "Rest_1", "Rest_5", "Rest_9"]
rec_lists_minority["LMS"] = ["Rest_7", "Rest_1", "Rest_2", "Rest_5", "Rest_8", "Rest_3", "Rest_4", "Rest_6", "Rest_9", "Rest_10"]
rec_lists_minority["MPL"] = ["Rest_2", "Rest_3", "Rest_4", "Rest_6", "Rest_7", "Rest_8", "Rest_9", "Rest_10", "Rest_1", "Rest_5"]

minority_min_group_conf = dict()

minority_min_group_conf["USER_RATINGS"] = user_ratings
minority_min_group_conf["AGR_RATINGS"] = []
minority_min_group_conf["DIS_RATINGS"] = [dis_1_ratings, dis_2_ratings, dis_3_ratings, dis_4_ratings]
minority_min_group_conf["REC_LISTS"] = rec_lists_minority

GROUP_CONF["MINORITY_MIN"] = minority_min_group_conf



# MINORITY - MAJ

#    Kris & 3 & 3 & 5 & 5 & 3 & 1 & 4 & 5 & 1 & 3 \ \
#    Leslie & 2 & 5 & 5 & 1 & 3 & 1 & 5 & 3 & 3 & 4 \ \
#    Max & 4 & 4 & 3 & 1 & 3 & 1 & 4 & 5 & 2 & 5 \ \
#    Noel & 4 & 4 & 5 & 4 & 2 & 1 & 3 & 2 & 1 & 5 \ \
#    Pat & 4 & 2 & 1 & 3 & 2 & 5 & 4 & 2 & 5 & 1 \\

# PAT is the member in minority position, in this case is the only in disagreemenr
# The user is one of the others, we chose Leslie

#    Leslie & 2 & 5 & 5 & 1 & 3 & 1 & 5 & 3 & 3 & 4 \ \
user_ratings = {
    "Rest_1": 2,
    "Rest_2": 5,
    "Rest_3": 5,
    "Rest_4": 1,
    "Rest_5": 3,
    "Rest_6": 1,
    "Rest_7": 5,
    "Rest_8": 3,
    "Rest_9": 3,
    "Rest_10": 4
}

# all the other users are in disagreement
#    Kris & 3 & 3 & 5 & 5 & 3 & 1 & 4 & 5 & 1 & 3 \ \
agr_1_ratings = {
    "Rest_1": 3,
    "Rest_2": 3,
    "Rest_3": 5,
    "Rest_4": 5,
    "Rest_5": 3,
    "Rest_6": 1,
    "Rest_7": 4,
    "Rest_8": 5,
    "Rest_9": 1,
    "Rest_10": 3
}

#    Max & 4 & 4 & 3 & 1 & 3 & 1 & 4 & 5 & 2 & 5 \ \
agr_2_ratings = {
    "Rest_1": 4,
    "Rest_2": 4,
    "Rest_3": 3,
    "Rest_4": 1,
    "Rest_5": 3,
    "Rest_6": 1,
    "Rest_7": 4,
    "Rest_8": 5,
    "Rest_9": 2,
    "Rest_10": 5
}

#    Noel & 4 & 4 & 5 & 4 & 2 & 1 & 3 & 2 & 1 & 5 \ \
agr_3_ratings = {
    "Rest_1": 1,
    "Rest_2": 1,
    "Rest_3": 4,
    "Rest_4": 4,
    "Rest_5": 5,
    "Rest_6": 5,
    "Rest_7": 4,
    "Rest_8": 4,
    "Rest_9": 5,
    "Rest_10": 1
}

#    Pat & 4 & 2 & 1 & 3 & 2 & 5 & 4 & 2 & 5 & 1 \\
dis_1_ratings = {
    "Rest_1": 4,
    "Rest_2": 2,
    "Rest_3": 1,
    "Rest_4": 3,
    "Rest_5": 2,
    "Rest_6": 5,
    "Rest_7": 4,
    "Rest_8": 2,
    "Rest_9": 5,
    "Rest_10": 1
}

rec_lists_minority = dict()
rec_lists_minority["MAJ"] = ["Rest_3", "Rest_8", "Rest_10", "Rest_2", "Rest_1", "Rest_4", "Rest_7", "Rest_5", "Rest_9", "Rest_6"]
rec_lists_minority["APP"] = ["Rest_7", "Rest_1", "Rest_2", "Rest_3", "Rest_10", "Rest_4", "Rest_8", "Rest_6", "Rest_9", "Rest_5"]
rec_lists_minority["ADD"] = ["Rest_7", "Rest_3", "Rest_2", "Rest_10", "Rest_1", "Rest_8", "Rest_4", "Rest_5", "Rest_9", "Rest_6"]
rec_lists_minority["FAI"] = ["Rest_3", "Rest_2", "Rest_8", "Rest_10", "Rest_6", "Rest_4", "Rest_7", "Rest_1", "Rest_5", "Rest_9"]
rec_lists_minority["LMS"] = ["Rest_7", "Rest_1", "Rest_2", "Rest_5", "Rest_8", "Rest_3", "Rest_4", "Rest_6", "Rest_9", "Rest_10"]
rec_lists_minority["MPL"] = ["Rest_2", "Rest_3", "Rest_4", "Rest_6", "Rest_7", "Rest_8", "Rest_9", "Rest_10", "Rest_1", "Rest_5"]

minority_maj_group_conf = dict()

minority_maj_group_conf["USER_RATINGS"] = user_ratings
minority_maj_group_conf["AGR_RATINGS"] = [agr_1_ratings, agr_2_ratings, agr_3_ratings]
minority_maj_group_conf["DIS_RATINGS"] = [dis_1_ratings]
minority_maj_group_conf["REC_LISTS"] = rec_lists_minority

GROUP_CONF["MINORITY_MAJ"] = minority_maj_group_conf



# COALITIONAL - SMALL

#    Robin & 2 & 4 & 2 & 5 & 2 & 1 & 1 & 4 & 5 & 5 \ \
#    Sandy & 4 & 4 & 1 & 5 & 3 & 4 & 5 & 3 & 1 & 2 \ \
#    Terry & 5 & 4 & 3 & 5 & 5 & 4 & 4 & 3 & 1 & 1 \ \
#    Vic & 4 & 5 & 4 & 4 & 3 & 4 & 3 & 5 & 1 & 1 \ \
#    Willie & 1 & 4 & 1 & 3 & 3 & 2 & 1 & 4 & 5 & 5 \\

# COALITIONS ARE {ROBIN, WILLIE} AND {SANDY, TERRY, VIC}
# in this case user will be ROBIN, agreement will contain WILLIE, disagreement SANDY TERRY and VIC

#    Robin & 2 & 4 & 2 & 5 & 2 & 1 & 1 & 4 & 5 & 5 \ \
user_ratings = {
    "Rest_1": 2,
    "Rest_2": 4,
    "Rest_3": 2,
    "Rest_4": 5,
    "Rest_5": 2,
    "Rest_6": 1,
    "Rest_7": 1,
    "Rest_8": 4,
    "Rest_9": 5,
    "Rest_10":5
}

#    Willie & 1 & 4 & 1 & 3 & 3 & 2 & 1 & 4 & 5 & 5 \\
agr_1_ratings = {
    "Rest_1": 1,
    "Rest_2": 4,
    "Rest_3": 1,
    "Rest_4": 3,
    "Rest_5": 3,
    "Rest_6": 2,
    "Rest_7": 1,
    "Rest_8": 4,
    "Rest_9": 5,
    "Rest_10": 5
}

#    Sandy & 4 & 4 & 1 & 5 & 3 & 4 & 5 & 3 & 1 & 2 \ \
dis_1_ratings = {
    "Rest_1": 4,
    "Rest_2": 4,
    "Rest_3": 1,
    "Rest_4": 5,
    "Rest_5": 3,
    "Rest_6": 4,
    "Rest_7": 5,
    "Rest_8": 3,
    "Rest_9": 1,
    "Rest_10": 2
}

#    Terry & 5 & 4 & 3 & 5 & 5 & 4 & 4 & 3 & 1 & 1 \ \
dis_2_ratings = {
    "Rest_1": 5,
    "Rest_2": 4,
    "Rest_3": 3,
    "Rest_4": 5,
    "Rest_5": 5,
    "Rest_6": 4,
    "Rest_7": 4,
    "Rest_8": 3,
    "Rest_9": 1,
    "Rest_10": 1
}


#    Vic & 4 & 5 & 4 & 4 & 3 & 4 & 3 & 5 & 1 & 1 \ \
dis_3_ratings = {
    "Rest_1": 4,
    "Rest_2": 5,
    "Rest_3": 4,
    "Rest_4": 4,
    "Rest_5": 3,
    "Rest_6": 4,
    "Rest_7": 3,
    "Rest_8": 5,
    "Rest_9": 1,
    "Rest_10": 1
}

rec_lists_coalitional = dict()
rec_lists_coalitional["MAJ"] = ["Rest_4", "Rest_9", "Rest_10", "Rest_2", "Rest_8", "Rest_1", "Rest_5", "Rest_6", "Rest_3", "Rest_7"]
rec_lists_coalitional["APP"] = ["Rest_2", "Rest_4", "Rest_1", "Rest_6", "Rest_8", "Rest_7", "Rest_9", "Rest_10", "Rest_3", "Rest_5"]
rec_lists_coalitional["ADD"] = ["Rest_4", "Rest_2", "Rest_8", "Rest_1", "Rest_5", "Rest_6", "Rest_7", "Rest_10", "Rest_9", "Rest_3"]
rec_lists_coalitional["FAI"] = ["Rest_4", "Rest_7", "Rest_1", "Rest_2", "Rest_9", "Rest_10", "Rest_8", "Rest_5", "Rest_3", "Rest_6"]
rec_lists_coalitional["LMS"] = ["Rest_2", "Rest_4", "Rest_8", "Rest_5", "Rest_1", "Rest_3", "Rest_6", "Rest_7", "Rest_9", "Rest_10"]
rec_lists_coalitional["MPL"] = ["Rest_1", "Rest_2", "Rest_4", "Rest_5", "Rest_7", "Rest_8", "Rest_9", "Rest_10", "Rest_3", "Rest_6"]

coalitional_small_group_conf = dict()

coalitional_small_group_conf["USER_RATINGS"] = user_ratings
coalitional_small_group_conf["AGR_RATINGS"] = [agr_1_ratings]
coalitional_small_group_conf["DIS_RATINGS"] = [dis_1_ratings, dis_2_ratings, dis_3_ratings]
coalitional_small_group_conf["REC_LISTS"] = rec_lists_coalitional

GROUP_CONF["COALITIONAL_SMALL"] = coalitional_small_group_conf


# COALITIONAL - BIG

#    Robin & 2 & 4 & 2 & 5 & 2 & 1 & 1 & 4 & 5 & 5 \ \
#    Sandy & 4 & 4 & 1 & 5 & 3 & 4 & 5 & 3 & 1 & 2 \ \
#    Terry & 5 & 4 & 3 & 5 & 5 & 4 & 4 & 3 & 1 & 1 \ \
#    Vic & 4 & 5 & 4 & 4 & 3 & 4 & 3 & 5 & 1 & 1 \ \
#    Willie & 1 & 4 & 1 & 3 & 3 & 2 & 1 & 4 & 5 & 5 \\

# COALITIONS ARE {ROBIN, WILLIE} AND {SANDY, TERRY, VIC}
# in this case user will be SANDY, agreement will contain TERRY and VIC, disagreement ROBIN and WILLIE

#    Sandy & 4 & 4 & 1 & 5 & 3 & 4 & 5 & 3 & 1 & 2 \ \
user_ratings = {
    "Rest_1": 4,
    "Rest_2": 4,
    "Rest_3": 1,
    "Rest_4": 5,
    "Rest_5": 3,
    "Rest_6": 4,
    "Rest_7": 5,
    "Rest_8": 3,
    "Rest_9": 1,
    "Rest_10": 2
}


#    Terry & 5 & 4 & 3 & 5 & 5 & 4 & 4 & 3 & 1 & 1 \ \
agr_1_ratings = {
    "Rest_1": 5,
    "Rest_2": 4,
    "Rest_3": 3,
    "Rest_4": 5,
    "Rest_5": 5,
    "Rest_6": 4,
    "Rest_7": 4,
    "Rest_8": 3,
    "Rest_9": 1,
    "Rest_10": 1
}

#    Vic & 4 & 5 & 4 & 4 & 3 & 4 & 3 & 5 & 1 & 1 \ \
agr_2_ratings = {
    "Rest_1": 4,
    "Rest_2": 5,
    "Rest_3": 4,
    "Rest_4": 4,
    "Rest_5": 3,
    "Rest_6": 4,
    "Rest_7": 3,
    "Rest_8": 5,
    "Rest_9": 1,
    "Rest_10": 1
}

#    Robin & 2 & 4 & 2 & 5 & 2 & 1 & 1 & 4 & 5 & 5 \ \
dis_1_ratings = {
    "Rest_1": 2,
    "Rest_2": 4,
    "Rest_3": 2,
    "Rest_4": 5,
    "Rest_5": 2,
    "Rest_6": 1,
    "Rest_7": 1,
    "Rest_8": 4,
    "Rest_9": 5,
    "Rest_10":5
}

#    Willie & 1 & 4 & 1 & 3 & 3 & 2 & 1 & 4 & 5 & 5 \\
dis_2_ratings = {
    "Rest_1": 1,
    "Rest_2": 4,
    "Rest_3": 1,
    "Rest_4": 3,
    "Rest_5": 3,
    "Rest_6": 2,
    "Rest_7": 1,
    "Rest_8": 4,
    "Rest_9": 5,
    "Rest_10": 5
}

rec_lists_coalitional = dict()
rec_lists_coalitional["MAJ"] = ["Rest_4", "Rest_9", "Rest_10", "Rest_2", "Rest_8", "Rest_1", "Rest_5", "Rest_6", "Rest_3", "Rest_7"]
rec_lists_coalitional["APP"] = ["Rest_2", "Rest_4", "Rest_1", "Rest_6", "Rest_8", "Rest_7", "Rest_9", "Rest_10", "Rest_3", "Rest_5"]
rec_lists_coalitional["ADD"] = ["Rest_4", "Rest_2", "Rest_8", "Rest_1", "Rest_5", "Rest_6", "Rest_7", "Rest_10", "Rest_9", "Rest_3"]
rec_lists_coalitional["FAI"] = ["Rest_4", "Rest_7", "Rest_1", "Rest_2", "Rest_9", "Rest_10", "Rest_8", "Rest_5", "Rest_3", "Rest_6"]
rec_lists_coalitional["LMS"] = ["Rest_2", "Rest_4", "Rest_8", "Rest_5", "Rest_1", "Rest_3", "Rest_6", "Rest_7", "Rest_9", "Rest_10"]
rec_lists_coalitional["MPL"] = ["Rest_1", "Rest_2", "Rest_4", "Rest_5", "Rest_7", "Rest_8", "Rest_9", "Rest_10", "Rest_3", "Rest_6"]

coalitional_big_group_conf = dict()

coalitional_big_group_conf["USER_RATINGS"] = user_ratings
coalitional_big_group_conf["AGR_RATINGS"] = [agr_1_ratings, agr_2_ratings]
coalitional_big_group_conf["DIS_RATINGS"] = [dis_1_ratings, dis_2_ratings]
coalitional_big_group_conf["REC_LISTS"] = rec_lists_coalitional

GROUP_CONF["COALITIONAL_BIG"] = coalitional_big_group_conf

# ============================== EXPLANATIONS ==============================

EXPLANATIONS = dict()
EXPLANATIONS["ADD"] = {
    "NO_EXP": "[ITEM] has been recommended to the group.",
    "EXP": "[ITEM] has been recommended to the group since it achieves the highest total rating among the available options."
}

EXPLANATIONS["APP"] = {
    "NO_EXP": "[ITEM] has been recommended to the group.",
    "EXP": "[ITEM] has been recommended to the group since it achieves the highest number of ratings which are above 3 among the available options."
}

EXPLANATIONS["LMS"] = {
    "NO_EXP": "[ITEM] has been recommended to the group.",
    "EXP": "[ITEM] has been recommended to the group since no group members has a real problem with it among the available options."
}

EXPLANATIONS["MAJ"] = {
    "NO_EXP": "[ITEM] has been recommended to the group.",
    "EXP": "[ITEM] has been recommended to the group since most group members like it among the available options."
}

EXPLANATIONS["MPL"] = {
    "NO_EXP": "[ITEM] has been recommended to the group.",
    "EXP": "[ITEM] has been recommended to the group since it achieves the highest of all individual group members among the available options."
}

EXPLANATIONS["FAI"] = {
    "NO_EXP": "[ITEM] has been recommended to the group.",
    "EXP": "[ITEM] has been recommended to the group since it is the user [USER] turn and this is his/her favourite choice among the available options."
}

PREVIOUS_REC_TEXT = "Your group decided to avoid going in the same restaurant too often; hence, after a restaurant has " \
                    "been selected, it cannot be chosen again for the next 4 dinners.\n" \
                    "The last 3 restaurants visited are: [REST_1], [REST_2] and [REST_3]."

PREVIOUS_REC_TEXT_UNDERST = "The group decided to avoid going in the same restaurant too often; hence, after a restaurant has " \
                    "been selected, it cannot be chosen again for the next 4 dinners.\n" \
                    "The last 3 restaurants visited are: [REST_1], [REST_2] and [REST_3]."

PRESENTATION_REC_TEXT = "Using the provided ratings, the system made a suggestion for the group on the basis of the " \
                        "preferences of all the group members among the remaining options."

UNDERSTANDABILITY_SCENARIO = {
    "MEMBERS_RATINGS": {
        "Alex": {
            "Rest_1": 2,
            "Rest_2": 4,
            "Rest_3": 2,
            "Rest_4": 5,
            "Rest_5": 2,
            "Rest_6": 1,
            "Rest_7": 1,
            "Rest_8": 4,
            "Rest_9": 5,
            "Rest_10": 5,
        },
        "Gene": {
            "Rest_1": 4,
            "Rest_2": 4,
            "Rest_3": 1,
            "Rest_4": 5,
            "Rest_5": 3,
            "Rest_6": 4,
            "Rest_7": 5,
            "Rest_8": 3,
            "Rest_9": 1,
            "Rest_10": 2,
        },
        "Max": {
            "Rest_1": 5,
            "Rest_2": 4,
            "Rest_3": 3,
            "Rest_4": 5,
            "Rest_5": 5,
            "Rest_6": 4,
            "Rest_7": 4,
            "Rest_8": 3,
            "Rest_9": 1,
            "Rest_10": 1,
        },
        "Sandy": {
            "Rest_1": 4,
            "Rest_2": 5,
            "Rest_3": 4,
            "Rest_4": 4,
            "Rest_5": 3,
            "Rest_6": 4,
            "Rest_7": 3,
            "Rest_8": 5,
            "Rest_9": 1,
            "Rest_10": 1,
        }
    },
    "REC_LIST": {
        "MAJ": ["Rest_8", "Rest_9", "Rest_5", "Rest_7"],
        "APP": ["Rest_4", "Rest_8", "Rest_10", "Rest_3"],
        "ADD": ["Rest_8", "Rest_4", "Rest_9", "Rest_5"],
        "FAI": ["Rest_5", "Rest_9", "Rest_7", "Rest_8"],
        "LMS": ["Rest_4", "Rest_8", "Rest_9", "Rest_10"],
        "MPL": ["Rest_5", "Rest_7", "Rest_8", "Rest_9"]
    }
}

