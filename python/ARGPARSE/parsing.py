import argparse



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('no1', help='first variable')
	parser.add_argument('--no2', help=('second variable'))

	args = parser.parse_args()

	n1 = int(args.no1)
	n2 = int(args.no2)

	result = n1 * n2

	print('\n[+] Multiplying {} with {} results to {}. \n'.format(n1, n2, result))