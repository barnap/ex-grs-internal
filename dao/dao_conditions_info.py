import json
import sys
from collections import defaultdict

sys.path.append('../')
import dao.db_utils as db_utils


def init_conditions_info():
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO conditions_info (id, AGGREGATION, EXPLANATION) 
        VALUES 
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s),
            (%s, %s, %s)
            """,
                (1, "ADD", "EXP",
                 2, "FAI", "EXP",
                 3, "MAJ", "EXP",
                 4, "APP", "EXP",
                 5, "LMS", "EXP",
                 6, "MPL", "EXP",
                 7, "ADD", "NO_EXP",
                 8, "FAI", "NO_EXP",
                 9, "MAJ", "NO_EXP",
                 10, "APP", "NO_EXP",
                 11, "LMS", "NO_EXP",
                 12, "MPL", "NO_EXP")
                )
    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')
    return cur


def get_conditions_info():
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
            select id, AGGREGATION, EXPLANATION, required, assigned
            from conditions_info
            """)

    results = cur.fetchall()
    print('Executed the query')

    db.close()

    conditions_list = list()
    for result in results:
        condition_dict = dict()
        print(result[0])

        condition_dict["id"] = result[0]
        condition_dict["AGGREGATION"] = result[1]
        condition_dict["EXPLANATION"] = result[2]
        condition_dict["required"] = result[3]
        condition_dict["assigned"] = result[4]

        conditions_list.append(condition_dict)

    return conditions_list


def increment_assigned_conditions_info(Agg, Exp):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
                select assigned
                from conditions_info
                where AGGREGATION = %s and EXPLANATION = %s
                """, (Agg, Exp))

    result = cur.fetchone()
    print('Executed the query')

    assigned = int(result[0]) + 1

    cur = db.cursor()
    cur.execute("""
                UPDATE conditions_info
                SET assigned = %s
                where AGGREGATION = %s and EXPLANATION = %s
                """, (assigned, Agg, Exp))

    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')

    return None
