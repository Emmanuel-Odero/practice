from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    
	def calculator(x):
			result =  (2 * (x ** 2)) + 3
			return result

	x = [x for x in range(10)]
	y = []
	for val in x:
		y.append(calculator(val))

	plt.style.use('dark_background')
	plt.xlabel('Rate')
	plt.ylabel('Change')
	plt.plot(x,y)
	plt.savefig('./static/poly.png')

	# code below saved the plot after rendering the template
	# without loading the intended static file saved_plots 
	'''plt.style.use('dark_background')
				plt.plot(x, y)
				plt.xlabel('Rate')
				plt.ylabel('Change')
				plt.savefig('saved_plots/exponential.png')'''

	return render_template('index.html',x=x, y=y, calculator=calculator)

if __name__ == '__main__':
	app.run(debug=True)