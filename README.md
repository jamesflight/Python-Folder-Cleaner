Simple python folder cleaner script
===================================

Keeps folders clean of old files.

For each of the directories listed in the config.yml file the script will remove any files or folders older than a specified number of days.

I use this to keep my downloads folder free of old junk.

Configure as follows:
```yaml
folders:
  - /path/to/folder1
  - /path/to/folder2
days_to_keep_files: 7
```

I use this by adding to my crobtab to run every hour:
```bash
crontab -e
```
Add:
```
0       *       *       *       *       /path/to/daemon.py
```
