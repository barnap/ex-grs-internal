import json
import sys
import dao.db_utils as db_utils
import config
from random import choice
from math import ceil

sys.path.append('../')


# REVISED
def load_user_data(prolific_id):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
        select 
            PROLIFIC_ID,
            AGGREGATION,
            EXPLANATION,
            Start_time,
            End_time,
            Age_group,
            Gender,
            Rest_1_0,
            Rest_1_1,
            Rest_1_2,
            Rest_2_0,
            Rest_2_1,
            Rest_2_2,
            Rest_3_0,
            Rest_3_1,
            Rest_3_2,
            Rest_4_0,
            Rest_4_1,
            Rest_4_2,
            Rest_5_0,
            Rest_5_1,
            Rest_5_2,
            Friend_agree_1,
            Friend_agree_2,
            Friend_agree_3,
            Friend_agree_4,
            Friend_disagree_1,
            Friend_disagree_2,
            Friend_disagree_3,
            Friend_disagree_4,
            Uniform_start_timestamp,
            Uniform_IND_fairness,
            Uniform_IND_consensus,
            Uniform_IND_satisfaction,
            Uniform_GRP_fairness,
            Uniform_GRP_consensus,
            Uniform_GRP_satisfaction,
            Uniform_feedback,
            Divergent_start_timestamp,
            Divergent_IND_fairness,
            Divergent_IND_consensus,
            Divergent_IND_satisfaction,
            Divergent_GRP_fairness,
            Divergent_GRP_consensus,
            Divergent_GRP_satisfaction,
            Divergent_feedback,
            Coalitional_small_start_timestamp,
            Coalitional_small_IND_fairness,
            Coalitional_small_IND_consensus,
            Coalitional_small_IND_satisfaction,
            Coalitional_small_GRP_fairness,
            Coalitional_small_GRP_consensus,
            Coalitional_small_GRP_satisfaction,
            Coalitional_small_feedback,
            Coalitional_large_start_timestamp,
            Coalitional_large_IND_fairness,
            Coalitional_large_IND_consensus,
            Coalitional_large_IND_satisfaction,
            Coalitional_large_GRP_fairness,
            Coalitional_large_GRP_consensus,
            Coalitional_large_GRP_satisfaction,
            Coalitional_large_feedback,
            Minority_min_start_timestamp,
            Minority_min_IND_fairness,
            Minority_min_IND_consensus,
            Minority_min_IND_satisfaction,
            Minority_min_GRP_fairness,
            Minority_min_GRP_consensus,
            Minority_min_GRP_satisfaction,
            Minority_min_feedback,
            Minority_maj_start_timestamp,
            Minority_maj_IND_fairness,
            Minority_maj_IND_consensus,
            Minority_maj_IND_satisfaction,
            Minority_maj_GRP_fairness,
            Minority_maj_GRP_consensus,
            Minority_maj_GRP_satisfaction,
            Minority_maj_feedback,
            Underst_start_timestamp,
            Underst_system_choice,
            Underst_system_choice_feedback,
            Underst_best_choice,
            Underst_best_feedback,
            Underst_end_timestamp,
            General_feedback,
            Attention_uniform,
            Attention_divergent,
            Attention_coalitional_small,
            Attention_coalitional_large,
            Attention_minority_min,
            Attention_minority_maj,
            Attention_understandability,
            Current_state,
            Name
        from user_app
        where PROLIFIC_ID = (%s)
        """, (prolific_id, ))

    result = cur.fetchone()
    print('Executed the query')
    print(result)
    db.close()

    user_dict = dict()
    if result:
        print(result[0])
        user_dict["PROLIFIC_ID"] = result[0]
        user_dict["AGGREGATION"] = result[1]
        user_dict["EXPLANATION"] = result[2]
        user_dict["Start_time"] = result[3]
        user_dict["End_time"] = result[4]
        user_dict["Age_group"] = result[5]
        user_dict["Gender"] = result[6]
        user_dict["Rest_1_0"] = result[7]
        user_dict["Rest_1_1"] = result[8]
        user_dict["Rest_1_2"] = result[9]
        user_dict["Rest_2_0"] = result[10]
        user_dict["Rest_2_1"] = result[11]
        user_dict["Rest_2_2"] = result[12]
        user_dict["Rest_3_0"] = result[13]
        user_dict["Rest_3_1"] = result[14]
        user_dict["Rest_3_2"] = result[15]
        user_dict["Rest_4_0"] = result[16]
        user_dict["Rest_4_1"] = result[17]
        user_dict["Rest_4_2"] = result[18]
        user_dict["Rest_5_0"] = result[19]
        user_dict["Rest_5_1"] = result[20]
        user_dict["Rest_5_2"] = result[21]
        user_dict["Friend_agree_1"] = result[22]
        user_dict["Friend_agree_2"] = result[23]
        user_dict["Friend_agree_3"] = result[24]
        user_dict["Friend_agree_4"] = result[25]
        user_dict["Friend_disagree_1"] = result[26]
        user_dict["Friend_disagree_2"] = result[27]
        user_dict["Friend_disagree_3"] = result[28]
        user_dict["Friend_disagree_4"] = result[29]
        user_dict["Uniform_start_timestamp"] = result[30]
        user_dict["Uniform_IND_fairness"] = result[31]
        user_dict["Uniform_IND_consensus"] = result[32]
        user_dict["Uniform_IND_satisfaction"] = result[33]
        user_dict["Uniform_GRP_fairness"] = result[34]
        user_dict["Uniform_GRP_consensus"] = result[35]
        user_dict["Uniform_GRP_satisfaction"] = result[36]
        user_dict["Uniform_feedback"] = result[37]
        user_dict["Divergent_start_timestamp"] = result[38]
        user_dict["Divergent_IND_fairness"] = result[39]
        user_dict["Divergent_IND_consensus"] = result[40]
        user_dict["Divergent_IND_satisfaction"] = result[41]
        user_dict["Divergent_GRP_fairness"] = result[42]
        user_dict["Divergent_GRP_consensus"] = result[43]
        user_dict["Divergent_GRP_satisfaction"] = result[44]
        user_dict["Divergent_feedback"] = result[45]
        user_dict["Coalitional_small_start_timestamp"] = result[46]
        user_dict["Coalitional_small_IND_fairness"] = result[47]
        user_dict["Coalitional_small_IND_consensus"] = result[48]
        user_dict["Coalitional_small_IND_satisfaction"] = result[49]
        user_dict["Coalitional_small_GRP_fairness"] = result[50]
        user_dict["Coalitional_small_GRP_consensus"] = result[51]
        user_dict["Coalitional_small_GRP_satisfaction"] = result[52]
        user_dict["Coalitional_small_feedback"] = result[53]
        user_dict["Coalitional_large_start_timestamp"] = result[54]
        user_dict["Coalitional_large_IND_fairness"] = result[55]
        user_dict["Coalitional_large_IND_consensus"] = result[56]
        user_dict["Coalitional_large_IND_satisfaction"] = result[57]
        user_dict["Coalitional_large_GRP_fairness"] = result[58]
        user_dict["Coalitional_large_GRP_consensus"] = result[59]
        user_dict["Coalitional_large_GRP_satisfaction"] = result[60]
        user_dict["Coalitional_large_feedback"] = result[61]
        user_dict["Minority_min_start_timestamp"] = result[62]
        user_dict["Minority_min_IND_fairness"] = result[63]
        user_dict["Minority_min_IND_consensus"] = result[64]
        user_dict["Minority_min_IND_satisfaction"] = result[65]
        user_dict["Minority_min_GRP_fairness"] = result[66]
        user_dict["Minority_min_GRP_consensus"] = result[67]
        user_dict["Minority_min_GRP_satisfaction"] = result[68]
        user_dict["Minority_min_feedback"] = result[69]
        user_dict["Minority_maj_start_timestamp"] = result[70]
        user_dict["Minority_maj_IND_fairness"] = result[71]
        user_dict["Minority_maj_IND_consensus"] = result[72]
        user_dict["Minority_maj_IND_satisfaction"] = result[73]
        user_dict["Minority_maj_GRP_fairness"] = result[74]
        user_dict["Minority_maj_GRP_consensus"] = result[75]
        user_dict["Minority_maj_GRP_satisfaction"] = result[76]
        user_dict["Minority_maj_feedback"] = result[77]
        user_dict["Underst_start_timestamp"] = result[78]
        user_dict["Underst_system_choice"] = result[79]
        user_dict["Underst_system_choice_feedback"] = result[80]
        user_dict["Underst_best_choice"] = result[81]
        user_dict["Underst_best_feedback"] = result[82]
        user_dict["Underst_end_timestamp"] = result[83]
        user_dict["General_feedback"] = result[84]
        user_dict["Attention_uniform"] = result[85]
        user_dict["Attention_divergent"] = result[86]
        user_dict["Attention_coalitional_small"] = result[87]
        user_dict["Attention_coalitional_large"] = result[88]
        user_dict["Attention_minority_min"] = result[89]
        user_dict["Attention_minority_maj"] = result[90]
        user_dict["Attention_understandability"] = result[91]
        user_dict["Current_state"] = result[92]
        user_dict["Name"] = result[93]

    print(user_dict)
    return user_dict


# Revised
def create_new_user(prolific_id, Agg, Exp, quit_user=False):
    initial_state = config.STATUSES[1]
    end_state = config.STATUSES[len(config.STATUSES) - 1]
    if not quit_user:
        state = initial_state
    else:
        state = end_state

    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO user_app (PROLIFIC_ID, AGGREGATION, EXPLANATION, Start_time, Current_state) 
        VALUES (%s, %s, %s, NOW(), %s)
        """, (prolific_id, Agg, Exp, state))
    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')
    return cur


