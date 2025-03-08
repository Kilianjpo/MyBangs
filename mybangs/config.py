from os import getenv


class Config:
	SECRET_KEY = getenv("SECRET")
	SESSION_COOKIE_DOMAIN = getenv("HOST")
	SERVER_NAME = getenv("HOST")
	DEFAULT_BANGS = dict(
		getenv(
			"DEFAULT_BANGS",
			{
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
			},
		)
	)
	CUSTOM_FOOTER = getenv("CUSTOM_FOOTER")
