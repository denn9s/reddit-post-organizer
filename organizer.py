import sys

def getArguments():
    argumentCount = len(sys.argv) - 1 # first argument is file name
    arguments = sys.argv[1:]
    for item in arguments:
        print(item)

def main():
    getArguments()

if __name__ == '__main__':
	main()
