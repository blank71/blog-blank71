import os
import subprocess

template = '''---
title: "{year}{month}{day}-{title}"
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


  print(template.format(title=title, year=year, month=month, day=day))
  template = template.format(title=title, year=year, month=month, day=day)

path = 'content/post/{year}{month}{day}-{title}.md'
path = path.format(title=title, year=year, month=month, day=day)

with open(path, mode='w') as f:
  f.write(template)

with open(path) as f:
  print(f.read())

vim = "vim content/post/{year}{month}{day}-{title}.md"
vim = vim.format(title=title, year=year, month=month, day=day)
os.system(vim)

subprocess.call('PAUSE', shell=True)

git = '''git add content/post/{year}{month}{day}-{title}.md
git commit -m "add {year}{month}{day}-{title}.md"
git push origin master
'''
git = git.format(title=title, year=year, month=month, day=day)
os.system(git)
