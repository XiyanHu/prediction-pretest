import requests
from bs4 import BeautifulSoup


user_list = []# put usernames here


def crawl(user_list):
	for user in user_list:
		url = "https://www.leetcode.com/" + user +"/"

		HTML = requests.get(url).content
		if not HTML:
			print "No this user!"
		soup = BeautifulSoup(HTML,"html.parser")
		solvedQuestions = soup.find_all("span",{"class":"progress-bar-success"})
		last_time = soup.find_all("span",{"class":"text-muted"})
		solveRes = ""
		if '/' in solvedQuestions[1].getText().strip():
			solveRes = solvedQuestions[1].getText().strip()
		else:
			solveRes = solvedQuestions[3].getText().strip()
		print user
		print "Solved Question : " + solveRes
		print "Most recent accepted submissions : " + last_time[0].getText().strip()

crawl(user_list)
