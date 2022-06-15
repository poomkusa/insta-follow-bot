# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:34:09 2021

@author: ThisPC
"""
from instapy import InstaPy
from instapy import smart_run
import requests
import pandas as pd

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1944131190:AAHno4s7j8H2Ksdxwzh8QsEwr5b_Q1aaVtQ'
    bot_chatID = '1942096678'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

user = 'sexy_girl_888_'
accs = pd.read_csv (r'C:/Users/ThisPC/Desktop/' + user + '.csv')
accs = accs['column'].to_list()

insta_username = 'username'
insta_password = 'password'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    # settings
    # will prevent commenting on and unfollowing your good friends (the images will
    # still be liked)
    session.set_dont_include(["cheesesaytv"])
    session.set_quota_supervisor(enabled=True, sleep_after=["follows"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_follows_hourly=50, peak_follows_daily=150)

    # activity
    # session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
    #['sexyready_girl', 'sexy_girl_888_']
    # session.follow_user_followers(['sexyready_girl'], amount=400,
    #                               randomize=False, interact=False, sleep_delay=600)
    session.follow_by_list(accs, times=1, sleep_delay=60, interact=False)

    # """ Unfollow not follower users...
    # """
    # session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
    #                        style="FIFO",
    #                        unfollow_after=12 * 60 * 60, sleep_delay=601)

    # """ Unfollow all users followed by InstaPy...
    # """
    # session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
    #                        style="FIFO", unfollow_after=24 * 60 * 60,
    #                        sleep_delay=601)
    
    test = telegram_bot_sendtext("Done!")
