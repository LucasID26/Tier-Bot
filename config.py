from pyrogram import Client
import os 

STRING = os.environ['STRING']
ownnn = [5039288972,1928677026]
own = [1928677026]

bot = Client("TierBOT",
            session_string=STRING,
            in_memory=True,
            alt_port=True)