import urllib.request;
import urllib.parse;
import re;
import json;
import os;

WATCH_URL = "https://www.youtube.com/watch?v=";

userInput = input("Enter a keyword to search: ");
userInput = userInput.replace(" ", "+");
count = int(input("Enter a maximum count: "));

url = "https://www.youtube.com/results?search_query=" + userInput;
response = urllib.request.urlopen(url).read().decode();
videoIds = re.findall(r"watch\?v=(\S{11})", response);

i = 0;
j = 0;
lastId = "";
for id in videoIds:
    if (i >= count): break;
    if (lastId == id):
        j += 1;
        continue;
    lastId = id;
    entry = {"format": "json", "url": WATCH_URL + "%s" % id}
    query = urllib.parse.urlencode(entry)
    url = "https://www.youtube.com/oembed?" + query

    response = urllib.request.urlopen(url).read();
    data = json.loads(response.decode());
    print(str(j) + ". " + data['title'] + "\n" + WATCH_URL + id);
    i += 1;
    j += 1;

choice = int(input("Enter a video to play: "));
choice = max(0, min(choice, len(videoIds) - 1));

os.system("vlc --no-video " + WATCH_URL + videoIds[choice]);
