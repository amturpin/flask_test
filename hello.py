from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cakes')
def cakes():
	return render_template('cakes.html')

@app.route('/hello/<hours>')
def plot_most_recent(hours):
	print("Plotting %s hours" % hours)
	return render_template('page.html', hours=hours)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
