# Newspaper Crawler

This repository only contains the Crawler of the Newspaper Website. For backend and frontend refer to below repositories. 
Frontend - https://github.com/rishabh-9000/newspaper-frontend
Backend - https://github.com/rishabh-9000/newspaper-backend.git
Live IP - http://35.154.105.119/

## Prerequisite

1. virtualenv - https://virtualenv.pypa.io/en/stable/installation.html
2. python 3 - https://www.python.org/downloads/

## Project Setup

Clone this repository

```bash
git clone https://github.com/rishabh-9000/news_crawler.git
```

Create virtualenv

```bash
virtualenv --python=python3 <env_name>
(--python=python3 is optional for windows)
```

Activate virtualenv

```bash
source <env_name>/bin/activate (For Linux and MacOS)
./<env_name>/Scripts/activate (For Windows)
```

Install Dependencies

```bash
cd news_crawler
pip3 install -r requirements.txt
```

Run Crawler

```bash
cd newspaper
scrapy crawl timesofindia
```