# Revised
def update_user_status(prolific_id, next_state):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
            UPDATE user_app 
            SET Current_state = %s
            WHERE PROLIFIC_ID = %s
            """, (next_state, prolific_id))
    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')
    return cur


# Revised
def update_demographics(prolific_id, age, gender, name, next_state):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
                UPDATE user_app 
                SET age_group = %s, gender = %s, name = %s, current_state = %s
                WHERE PROLIFIC_ID = %s
                """, (age, gender, name, next_state, prolific_id))
    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')
    return cur


# Revised
def update_user_items_friends(prolific_id, friends_agr, friends_dis, rest_1, rest_2, rest_3, rest_4, rest_5, next_state):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
                UPDATE user_app 
                SET 
                    Rest_1_0 = %s,
                    Rest_1_1 = %s,
                    Rest_1_2 = %s,
                    Rest_2_0 = %s,
                    Rest_2_1 = %s,
                    Rest_2_2 = %s,
                    Rest_3_0 = %s,
                    Rest_3_1 = %s,
                    Rest_3_2 = %s,
                    Rest_4_0 = %s,
                    Rest_4_1 = %s,
                    Rest_4_2 = %s,
                    Rest_5_0 = %s,
                    Rest_5_1 = %s,
                    Rest_5_2 = %s,
                    Friend_agree_1 = %s,
                    Friend_agree_2 = %s,
                    Friend_agree_3 = %s,
                    Friend_agree_4 = %s,
                    Friend_disagree_1 = %s,
                    Friend_disagree_2 = %s,
                    Friend_disagree_3 = %s,
                    Friend_disagree_4 = %s,
                    current_state = %s
                WHERE PROLIFIC_ID = %s
                """, (rest_1[0],
                      rest_1[1],
                      rest_1[2],
                      rest_2[0],
                      rest_2[1],
                      rest_2[2],
                      rest_3[0],
                      rest_3[1],
                      rest_3[2],
                      rest_4[0],
                      rest_4[1],
                      rest_4[2],
                      rest_5[0],
                      rest_5[1],
                      rest_5[2],
                      friends_agr[0],
                      friends_agr[1],
                      friends_agr[2],
                      friends_agr[3],
                      friends_dis[0],
                      friends_dis[1],
                      friends_dis[2],
                      friends_dis[3],
                      next_state, prolific_id))
    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')
    return cur


# Revised
def update_group_conf_evaluations(prolific_id, evaluations, next_state):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
                    UPDATE user_app 
                    SET 
                        Uniform_IND_fairness = %s,
                        Uniform_IND_consensus = %s,
                        Uniform_IND_satisfaction = %s,
                        Uniform_GRP_fairness = %s,
                        Uniform_GRP_consensus = %s,
                        Uniform_GRP_satisfaction = %s,
                        Uniform_feedback  = %s,
                        Divergent_IND_fairness = %s,
                        Divergent_IND_consensus = %s,
                        Divergent_IND_satisfaction = %s,
                        Divergent_GRP_fairness = %s,
                        Divergent_GRP_consensus = %s,
                        Divergent_GRP_satisfaction = %s,
                        Divergent_feedback  = %s,
                        Coalitional_small_IND_fairness = %s,
                        Coalitional_small_IND_consensus = %s,
                        Coalitional_small_IND_satisfaction = %s,
                        Coalitional_small_GRP_fairness = %s,
                        Coalitional_small_GRP_consensus = %s,
                        Coalitional_small_GRP_satisfaction = %s,
                        Coalitional_small_feedback  = %s,
                        Coalitional_large_IND_fairness = %s,
                        Coalitional_large_IND_consensus = %s,
                        Coalitional_large_IND_satisfaction = %s,
                        Coalitional_large_GRP_fairness = %s,
                        Coalitional_large_GRP_consensus = %s,
                        Coalitional_large_GRP_satisfaction = %s,
                        Coalitional_large_feedback  = %s,
                        Minority_min_IND_fairness = %s,
                        Minority_min_IND_consensus = %s,
                        Minority_min_IND_satisfaction = %s,
                        Minority_min_GRP_fairness = %s,
                        Minority_min_GRP_consensus = %s,
                        Minority_min_GRP_satisfaction = %s,
                        Minority_min_feedback  = %s,
                        Minority_maj_IND_fairness = %s,
                        Minority_maj_IND_consensus = %s,
                        Minority_maj_IND_satisfaction = %s,
                        Minority_maj_GRP_fairness = %s,
                        Minority_maj_GRP_consensus = %s,
                        Minority_maj_GRP_satisfaction = %s,
                        Minority_maj_feedback = %s,
                        Attention_uniform = %s,
                        Attention_divergent = %s,
                        Attention_coalitional_small = %s,
                        Attention_coalitional_large = %s,
                        Attention_minority_min = %s,
                        Attention_minority_maj = %s,
                        Underst_start_timestamp = NOW(),
                        Uniform_start_timestamp = %s,
                        Divergent_start_timestamp = %s,
                        Coalitional_small_start_timestamp = %s,
                        Coalitional_large_start_timestamp = %s,
                        Minority_min_start_timestamp = %s,
                        Minority_maj_start_timestamp = %s,
                        current_state = %s
                    WHERE PROLIFIC_ID = %s
                    """, (
        evaluations["UNIFORM"]["IND_consensus"],
        evaluations["UNIFORM"]["IND_satisfaction"],
        evaluations["UNIFORM"]["IND_fairness"],
        evaluations["UNIFORM"]["GRP_consensus"],
        evaluations["UNIFORM"]["GRP_satisfaction"],
        evaluations["UNIFORM"]["GRP_fairness"],
        evaluations["UNIFORM"]["Feedback"],
        evaluations["DIVERGENT"]["IND_consensus"],
        evaluations["DIVERGENT"]["IND_satisfaction"],
        evaluations["DIVERGENT"]["IND_fairness"],
        evaluations["DIVERGENT"]["GRP_consensus"],
        evaluations["DIVERGENT"]["GRP_satisfaction"],
        evaluations["DIVERGENT"]["GRP_fairness"],
        evaluations["DIVERGENT"]["Feedback"],
        evaluations["COALITIONAL_SMALL"]["IND_consensus"],
        evaluations["COALITIONAL_SMALL"]["IND_satisfaction"],
        evaluations["COALITIONAL_SMALL"]["IND_fairness"],
        evaluations["COALITIONAL_SMALL"]["GRP_consensus"],
        evaluations["COALITIONAL_SMALL"]["GRP_satisfaction"],
        evaluations["COALITIONAL_SMALL"]["GRP_fairness"],
        evaluations["COALITIONAL_SMALL"]["Feedback"],
        evaluations["COALITIONAL_BIG"]["IND_consensus"],
        evaluations["COALITIONAL_BIG"]["IND_satisfaction"],
        evaluations["COALITIONAL_BIG"]["IND_fairness"],
        evaluations["COALITIONAL_BIG"]["GRP_consensus"],
        evaluations["COALITIONAL_BIG"]["GRP_satisfaction"],
        evaluations["COALITIONAL_BIG"]["GRP_fairness"],
        evaluations["COALITIONAL_BIG"]["Feedback"],
        evaluations["MINORITY_MIN"]["IND_consensus"],
        evaluations["MINORITY_MIN"]["IND_satisfaction"],
        evaluations["MINORITY_MIN"]["IND_fairness"],
        evaluations["MINORITY_MIN"]["GRP_consensus"],
        evaluations["MINORITY_MIN"]["GRP_satisfaction"],
        evaluations["MINORITY_MIN"]["GRP_fairness"],
        evaluations["MINORITY_MIN"]["Feedback"],
        evaluations["MINORITY_MAJ"]["IND_consensus"],
        evaluations["MINORITY_MAJ"]["IND_satisfaction"],
        evaluations["MINORITY_MAJ"]["IND_fairness"],
        evaluations["MINORITY_MAJ"]["GRP_consensus"],
        evaluations["MINORITY_MAJ"]["GRP_satisfaction"],
        evaluations["MINORITY_MAJ"]["GRP_fairness"],
        evaluations["MINORITY_MAJ"]["Feedback"],
        evaluations["UNIFORM"]["Attention"],
        evaluations["DIVERGENT"]["Attention"],
        evaluations["COALITIONAL_SMALL"]["Attention"],
        evaluations["COALITIONAL_BIG"]["Attention"],
        evaluations["MINORITY_MIN"]["Attention"],
        evaluations["MINORITY_MAJ"]["Attention"],
        evaluations["UNIFORM"]["Start_timestamp"],
        evaluations["DIVERGENT"]["Start_timestamp"],
        evaluations["COALITIONAL_SMALL"]["Start_timestamp"],
        evaluations["COALITIONAL_BIG"]["Start_timestamp"],
        evaluations["MINORITY_MIN"]["Start_timestamp"],
        evaluations["MINORITY_MAJ"]["Start_timestamp"],
        next_state, prolific_id))
    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')
    return cur


