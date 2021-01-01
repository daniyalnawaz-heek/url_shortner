
#importing pyshortener module
import pyshorteners

#taking input link
link=input("enter the link:\t")

#shortening the url
shortened=pyshorteners.Shortener()
new_link=shortened.tinyurl.short(link)

#printing the shortened url
print(new_link)