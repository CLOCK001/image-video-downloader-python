import requests
import pytube

print("video or image")
userInput = input("Input: ")

if userInput == "image":
	print("A python-image-downloader")
	URLp = input("URL: ")
	print("------->")
	name = input("name-of-file: ")
	print("------->")
	Type = input("type-of-file: ")

	fin = name + Type

	R = requests.get(URLp)

	with open(fin, "wb") as f:
		f.write(R.content)

	print("------------->")
	print("your image has been downloaded!")
	print("downloader by Anas sameh")

elif userInput == "video":
	print("A python-video-downloader")
	VID = input("url: ")
	
	pytube.YouTube(VID).streams.get_highest_resolution().download("video")
	
	print("your video has been downloaded!")
	quit()
