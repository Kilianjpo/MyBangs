from urllib.parse import quote_plus

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

		# If no bangs provided, use the default ones
		if not bang and not engin:
			bangs = app.config["DEFAULT_BANGS"]

		elif bang and engin and len(bang) == len(engin):
			bangs = dict(zip(bang, engin))  # Create a dictionary from the two lists

		query = request.args.get("q")
		if query is None:
			return render_template(
				"index.html",
				bangs=bangs,
				url=request.url,
				surl=quote_plus(request.url),
				custom_footer=app.config["CUSTOM_FOOTER"],
			)

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
					"false_bang.html",
					r_url=bangs["Default"] % query,
					custom_footer=app.config["CUSTOM_FOOTER"],
				)

		# If the query has no bang, use the default engine
		elif " !" not in query:
			return redirect(bangs["Default"] % query)

	return app
