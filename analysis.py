from matplotlib import pyplot as plt
from db_module import Database

users = ['Rahi', 'Chaitanya']
rahi_key = 1
chaitanya_key = 2

def first_visual():
    '''
    This function is to generate a plot.
    Total messages sent by each person. 1> With media 2>Without media
    '''
    dbObj = Database()

    ##-------------------------Getting total count of messages without_media-----------------------
    without_media = []
    query = "SELECT count(message) From history where sent_by = ?", (rahi_key, )

    dbObj.make_connection()
    data = dbObj.select_query(query)
    dbObj.close_connection()

    without_media.append(data[0][0])

    query = "SELECT count(message) From history where sent_by = ?", (chaitanya_key, )

    dbObj.make_connection()
    data = dbObj.select_query(query)
    dbObj.close_connection()

    without_media.append(data[0][0])
    print(without_media)

    ##------------------------Getting Message count for only media---------------------------------
    media_only = []

    query = "SELECT count(message) From media_history where sent_by = ?", (rahi_key, )

    dbObj.make_connection()
    data = dbObj.select_query(query)
    dbObj.close_connection()

    media_only.append(data[0][0])

    query = "SELECT count(message) From media_history where sent_by = ?", (chaitanya_key, )

    dbObj.make_connection()
    data = dbObj.select_query(query)
    dbObj.close_connection()

    media_only.append(data[0][0])
    print(media_only)


first_visual()
