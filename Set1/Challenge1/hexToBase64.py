import argparse

# parses the arguments and calls the function that does the work
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-hv', '--hex-value', required=True)
	args = vars(parser.parse_args())
	
	convertValue(args['hex_value'])

# This will take a hex value and return a base64 representation
def convertValue(value):
	pass


main()

