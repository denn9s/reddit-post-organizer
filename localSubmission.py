class LocalSubmission:
	def __init__(self, username, date, subreddit, permalink, isSelfText):
		self.username = username
		self.date = date
		self.subreddit = subreddit
		self.permalink = permalink
		self.isSelfText = isSelfText

	def setUsername(self, username):
		self.username = username

	def getUsername(self):
		return self.username

	def setDate(self, date):
		self.date = date

	def getDate(self):
		return self.date

	def setSubreddit(self, subreddit):
		self.subreddit = subreddit

	def getSubreddit(self):
		return self.subreddit

	def setPermalink(self, permalink):
		self.permalink = permalink

	def getPermalink(self):
		return self.permalink

	def setIsSelfText(self):
		self.isSelfText = isSelfText

	def getIsSelfText(self):
		return self.isSelfText