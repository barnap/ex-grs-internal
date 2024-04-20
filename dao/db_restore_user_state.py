import dao.db_utils as db_utils


def update_user_state(state, user_id):
    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute("""
                    UPDATE user_app 
                    SET state = %s
                    WHERE id = %s
                    """, (state, user_id))

    db.commit()
    print('Executed the query')
    db.close()
    print('Closed the dao!')


if __name__ == '__main__':
    print("")
    # update_user_state('EVALUATE_SONGS_GROUP_FRIEND', '108233296746816807650')


