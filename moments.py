
from config import *
import _os
import os
from dateutil import parser
import _exif
from PIL import Image, ExifTags



class Folder(object):

	def __init__(self, path):
		self.path = path

	def get_all_images(self):
		return _os.get_all_files_ending_with(self.path, JPG_EXTENSIONS)


	def move_file(self, filepath, date):
		year = str(date.year)
		current_dir = os.path.normpath(self.path)
		year_path = os.path.join(current_dir, year)

		_os.ensure_dir(year_path)


		month = str(date.month)
		month_path = os.path.join(year_path,month)
		_os.ensure_dir(month_path)

		filename = _os.extract_filename_from_path(filepath)
		# print "[", filepath, "]->[",os.path.join(month_path, filename),"]"

		os.rename(filepath, os.path.join(month_path, filename))
		# print os.path.join(year, month)

	def reorganize(self):
		l = self.get_all_images()
		years = set()

		img_dt = {}
		for img in l:
			try:
				dt = _exif.get_date(img)
				years.add(dt.year)
				img_dt[img] = dt
				# print exif['DateTimeOriginal'],"||||||||||||||||||||||", dt, "\n"
			except Exception as e:
				# print "Failed", e
				pass


		print len(img_dt)
		print years
		years = list(years)
		years.sort()
		for year in years:
			print year
			for img, dt in img_dt.items():
				if dt.year == year:
					print "  |___", img, dt.month, dt.year
					self.move_file(img,dt)



if __name__ == "__main__":
	f = Folder("images")
	f.reorganize()
