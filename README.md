# wallops

Bot to record all `WALLOPS` and global notices
recieved on an IRC server

## setup

```
$ pip3 install -r requirements.txt
$ cp config.example.yaml config.yaml
$ nano config.yaml
$ sqlite3 .wallops.db < make-database.sql
```

## running

```
$ python3 -m wallops config.yaml
```

That's it! The bot should now do it's thing.
