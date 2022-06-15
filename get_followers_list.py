# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 15:27:23 2021

@author: ThisPC
"""

import pandas as pd
from instapy import InstaPy
from instapy import smart_run

# insta_username = 'username'
# insta_password = 'password'
insta_username = 'username'
insta_password = 'password'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    # settings

    # activity
    #['sexyready_girl', 'sexy_girl_888_']
    session.follow_user_followers(['insta.sexybabes6969'], amount=7000, randomize=False, interact=False, sleep_delay=600)
    
    # session.follow_user_following(['insta.sexybabes6969'], amount=1041, randomize=False)
    
#set a breakpoint at line 26.
#step into until instapy.py pops up.  
#set a breakpoint at line 3497. 
#continue until next breakpoint (3497).
#run below codes to save the list of followers:
# df = pd.DataFrame(person_list, columns=["column"])
# df.to_csv('C:/Users/ThisPC/Desktop/' + user + '.csv', index=False)
