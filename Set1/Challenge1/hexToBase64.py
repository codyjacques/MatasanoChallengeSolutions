import argparse
import binascii

# parses the arguments and calls the function that does the work
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-hv', '--hex-value', required=True)
	args = vars(parser.parse_args())
	
	convertValue(args['hex_value'])

# This will take a hex value and return a base64 representation
def convertValue(value):
	bits = binascii.unhexlify(value)
	val = binascii.b2a_base64(bits)
	print val
	return val

main()

