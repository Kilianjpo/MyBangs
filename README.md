![MyBangs icon](https://raw.githubusercontent.com/Kilianjpo/MyBangs/refs/heads/master/mybangs/static/icon.png)

# Mybangs

Simple search wrapper✨ with customizable Bangs‼️

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)

## Introduction

MyBangs is a powerful and user-friendly search wrapper that enhances your search experience with customizable Bangs in Duckduckgo style. Inspiration for this project was [unduck](https://github.com/t3dotgg/unduck), i really loved it but i wanted a more customizable version of it. that's why i created this project.

## Features

- Customizable search bangs
- Customizable search engines
- Easy to use
- Can be selfhosted
- Lightweight and fast
- Customizable settings and preferences
- Advanced search options
- Free and open-source license

## Demo

If you want to try MyBangs, a demo is available at [mybangs.party](https://mybangs.party/)

## Installation

To install and run MyBangs using Docker, follow these steps:

1. **Create a `compose.yml` file**:

   ```yaml
   services:
     mybangs:
       image: kilianjpo/mybangs:latest
       ports:
         - 8000:8000
       environment:
         - SECRET="" #generate with openssl rand -hex 16
         - HOST="" # for example mybangs.party
         - DEFAULT_BANGS="" # something like {"Default": "https://www.google.com/search?q=%s", "gh": "https://github.com/search?q=%s"}
         - CUSTOM_FOOTER="" # html code displayed in the footer
   ```

2. **Run the application**:

   ```sh
   docker-compose up -d
   ```

That's it!
