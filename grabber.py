from prawInfo import reddit

def inputLink(link):
	submission = reddit.submission(url = link)
	return submssion

def main():
	submission = inputLink('')

if __name__ == '__main__':
	main()