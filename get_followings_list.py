# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:34:09 2021

@author: ThisPC
"""
from instapy import InstaPy
from instapy import smart_run
import pandas as pd

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
    session.set_quota_supervisor(enabled=True, sleep_after=["unfollows"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_unfollows_hourly=25, peak_unfollows_daily=100)

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
    session.unfollow_users(amount=100, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=200)
    
#set a breakpoint at line 37.
#step into until instapy.py pops up.  
#set a breakpoint at line 3851. 
#continue until next breakpoint (3851).
#step into until unfollow_util.py pops up.  
#set a breakpoint at line 341. 
#continue until next breakpoint (341).
#run current line until var unfollow_list appears
#run below codes to save the list of followers:
# df = pd.DataFrame(unfollow_list, columns=["column"])
# df.to_csv('C:/Users/ThisPC/Desktop/' + user + '.csv', index=False)

import pandas as pd
import numpy as np
import os

df = pd.DataFrame(unfollow_list, columns=["column"])
list_int = list(range( int(len(df)/150) ))
df['list_int'] = np.tile(list_int, len(df)//len(list_int) + 1)[:len(df)]

os.chdir("C:/Users/ThisPC/Desktop/New folder")
for i, g in df.groupby('list_int'):
    g.to_csv('{}.csv'.format(i), header=True, index_label=False)
