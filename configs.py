# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = os.environ.get("1340222")
	API_HASH = os.environ.get("334133d7097f902e7c3776dbe5ab9ea8")
	BOT_TOKEN = os.environ.get("5227373896:AAF-QdagR3i_X6-rClQ4S7TYMAyJRSr_blY")
	
	STREAMTAPE_API_PASS = os.environ.get("6RV1XvxmZMc9D4Z")
	STREAMTAPE_API_USERNAME = os.environ.get("6234b79c86891789d4ec")
	SESSION_NAME = os.environ.get("SESSION_NAME", "streamLogosBot")
	BOT_OWNER = os.environ.get("2054421248")
	
	DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
	HELP_TEXT = """
Send me any Media & Choose Upload Server,
I will Upload the Media to that server.

Currently I can Upload to:
> GoFile.io
> Streamtape.com
> Pixeldrain.com

Also I can do a lot of things from Inline!
__Check Below Buttons >>>__
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
