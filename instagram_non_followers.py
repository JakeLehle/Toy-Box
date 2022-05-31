#Importing libraries
from instabot import Bot
import config
import requests
import re
#Set up the bot object
bot = Bot()
#Login and request cookies from session and save them
bot.login(username = config.USERNAME, password = config.PASSWORD)
#Get following list
not_following = set(bot.following) - set(bot.followers)
raw_username_list = []
#Convert userID to username
for x in not_following:
    print(x)
for x in not_following:
    x = str(x)
    url = ['https://www.instagram.com/graphql/query/?query_hash=c9100bf9110dd6361671f113dd02e7d6&variables={\"user_id\":\"', x, '\",\"include_chaining\":false,\"include_reel\":true,\"include_suggested_users\":false,\"include_logged_out_extras\":false,\"include_highlight_reels\":false,\"include_related_profiles\":false}']
    url_joined = ''.join(url)
    url_output = requests.get(url_joined)
    raw_username_list.append(url_output.text)
#Filter string
print(raw_username_list)
joined_username_string = "".join(raw_username_list)
username_list = re.findall('username\":\"\s?(.{1,30})\s?\"},\"owner', joined_username_string)
with open('people_to_unfollow.txt', 'w') as fp:
    for name in username_list:
        fp.write("%s\n" % name)
    print('You sexy bastard. You are done!')
