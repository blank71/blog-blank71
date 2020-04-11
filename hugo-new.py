import os
import subprocess

os.system("git pull")

template = '''---
title: "{title}"
author: ""
type: ""
date: {year}-{month}-{day}
subtitle: ""
image: ""
tags: [{tags}]
---
'''

title = input("title:")
year = input("year:")
month = input("month:")
day = input("day:")
number = input("number")
tags = input("tags:")

template = template.format(title=title, year=year, month=month, day=day, tags=tags)
filename = '{year}-{month}-{day}-{number}.md'
filename = filename.format(number=number, year=year, month=month, day=day)

path = 'content/post/{filename}'
path = path.format(filename=filename)

with open(path, mode='w') as f:
  f.write(template)

vim = "vim content/post/{filename}"
vim = vim.format(filename=filename)
print(vim)
os.system(vim)

os.system("hugo")

git_push_md = '''git add {path}
git commit -m "Add {filename}"
git push origin master
'''
git_push_md = git_push_md.format(path=path, filename=filename)
os.system(git_push_md)

git_push_hugo = '''git add -A 
git commit -m "hugo {filename}"
git push origin master
'''
git_push_hugo = git_push_hugo.format(filename=filename)
os.system(git_push_hugo)
