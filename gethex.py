import json
import urllib

def ishexonly(string):
    hex = "abcdef0123456789ABCDEF"
    for x in string:
        if x not in hex:
            return False
    return True

def get_hexes():
    string = ""
    #open the reddit thread
    json_obj = json.loads(urllib.urlopen("http://www.reddit.com/r/programming/comments/rxve9/let_us_have_hex/.json").read())

    #put the comments in a giant string
    for comment in json_obj[1]["data"]["children"]:
        if comment["data"].has_key("body"):
            string += comment["data"]["body"] + "\n"

    hexes = []

    #find all the hex strings in that string
    for x in string.rsplit():
        if ishexonly(x) and x != "":
            if x not in hexes:
                hexes.append(x)

    return hexes

if __name__ == "__main__":
    #print all the data
    for x in get_hexes():
        print x

