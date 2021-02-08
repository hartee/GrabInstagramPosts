#!/bin/zsh

rm /Users/ea/Projects/Portfolio/Portfolio/content/music/*/*.md

cd /Users/ea/Projects/NewAdventure/GrabInstagram/grabInstagram
/usr/local/bin/pipenv run python grabMusic.py
cp /Users/ea/Projects/NewAdventure/GrabInstagram/grabInstagram/*.md /Users/ea/Projects/Portfolio/Portfolio/content/music/2020
cd /Users/ea/Projects/Portfolio/Portfolio/
/usr/local/bin/hugo
/usr/local/bin/git status
/usr/local/bin/git add .
/usr/local/bin/git commit -m "Autogenerate new music posts"
/usr/local/bin/git push
