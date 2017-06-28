actor = {"name": "Kanu Reeves", "rank": "Awesome"}

def get_last_name():
    try:
        print  actor["last_name"]
    except KeyError:
        print (actor["name"]).split(" ")[1]

get_last_name()
