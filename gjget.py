import requests as rq

# choose what to get
print("jacks gjget")
print(" ")
getoption = int(input("what to get 1: account. 2: levels. 3: Account Comments ").strip())
gdserversecret = "Wmfd2893gb7" # nice gdserversecret rob

if getoption == 1:
    targetid = input("Enter AccountID: ").strip()
    if targetid == "":
        targetid = 31436582
    else:
        targetid = int(targetid)
    print("Requesting user from https://www.boomlings.com/database/getGJUserInfo20.php")
    url = "https://www.boomlings.com/database/getGJUserInfo20.php"
    params = {"secret": gdserversecret, "targetAccountID": targetid }
    headers = {
    "User-Agent": ""
    }

    req = rq.post(url, data=params, headers=headers)
elif getoption == 2:
    cat = int(input("What Catagory: 0 = search | 1 = most download | 2 = most liked | 3 = trending | 4 = recent | 6 = featured | 7 = magic | 11 = awarded | 16 = hall of fame | 27 = sent | 31 = hyped | ").strip())
    if cat == 5 or cat == 10 or cat == 0:
        query = str(input("Search Query: ").strip())
    else:
        query = ""
    print("Requesting level from https://www.boomlings.com/database/getGJLevels21.php")
    url = "https://www.boomlings.com/database/getGJLevels21.php"
    params = {"secret": gdserversecret, "type": cat, "str": query}
    headers = {
    "User-Agent": ""
    }
    req = rq.post(url, data=params, headers=headers)

elif getoption == 3:
    targetid = input("Enter AccountID: ").strip()
    if targetid == "":
        targetid = 31436582
    else:
        targetid = int(targetid)
    print("Requesting user from https://www.boomlings.com/database/getGJAccountComments20.php")
    url = "https://www.boomlings.com/database/getGJAccountComments20.php"
    params = {"secret": gdserversecret, "accountID": targetid, "page": 0 }
    headers = {
    "User-Agent": ""
    }

    req = rq.post(url, data=params, headers=headers)
    print(req.text)

# make info readable
userkey = {
    1: "userName",
    2: "userID",
    3: "stars",
    4: "demonCount",
    6: "ranking",
    7: "accountHighlight",
    8: "creatorpoints",
    9: "iconID",
    10: "color",
    11: "color2",
    12: "shipID",
    13: "gdserversecretCoins",
    14: "iconType",
    15: "special",
    16: "accountID",
    17: "userCoins",
    18: "messageState",
    19: "friendsState",
    20: "youTube",
    21: "accIcon",
    22: "accShip",
    23: "accBall",
    24: "accBird",
    25: "accDart",
    26: "accRobot",
    28: "accGlow",
    29: "isRegistered",
    30: "globalRank",
    31: "friendState",
    38: "messages",
    43: "accSpider",
    44: "twitter",
    45: "twitch",
    46: "diamonds",
    48: "accExplosion",
    49: "mod",
    50: "commentHistoryState",
    51: "color3",
    52: "moons",
    53: "accSwing",
    54: "accJetpack",
    55: "demons",
    56: "classicLevels",
    57: "platformerLevels",
    58: "discord",
    59: "instagram",
    60: "tiktok",
    61: "custom",
    62: "groupState",
    63: "gO",
    64: "friendsSince",
    67: "followers",
    68: "following",
    69: "isFollowing",
}
levelkey = {
    1: "levelID",
    2: "levelName",
    3: "description",
    4: "levelString",
    5: "version",
    6: "playerID",
    8: "difficultyDenominator",
    9: "difficultyNumerator",
    10: "downloads",
    11: "completes",
    12: "officialSong",
    13: "gameVersion",
    14: "likes",
    15: "length",
    16: "dislikes",
    17: "demon",
    18: "stars",
    19: "featureScore",
    20: "starRatings",
    21: "starRatingsSum",
    22: "minStarRatings",
    23: "maxStarRatings",
    24: "demonVotes",
    25: "auto",
    26: "recordString",
    27: "password",
    28: "uploadDate",
    29: "updateDate",
    30: "copiedID",
    31: "twoPlayer",
    32: "rateStars",
    33: "rateFeature",
    34: "rateUser",
    35: "customSongID",
    36: "extraString",
    37: "coins",
    38: "verifiedCoins",
    39: "starsRequested",
    40: "lowDetailMode",
    41: "dailyNumber",
    42: "epic",
    43: "demonDifficulty",
    44: "isGauntlet",
    45: "objects",
    46: "editorTime",
    47: "editorTimeCopies",
    48: "settingsString",
    52: "songIDs",
    53: "sfxIDs",
    54: "songSize",
    57: "verificationTime",
    58: "unknown58",
    62: "exactUploadTime",
    63: "exactUpdateTime",
    65: "timelyID"
}

data = req.text

if data == "-1":
    print("Not Found")
    input()
    exit()

def parse_user(data):
    parts = data.split(":")
    user = {}

    for i in range(0, len(parts) - 1, 2):
        key = int(parts[i])
        value = parts[i + 1]

        name = userkey.get(key, f"unknown_{key}")
        user[name] = value
    return user

def parse_level(data):
    parts = data.split(":")
    level = {}

    for i in range(0, len(parts) - 1, 2):
        key = int(parts[i])
        value = parts[i + 1]

        name = levelkey.get(key, f"unknown_{key}")
        level[name] = value
    return level

if getoption == 1:
    player = parse_user(data)

    print(player["userName"], "| Name")
    print(player["stars"], "| Stars")
    print(player["moons"], "| Moons")
    print(player["demonCount"], "| Demons")
    print(player["globalRank"], "| Rank")
    print(player.get("diamonds", "Not available"), "| Diamonds")
    print(player["followers"], "| Followers")

elif getoption == 2:
    levels = data.split("#")[0].split("|")

    for leveldata in levels:
        level = parse_level(leveldata)
        print(level.get("levelName", "Unknown"), "| Name")
        print(level.get("levelID", "Unknown"), "| LevelID")
        print(level.get("downloads", "Unknown"), "| Downloads")
        print(level.get("likes", "Unknown"), "| Likes")
        print(level.get("stars", "Unknown"), "| Stars")
        print("--------------------")
input()

input()