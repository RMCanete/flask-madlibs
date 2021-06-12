from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

debug = DebugToolbarExtension(app)

@app.route("/")
def story_prompts():
    """ Generate form to ask for word prompts"""

    prompts = story.prompts

    return render_template("prompts.html", prompts=prompts)

@app.route("/story")
def get_story():
    """ Display story"""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
