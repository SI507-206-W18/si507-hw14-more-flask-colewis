import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id": next_id} #item not defined
    next_id += 1
    entries.insert(next_id, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(next_id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for item in entries:
        if item['id'] == next_id:
            x=item['id']
    entries.remove(x)
