def z_score_analysis(pop_mean=None, pop_std=None, obs_mean=None, sample_size=None, sig_level=None, tail=None):
	
	def compute_zscore(pop_mean, pop_std, obs_mean, sample_size):
		numerator = obs_mean - pop_mean 	#observed_mean - population_mean
		denominator = pop_std / (sample_size**0.5)  	#standard_deviation(pop) / square root sample size
		z =  numerator / denominator 	#our z score

		#specifying our decimal extent for our z score
		#statement = f"\nOur z_score is {z} \nTo how many decimal would you like to change our z_score.\nDecimal places input :"
		decimal_for_zscore = 2
		rounded_zscore = float(f"{z:.{decimal_for_zscore}f}")
		print(f"\nWe have rouded our z score to {decimal_for_zscore} decimal places and got {rounded_zscore}.\n")
		return rounded_zscore

	def plot(tail, rounded_zscore):
		from scipy.stats import norm
		import matplotlib.pyplot as plt
		import numpy as np
		if tail == 1.0:
			p_value = norm.cdf(rounded_zscore)
			if rounded_zscore < 0:
				end = p_value
				x1 = np.arange(norm.ppf(0.001), norm.ppf(end), 0.001)
				y1 = norm.pdf(x1, 0, 1)
			else:
				start = p_value
				x1 = np.arange(norm.ppf(start), norm.ppf(0.999), 0.001)
				y1 = norm.pdf(x1, 0, 1)

					#cordinates for explanation line
			x_cod = [rounded_zscore, rounded_zscore]
			y_cod = [0.00, 0.24]

			x = np.arange(norm.ppf(0.001), norm.ppf(0.999), 0.001)
			print(len(x))
			y = norm.pdf(x, 0, 1)


			fig, ax = plt.subplots(1, 1)
			label = f"P_value = {p_value}" 
			ax.plot(x, y,  'b', lw=3, alpha=0.6)
			ax.fill_between(x1, y1, 0, color='red')
			ax.plot(x_cod, y_cod, color='black', label= label)
			plt.legend("")

		else:	
			
			if rounded_zscore < 0:
				p_value = norm.cdf(rounded_zscore) / 2
				end = p_value
				x1 = np.arange(norm.ppf(0.001), norm.ppf(end), 0.001)
				y1 = norm.pdf(x1, 0, 1)
				start = 1 - p_value
				x2 = np.arange(norm.ppf(start), norm.ppf(0.999), 0.001)
				y2 = norm.pdf(x2, 0, 1)
			else:
				p_value = (1 - norm.cdf(rounded_zscore))
				end = p_value
				x1 = np.arange(norm.ppf(0.001), norm.ppf(end), 0.001)
				y1 = norm.pdf(x1, 0, 1)
				start = 1 - p_value
				x2 = np.arange(norm.ppf(start), norm.ppf(0.999), 0.001)
				y2 = norm.pdf(x2, 0, 1)

			#cordinated for vertical zscore line
			rounded_zscore = abs(rounded_zscore)
			x1_cod = [norm.ppf(end), norm.ppf(end)]
			x2_cod = [norm.ppf(start), norm.ppf(start)]
			y_cod = [0.00, 0.4]

			x = np.arange(norm.ppf(0.001), norm.ppf(0.999), 0.001)
			print(len(x))
			y = norm.pdf(x, 0, 1)

			fig, ax = plt.subplots(1, 1)
			label = f"P_value = {p_value}" 
			ax.plot(x, y,  'b', lw=3, alpha=0.6)
			ax.fill_between(x1, y1, 0, color='red')
			ax.fill_between(x2, y2, 0, color='red')
			ax.plot(x1_cod, y_cod, color='black', label= label)
			ax.plot(x2_cod, y_cod, color='black', label= label)
			plt.legend("")
		return plt.show()

	
	def analyze(tail, rounded_zscore, sig_level, mean, std):
			from scipy.stats import norm
			import matplotlib.pyplot as plt
			import numpy as np

			if tail == 1.0:
				if rounded_zscore < 0:
					p_value = norm.cdf(rounded_zscore)
				else:
					p_value = 1 - norm.cdf(rounded_zscore)
				if p_value < sig_level:
					print(f"Reject null hypothesis when sample mean is {obs_mean} and {p_value} < {sig_level}")
				else:
					print(f"Null stands when mean is {obs_mean} and {p_value} > {sig_level}")
				

			else:
				p_value = norm.cdf(rounded_zscore)
				if p_value < sig_level:
					print(f"Reject null hypothesis when sample mean is {obs_mean} and {p_value * 2} < {sig_level}")
				else:
					print(f"Null stands when mean is {obs_mean} and {p_value * 2} > {sig_level}")
					
			return plot(tail, rounded_zscore)


	

	zscore = compute_zscore(pop_mean, pop_std, obs_mean, sample_size)
	return analyze(tail, zscore, sig_level, pop_mean, pop_std)


#requests user inputs necessary for z score analysis.
#returns a list that helps in loading data to our z_score function
def parameters_loader():
	z_score_paramaters_input_values = []
	parameters_list = ["Ho : u =", "Hi : u =", "std =", "n_size", "alpha", "tail"]
	
	count = 0
	while count < len(parameters_list):
		parameter_input = float(input(f"{parameters_list[count]} : "))
		z_score_paramaters_input_values.append(parameter_input)
		count = count + 1

	return z_score_paramaters_input_values

#request user inputs needed for z_test analysis
def by_zscore():
	z_parameters = parameters_loader()
	z_test_score = z_score_analysis(z_parameters[0], z_parameters[2], z_parameters[1], z_parameters[3], z_parameters[4], z_parameters[5])
	return print("\nDone with hypthesis testing using zscore")

