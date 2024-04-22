import dao.db_utils as db_utils
import config

import pickle
import pandas as pd
import xmltodict

# Scenario_columns_names = dict()
#
# Scenario_columns_names["One"] = "QID17_TEXT"
# Scenario_columns_names["Two"] = "QID20_TEXT"
# Scenario_columns_names["Three"] = "QID23_TEXT"
# Scenario_columns_names["Four"] = "QID24_TEXT"
# Scenario_columns_names["Five"] = "QID25_TEXT"
# Scenario_columns_names["Six"] = "QID26_TEXT"
# Scenario_columns_names["Seven"] = "QID27_TEXT"
# Scenario_columns_names["Eight"] = "QID28_TEXT"
#
# Features_column_name = "QID22"


def create_info_expl_features_mock():
    dict_answers = list()
    with open("../export.csv") as file:
        lines = file.readlines()
        head = lines[0].strip().split(";")
        # print(head)
        for i in range(1, len(lines)):
            dict_answers_entry = dict()
            for j in range(len(head)):
                line_features = lines[i].strip().split(";")
                dict_answers_entry[head[j]] = line_features[j]
            dict_answers.append(dict_answers_entry)
    print(dict_answers)

    answers_list = list()
    for answer in dict_answers:

        explanation = ""

        for i in range(1, 9):
            if answer['S' + str(i)]:
                explanation = answer['S' + str(i)]

        # features = ""
        #
        # for i in range(1, 10):
        #     if answer['features_' + str(i)]:
        #         features = features + answer['features_' + str(i)] + "; "

        single_answer_dict = {
            "PREVIOUS_EXPLANATION": explanation,
            "PREVIOUS_FEATURES": answer['features'],
            "PREVIOUS_ROLE": answer['Role'],
            "PREVIOUS_SCENARIO": answer['Scenario'],
            "PREVIOUS_PROLIFIC_PID": answer['PROLIFIC_PID'],
            "ASSIGNED": "NO"
        }
        answers_list.append(single_answer_dict)

    print(answers_list)
    # for i in range(100):
    #     single_answer_dict = {
    #         "ID": i,
    #         "EXPLANATION": "EXPLANATION - " + str(i),
    #         "GENDER": "specific gender - " + str(i),
    #         "AGE": "specific age - " + str(i),
    #         "CONTENT": "specific content - " + str(i),
    #         "GENRE": "specific genre - " + str(i),
    #         "PROGRAMS": "specific programs - " + str(i),
    #         "HOURS": "specific hours - " + str(i),
    #         "TYPE_DAY": "specific type day - " + str(i),
    #         "TIME_DAY": "specific time day - " + str(i),
    #         "DEVICE": "specific device - " + str(i),
    #         "ASSIGNED": "NO"
    #     }
    #     answers_list.append(single_answer_dict)
    # print(answers_list)
    # # TODO: SAVE ON PICKLE FILE
    #
    with open("../answers.pk", "wb") as f:
        pickle.dump(answers_list, f)

    return answers_list


if __name__ == '__main__':
    create_info_expl_features_mock()
    f = open("../answers.pk", "rb")
    answers_list = pickle.load(f)
    # print(answers_list)

