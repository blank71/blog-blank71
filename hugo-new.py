import os
import subprocess

template = '''---
title: "{year}-{month}-{day}-{title}"
author: ""
type: ""
date: {year}-{month}-{day}
subtitle: ""
image: ""
tags: []
---
'''

if __name__ == "__main__":
  title = input("title:")
  year = input("year:")
  month = input("month:")
  day = input("day:")

template = template.format(title=title, year=year, month=month, day=day)
filename = '{year}-{month}-{title}.md'
filename = filename.format(title=title, year=year, month=month, day=day)

path = 'content/post/{filename}'
path = path.format(filename=filename)

with open(path, mode='w') as f:
  f.write(template)

with open(path) as f:
  print(f.read())

vim = "vim content/post/{filename}"
vim = vim.format(filename=filename)
print(vim)
os.system(vim)

git = '''git pull
git add content/post/{filename}
git commit -m "Add {filename}"
git push origin master
'''
git = git.format(filename=filename)
os.system(git)
