from prawInfo import reddit

testLink = 'https://old.reddit.com/r/nba/comments/c0ky2l/board_man_celebrates/'

def inputLink(link):
	submission = reddit.submission(url = link)
	return submission

def main():
	submission = inputLink(testLink)
	print(submission.title)

if __name__ == '__main__':
	main()