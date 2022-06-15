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

custom_list = pd.read_csv (r'C:/Users/ThisPC/Desktop/0.csv')
custom_list = custom_list['list_int'].to_list()

insta_username = 'username'
insta_password = 'password'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    # settings
    # will prevent commenting on and unfollowing your good friends (the images will
    # still be liked)
    session.set_dont_include(['awesomeyurii', 'ry____eong', '__myang', 'printerpan82', 'effy.kim', 'grtgrtn', 'bemeal_yoon', 'chanwaikaaa', 'heejoo.c', 'jjjasjasmine', 'ari__shark', 'bfkc_', '_hyunju.__', 'raelilblack', 'ggigie','39saku_chan','mwcho2021'])
    session.set_quota_supervisor(enabled=True, sleep_after=["unfollows"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_unfollows_hourly=25, peak_unfollows_daily=155)

    # activity
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
    # session.unfollow_users(amount=100, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=200)
    session.unfollow_users(amount=155, custom_list_enabled=True, custom_list=custom_list, custom_list_param="all", style="FIFO", unfollow_after=None, sleep_delay=600)

    
    test = telegram_bot_sendtext("Done!")
