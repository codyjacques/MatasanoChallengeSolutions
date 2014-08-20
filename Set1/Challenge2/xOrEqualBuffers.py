import argparse


# parses the arguments and calls the function that does the work
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b1', '--first-buffer', required=True)
	parser.add_argument('-b2', '--second-buffer', required=True)
    args = vars(parser.parse_args())

    xOrValues(args['first_buffer'], args['second_buffer'])

# This function will take two buffers and return the xor of them
def xOrValues(buffer1, buffer2):
	pass

main()
