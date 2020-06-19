class LocalSubmission:
	def __init__(self, title, username, date, subreddit, permalink, isSelfText, content):
		self.title = title
		self.username = username
		self.date = date
		self.subreddit = subreddit
		self.permalink = permalink
		self.isSelfText = isSelfText
		self.content = content

	def setTitle(self, title):
		self.title = title

	def getTitle(self):
		return self.title

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

	def setIsSelfText(self, isSelfText):
		self.isSelfText = isSelfText

	def getIsSelfText(self):
		return self.isSelfText

	def setContent(self, content):
		self.content = content

	def getContent(self):
		return self.content