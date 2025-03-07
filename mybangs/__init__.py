from flask import Flask, redirect, render_template, request

from .config import Config


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    @app.route("/")
    def index():
        bang = request.args.getlist("bang")
        engin = request.args.getlist("engin")

        # If no bangs and engines are provided, use the default ones
        if not bang and not engin:
            bangs = dict(
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
                }
            )

        elif bang and engin and len(bang) == len(engin):
            bangs = dict(zip(bang, engin))  # Create a dictionary from the two lists

        query = request.args.get("q")
        if query is None:
            return render_template("index.html", bangs=bangs, url=request.url)

        # Check if the query has a bang
        elif " !" in query:
            # Split the query in the search term and the bang
            query, bang = query.split(" !", 1)
            if bang in bangs:
                engin = bangs[bang]  # Get the engine from the bang
                return redirect(engin % query)
            else:
                # If the bang is not in the list, return a false bang page
                return render_template(
                    "false_bang.html", r_url=bangs["Default"] % query
                )

        # If the query has no bang, use the default engine
        elif " !" not in query:
            return redirect(bangs["Default"] % query)

    return app
