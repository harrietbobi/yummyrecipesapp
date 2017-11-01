from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("homePage.html")

@app.route("/Signup")
def Signup():
	return render_template("Signup.html")

@app.route("/addrecipes")
def addrecipes():
	return render_template("category.html")


if __name__=="__main__":
	app.run(debug=True)