from prawInfo import reddit
from localSubmission import LocalSubmission

testLink = 'https://old.reddit.com/r/nba/comments/c0ky2l/board_man_celebrates/'
testSelfLink = 'https://old.reddit.com/r/nba/comments/hbgvqi/marcus_morris_career_points_7248_markieff_morris/'

def inputLink(link):
	submission = reddit.submission(url = link)
	return submission

def createLocalSubmissionObject(submission):
	title = submission.title
	username = submission.author.name
	date = submission.created_utc
	subreddit = submission.subreddit.display_name
	permalink = submission.permalink
	selfText = submission.is_self
	if (selfText is False):
		url = submission.url
	else:
		url = 'https://reddit.com' + submission.permalink
	return LocalSubmission(title, username, date, subreddit, permalink, selfText)

def main():
	submission = inputLink(testSelfLink)
	submissionObject = createLocalSubmissionObject(submission)

if __name__ == '__main__':
	main()