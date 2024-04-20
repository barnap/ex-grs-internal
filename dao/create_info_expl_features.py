import dao.db_utils as db_utils
import config

import pickle


def create_info_expl_features_mock():
    answers_list = list()
    for i in range(100):
        single_answer_dict = {
            "ID": i,
            "EXPLANATION": "EXPLANATION - " + str(i),
            "GENDER": "specific gender - " + str(i),
            "AGE": "specific age - " + str(i),
            "CONTENT": "specific content - " + str(i),
            "GENRE": "specific genre - " + str(i),
            "PROGRAMS": "specific programs - " + str(i),
            "HOURS": "specific hours - " + str(i),
            "TYPE_DAY": "specific type day - " + str(i),
            "TIME_DAY": "specific time day - " + str(i),
            "DEVICE": "specific device - " + str(i),
            "ASSIGNED": "NO"
        }
        answers_list.append(single_answer_dict)
    print(answers_list)
    # TODO: SAVE ON PICKLE FILE

    f = open("../answers.pk", "wb")
    pickle.dump(answers_list, f)
    return answers_list


if __name__ == '__main__':
    create_info_expl_features_mock()
    f = open("../answers.pk", "rb")
    answers_list = pickle.load(f)
    print(answers_list)

