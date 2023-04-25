"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f'{os.getcwd()}/Himawari/{config}', 'r') as json_file:
        return json.load(json_file)[key]

class Config(object):

    ##dont change
    LOGGER=True
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="./"
    DEL_CMDS=False
    BAN_STICKER="kans" 
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="Himawari"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"

    #you can change these 
    INFOPIC=True #picture while doing /info
    STRICT_GBAN=True
    API_ID=25591955 ##api id from my.telegram.org
    APP_ID=25591955 #same as API_ID
    API_HASH="190867151075b43a1d0ffb1213b16c7d" ##api hash from my.telegram.org
    APP_HASH="190867151075b43a1d0ffb1213b16c7d" #same as API_HASH
    BL_CHATS=[1] #chats to be blacklisted
    MONGO_DB_URL="mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority" ##mongo database link (necessary)
    DB_URL2="mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority" #mongo db (not necessary)
    DB_URL="postgres://zwuqioqo:0Gyr03_QtgOXvtEgYCcOuib7ALGBuHnm@hattie.db.elephantsql.com/zwuqioqo" #postgres sql database link
    REDIS_URL="redis-cli -u redis://default:0nLBaxJed1LJaNgn9xhL1oyTL49u4B1T@redis-14243.c85.us-east-1-2.ec2.cloud.redislabs.com:14243" #redis database url from redislabs.com
    TOKEN="6072150041:AAEfA3MdHfP4jzUlpkFrLCfcIRX20oSF6XM" #bot token from @BotFather
    DEV_USERS=[6273496002] #developers id
    DRAGONS=[9656] #sudo users id
    DEMONS=[1909] #support user ids
    TIGERS=[1] #commas for multiple ids
    WOLVES=[2112, 1212] #commas for multiple ids 
    EVENT_LOGS=-1001752675171 #channel id 6273496002for gban logs
    JOIN_LOGGER=-1001217847667  #log channel/group id
    OWNER_ID=5477247654 #owner id in integer
    ERROR_LOGS=-1001217847667 #support group id
    BOT_ID = 2321 #id of bot in integer value
    BOT_NAME="𝐌ɪᴢᴜᴋɪ 𝐀ᴋɪʏᴀᴍᴀ" #your bot name
    ARQ_API_KEY="TDUXGZ-KIRHFZ-DJVBLX-RVGZFD-ARQ" #ARQ api key from @ARQRobot
    ARQ_API_URL="arq.hamker.dev" #arq link
    SUPPORT_CHAT="Xd_Bot_Support" #support group username without @
    OWNER_USERNAME="Noah_Afk" #owner username without @
    UPDATES_CHANNEL="xD_Bots_Update" #Updates/News Channel username without @
    BOT_USERNAME="Mizuki_xprobot" #bot username without @
    REM_BG_API_KEY="K2dsdsYma6cZx" #not necessary
    GENIUS_API_TOKEN="e-8UdRQNrIssPyM" # api token from genius.com (not necessary)
    TIME_API_KEY="QLLLDV7SWFD3" #not necessary
    SPAMWATCH_API="J968E_20LgxrKjsdN24cqYtD~gNRTbU" #spamwatch api token from @SpamWatchBot
    WALL_API="6950f5ds6a3" #wall api (not necessary)


class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
