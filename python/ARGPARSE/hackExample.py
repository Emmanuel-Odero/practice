import argparse



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('ip', help=('ip address'))
	parser.add_argument('port', help=('port'))
	parser.add_argument('operation', help=('operation'))

	args = parser.parse_args()

	n1 = str(args.ip)
	n2 = str(args.port)

	if args.operation == 'hack':
		result = ('Computer of ip:{} port:{} is listening').format(n1, n2)
		print(result)
	else:
		print('check operation')