# Revised
def update_underst_evaluations(prolific_id, underst_system_choice, underst_system_choice_feedback,
                               underst_best_choice, underst_best_feedback, underst_attention,
                               general_feedback, next_state):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
                        UPDATE user_app 
                        SET 
                            Underst_system_choice = %s,
                            Underst_system_choice_feedback = %s,
                            Underst_best_choice = %s,
                            Underst_best_feedback = %s,
                            Attention_understandability = %s,
                            General_feedback = %s,
                            Underst_end_timestamp = NOW(),
                            End_time = NOW(),
                            current_state = %s
                        WHERE PROLIFIC_ID = %s
                        """, (underst_system_choice, underst_system_choice_feedback, underst_best_choice,
                              underst_best_feedback, underst_attention, general_feedback, next_state, prolific_id))
    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')
    return cur


# Revised
def load_users_table_as_json():
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
            select 
                PROLIFIC_ID,
                AGGREGATION,
                EXPLANATION,
                Start_time,
                End_time,
                Age_group,
                Gender,
                Rest_1_0,
                Rest_1_1,
                Rest_1_2,
                Rest_2_0,
                Rest_2_1,
                Rest_2_2,
                Rest_3_0,
                Rest_3_1,
                Rest_3_2,
                Rest_4_0,
                Rest_4_1,
                Rest_4_2,
                Rest_5_0,
                Rest_5_1,
                Rest_5_2,
                Friend_agree_1,
                Friend_agree_2,
                Friend_agree_3,
                Friend_agree_4,
                Friend_disagree_1,
                Friend_disagree_2,
                Friend_disagree_3,
                Friend_disagree_4,
                Uniform_start_timestamp,
                Uniform_IND_fairness,
                Uniform_IND_consensus,
                Uniform_IND_satisfaction,
                Uniform_GRP_fairness,
                Uniform_GRP_consensus,
                Uniform_GRP_satisfaction,
                Uniform_feedback,
                Divergent_start_timestamp,
                Divergent_IND_fairness,
                Divergent_IND_consensus,
                Divergent_IND_satisfaction,
                Divergent_GRP_fairness,
                Divergent_GRP_consensus,
                Divergent_GRP_satisfaction,
                Divergent_feedback,
                Coalitional_small_start_timestamp,
                Coalitional_small_IND_fairness,
                Coalitional_small_IND_consensus,
                Coalitional_small_IND_satisfaction,
                Coalitional_small_GRP_fairness,
                Coalitional_small_GRP_consensus,
                Coalitional_small_GRP_satisfaction,
                Coalitional_small_feedback,
                Coalitional_large_start_timestamp,
                Coalitional_large_IND_fairness,
                Coalitional_large_IND_consensus,
                Coalitional_large_IND_satisfaction,
                Coalitional_large_GRP_fairness,
                Coalitional_large_GRP_consensus,
                Coalitional_large_GRP_satisfaction,
                Coalitional_large_feedback,
                Minority_min_start_timestamp,
                Minority_min_IND_fairness,
                Minority_min_IND_consensus,
                Minority_min_IND_satisfaction,
                Minority_min_GRP_fairness,
                Minority_min_GRP_consensus,
                Minority_min_GRP_satisfaction,
                Minority_min_feedback,
                Minority_maj_start_timestamp,
                Minority_maj_IND_fairness,
                Minority_maj_IND_consensus,
                Minority_maj_IND_satisfaction,
                Minority_maj_GRP_fairness,
                Minority_maj_GRP_consensus,
                Minority_maj_GRP_satisfaction,
                Minority_maj_feedback,
                Underst_start_timestamp,
                Underst_system_choice,
                Underst_system_choice_feedback,
                Underst_best_choice,
                Underst_best_feedback,
                Underst_end_timestamp,
                General_feedback,
                Attention_uniform,
                Attention_divergent,
                Attention_coalitional_small,
                Attention_coalitional_large,
                Attention_minority_min,
                Attention_minority_maj,
                Attention_understandability,
                Current_state,
                Name
            from user_app
            """)

    results = cur.fetchall()
    print('Executed the query')

    db.close()

    users_list = list()
    for result in results:

        user_dict = dict()

        user_dict["PROLIFIC_ID"] = result[0]
        user_dict["AGGREGATION"] = result[1]
        user_dict["EXPLANATION"] = result[2]
        user_dict["Start_time"] = result[3].strftime('%Y-%m-%d %H:%M:%S') if result[3] else None
        user_dict["End_time"] = result[4].strftime('%Y-%m-%d %H:%M:%S') if result[4] else None
        user_dict["Age_group"] = result[5]
        user_dict["Gender"] = result[6]
        user_dict["Rest_1_0"] = result[7]
        user_dict["Rest_1_1"] = result[8]
        user_dict["Rest_1_2"] = result[9]
        user_dict["Rest_2_0"] = result[10]
        user_dict["Rest_2_1"] = result[11]
        user_dict["Rest_2_2"] = result[12]
        user_dict["Rest_3_0"] = result[13]
        user_dict["Rest_3_1"] = result[14]
        user_dict["Rest_3_2"] = result[15]
        user_dict["Rest_4_0"] = result[16]
        user_dict["Rest_4_1"] = result[17]
        user_dict["Rest_4_2"] = result[18]
        user_dict["Rest_5_0"] = result[19]
        user_dict["Rest_5_1"] = result[20]
        user_dict["Rest_5_2"] = result[21]
        user_dict["Friend_agree_1"] = result[22]
        user_dict["Friend_agree_2"] = result[23]
        user_dict["Friend_agree_3"] = result[24]
        user_dict["Friend_agree_4"] = result[25]
        user_dict["Friend_disagree_1"] = result[26]
        user_dict["Friend_disagree_2"] = result[27]
        user_dict["Friend_disagree_3"] = result[28]
        user_dict["Friend_disagree_4"] = result[29]
        user_dict["Uniform_start_timestamp"] = result[30].strftime('%Y-%m-%d %H:%M:%S') if result[30] else None
        user_dict["Uniform_IND_fairness"] = result[31]
        user_dict["Uniform_IND_consensus"] = result[32]
        user_dict["Uniform_IND_satisfaction"] = result[33]
        user_dict["Uniform_GRP_fairness"] = result[34]
        user_dict["Uniform_GRP_consensus"] = result[35]
        user_dict["Uniform_GRP_satisfaction"] = result[36]
        user_dict["Uniform_feedback"] = result[37]
        user_dict["Divergent_start_timestamp"] = result[38].strftime('%Y-%m-%d %H:%M:%S') if result[38] else None
        user_dict["Divergent_IND_fairness"] = result[39]
        user_dict["Divergent_IND_consensus"] = result[40]
        user_dict["Divergent_IND_satisfaction"] = result[41]
        user_dict["Divergent_GRP_fairness"] = result[42]
        user_dict["Divergent_GRP_consensus"] = result[43]
        user_dict["Divergent_GRP_satisfaction"] = result[44]
        user_dict["Divergent_feedback"] = result[45]
        user_dict["Coalitional_small_start_timestamp"] = result[46].strftime('%Y-%m-%d %H:%M:%S') if result[46] else None
        user_dict["Coalitional_small_IND_fairness"] = result[47]
        user_dict["Coalitional_small_IND_consensus"] = result[48]
        user_dict["Coalitional_small_IND_satisfaction"] = result[49]
        user_dict["Coalitional_small_GRP_fairness"] = result[50]
        user_dict["Coalitional_small_GRP_consensus"] = result[51]
        user_dict["Coalitional_small_GRP_satisfaction"] = result[52]
        user_dict["Coalitional_small_feedback"] = result[53]
        user_dict["Coalitional_large_start_timestamp"] = result[54].strftime('%Y-%m-%d %H:%M:%S') if result[54] else None
        user_dict["Coalitional_large_IND_fairness"] = result[55]
        user_dict["Coalitional_large_IND_consensus"] = result[56]
        user_dict["Coalitional_large_IND_satisfaction"] = result[57]
        user_dict["Coalitional_large_GRP_fairness"] = result[58]
        user_dict["Coalitional_large_GRP_consensus"] = result[59]
        user_dict["Coalitional_large_GRP_satisfaction"] = result[60]
        user_dict["Coalitional_large_feedback"] = result[61]
        user_dict["Minority_min_start_timestamp"] = result[62].strftime('%Y-%m-%d %H:%M:%S') if result[62] else None
        user_dict["Minority_min_IND_fairness"] = result[63]
        user_dict["Minority_min_IND_consensus"] = result[64]
        user_dict["Minority_min_IND_satisfaction"] = result[65]
        user_dict["Minority_min_GRP_fairness"] = result[66]
        user_dict["Minority_min_GRP_consensus"] = result[67]
        user_dict["Minority_min_GRP_satisfaction"] = result[68]
        user_dict["Minority_min_feedback"] = result[69]
        user_dict["Minority_maj_start_timestamp"] = result[70].strftime('%Y-%m-%d %H:%M:%S') if result[70] else None
        user_dict["Minority_maj_IND_fairness"] = result[71]
        user_dict["Minority_maj_IND_consensus"] = result[72]
        user_dict["Minority_maj_IND_satisfaction"] = result[73]
        user_dict["Minority_maj_GRP_fairness"] = result[74]
        user_dict["Minority_maj_GRP_consensus"] = result[75]
        user_dict["Minority_maj_GRP_satisfaction"] = result[76]
        user_dict["Minority_maj_feedback"] = result[77]
        user_dict["Underst_start_timestamp"] = result[78].strftime('%Y-%m-%d %H:%M:%S') if result[78] else None
        user_dict["Underst_system_choice"] = result[79]
        user_dict["Underst_system_choice_feedback"] = result[80]
        user_dict["Underst_best_choice"] = result[81]
        user_dict["Underst_best_feedback"] = result[82]
        user_dict["Underst_end_timestamp"] = result[83].strftime('%Y-%m-%d %H:%M:%S') if result[83] else None
        user_dict["General_feedback"] = result[84]
        user_dict["Attention_uniform"] = result[85]
        user_dict["Attention_divergent"] = result[86]
        user_dict["Attention_coalitional_small"] = result[87]
        user_dict["Attention_coalitional_large"] = result[88]
        user_dict["Attention_minority_min"] = result[89]
        user_dict["Attention_minority_maj"] = result[90]
        user_dict["Attention_understandability"] = result[91]
        user_dict["Current_state"] = result[92]
        user_dict["Name"] = result[93]

        users_list.append(user_dict)

    return json.dumps(users_list, indent=2)
