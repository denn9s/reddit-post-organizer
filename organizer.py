import sys

def checkArguments(arguments):
    argumentCount = len(arguments) # first argument is file name
    if (argumentCount == 2):
        if ('redd.it' in arguments[0]) or ('reddit.com' in arguments[0]):
            return True
        else:
            return False
    else:
        return False

def getArguments():
    arguments = sys.argv[1:]
    if (checkArguments(arguments) == False):
        print('Incorrect input')

def main():
    getArguments()

if __name__ == '__main__':
	main()
