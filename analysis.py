from matplotlib import pyplot as plt
from db_module import Database
import numpy as np

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

    total_chats = [without_media[0]+media_only[0], without_media[1]+media_only[1]]
    # print(total_chats)

    ##------------------------- Plotting without_media--------------------------------------
    width = 0.25
    x_index = np.arange(len(users))

    plt.style.use('fivethirtyeight')
    plt.xkcd()

    plt.bar(x_index - width, media_only, width=width, label='media only chats', color='#ADD8E6')

    plt.bar(x_index, without_media, width=width, label='without media chats', color='#ff726f')

    plt.bar(x_index + width, total_chats, width=width, label='total chats', color='#000045')

    plt.title('Messages sent by each person')
    plt.ylabel('Number of messages')

    plt.xticks(ticks=x_index, labels=users)

    plt.legend()
    plt.tight_layout()
    plt.show()

first_visual()
