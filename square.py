import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('value', type=int)
	args = parser.parse_args()

	print(args.value ** 2)