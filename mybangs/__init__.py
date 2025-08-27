from urllib.parse import quote_plus

from flask import Flask, redirect, render_template, request, session

from .config import Config


def create_app():
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(Config)

	# Make session permanent
	@app.before_request
	def make_session_permanent():
		session.permanent = True

	@app.route("/")
	def index():
		# Get parameters from the request
		bang = request.args.getlist("bang")
		engin = request.args.getlist("engin")
		query = request.args.get("q")

		# Use values from url parameters if provided
		if bang and engin and len(bang) == len(engin):
			bangs = dict(zip(bang, engin))  # Create a dictionary from the two lists
			session["bangs"] = bangs  # Update session with url parameters

		# If no bangs provided in the url, use the session bangs if available
		elif "bangs" in session:
			bangs = session["bangs"]

		# If no bangs provided, use the default ones
		elif not bang and not engin:
			bangs = app.config["DEFAULT_BANGS"]
			session["bangs"] = bangs

		# Return the index when no query is provided
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
				return redirect(engin % quote_plus(query))
			else:
				# If the bang is not in the list, return a false bang page
				return render_template(
					"false_bang.html",
					r_url=bangs["Default"] % quote_plus(query),
					custom_footer=app.config["CUSTOM_FOOTER"],
				)

		# If the query has no bang, use the default engine
		elif " !" not in query:
			return redirect(bangs["Default"] % quote_plus(query))

	return app
