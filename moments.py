
from config import *
import os
from PIL import Image, ExifTags
from dateutil import parser


class ExifData(object):
	def __init__(self, filepath):
		self.filepath = filepath

	def get_exif_dict(self):
		img = Image.open(self.filepath)
		exif = {
		    ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS
		}
		return exif





class Folder(object):

	def __init__(self, path):
		self.path = path
		self.subfolders = []
		self.files = []

	def get_all_images(self):
		image_files = []
		for _file in os.listdir(self.path):
			if _file.endswith(JPG_EXTENSIONS):
				image_files.append(_file)

		return image_files

# 
# class MomentFolder(Folder)
# 



if __name__ == "__main__":
	f = Folder("images")
	l = f.get_all_images()
	print len(l)
	# e = ExifData("images/IMG_1641.JPG")
	# exif = e.get_exif_dict()
	# print exif['DateTimeOriginal']

	years = set()

	img_dt = {}
	os.chdir("images")
	for img in l:
		e = ExifData(img)
		exif = e.get_exif_dict()
		try:
			date,time = exif['DateTimeOriginal'].split()
			date = date.replace(":", "/")
			dt = parser.parse(date+" "+time)
			years.add(dt.year)
			img_dt[img] = dt
			# print exif['DateTimeOriginal'],"||||||||||||||||||||||", dt, "\n"
		except:
			pass


	print len(img_dt)
	print years
	
	for year in years:
		print year
		for img, dt in img_dt.items():
			if dt.year == year:
				print "  |___", img, dt.month