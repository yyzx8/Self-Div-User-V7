import os, time

tokens = open('config/tokens.txt').read().splitlines()

for token in tokens:
    os.system(f"start main.py {token}")
    time.sleep(1)