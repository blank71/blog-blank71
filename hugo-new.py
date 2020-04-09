import os
import subprocess

template = '''---
title: "{year}-{month}-{day}-{title}"
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
tags = input("tags:")

template = template.format(title=title, year=year, month=month, day=day, tags=tags)
filename = '{year}-{month}-{title}.md'
filename = filename.format(title=title, year=year, month=month, day=day)

path = 'content/post/{filename}'
path = path.format(filename=filename)

with open(path, mode='w') as f:
  f.write(template)

vim = "vim content/post/{filename}"
vim = vim.format(filename=filename)
print(vim)
os.system(vim)

git = '''git pull
git add {path}
git commit -m "Add {filename}"
git push origin master
'''
git = git.format(path=path, filename=filename)
os.system(git)
