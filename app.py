from flask import Flask, render_template
import functions

app = Flask(__name__)


@app.route("/")
def homepage():
    candidates = functions.load_candidates()
    return render_template("list.html", candidates=candidates)


@app.route("/candidates/<int:uid>")
def candidate_single_id(uid):
    candidates = functions.get_candidate(uid)
    return render_template("single.html", candidates=candidates)


@app.route("/search/<name>")
def candidate_search_name(name):
    candidates = functions.get_candidates_by_name(name)
    return render_template("search.html", candidates=candidates)

@app.route("/skill/<skill>")
def candidate_search_skill(skill):
    candidates = functions.get_candidates_by_skill(skill)
    return render_template("skill.html", candidates=candidates)

app.run(debug=True)
