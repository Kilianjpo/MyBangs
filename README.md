<img width="200px" src="https://raw.githubusercontent.com/Kilianjpo/MyBangs/refs/heads/master/mybangs/static/icon.png" align="center" alt="GitHub Readme Stats" />

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
         - SECRET=
         - HOST=
   ```

2. **Set otional enviroment variables**

<table>
  <thead>
    <tr>
      <th>Env var name</th>
      <th>Description</th>
      <th>Optional</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SECRET</td>
      <td>A secret string can be generated with "openssl rand -hex 16"</td>
      <td>No</td>
      <td></td>
    </tr>
    <tr>
      <td>HOST</td>
      <td>Domain under which the instance is accessible for example mybangs.party</td>
      <td>No</td>
      <td></td>
    </tr>
    <tr>
      <td>DEFAULT_BANGS</td>
      <td>A Python Dictionary. Each key represents a bang the exclamation mark must be removed. The default key defines the search engine that will be used if no bang is specified.</td>
      <td>Yes</td>
      <td>{
				"Default": "https://www.google.com/search?q=%s",
				"g": "https://www.google.com/search?q=%s",
				"d": "https://duckduckgo.com/?q=%s",
				"b": "https://www.bing.com/search?q=%s",
				"y": "https://search.yahoo.com/search?p=%s",
				"w": "https://en.wikipedia.org/wiki/Special:Search?search=%s",
				"yt": "https://www.youtube.com/results?search_query=%s",
				"a": "https://www.amazon.com/s?k=%s",
				"e": "https://www.ebay.com/sch/i.html?_nkw=%s",
				"x": "https://x.com/search?q=%s",
				"i": "https://www.instagram.com/explore/search/keyword/?q=%s",
				"r": "https://www.reddit.com/search/?q=%s",
				"gh": "https://github.com/search?q=%s",
				"gm": "https://www.google.com/maps/search/%s",
				"gi": "https://www.google.com/search?tbm=isch&q=%s",
			},</td>
    </tr>
    <tr>
      <td>CUSTOM_FOOTER</td>
      <td>Any valid HTML code. Will be displayed in the footer.</td>
      <td>Yes</td>
      <td></td>
    </tr>
  </tbody>
</table>

3. **Run the application**:

   ```sh
   docker-compose up -d
   ```

That's it!
