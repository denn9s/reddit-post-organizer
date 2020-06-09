from prawInfo import reddit

def inputLink(link):
	submission = reddit.submission(url = link)
	return submission

def main():
	submission = inputLink('')

if __name__ == '__main__':
	main()