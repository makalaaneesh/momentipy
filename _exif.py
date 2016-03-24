from PIL import Image, ExifTags
from dateutil import parser

def get_exif_dict(filepath):
	img = Image.open(filepath)
	e = img._getexif()
	if e is None:
		return {}

	exif = {
	    ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS
	}
	return exif


def get_date(filepath):
	exif = get_exif_dict(filepath)
	if exif is None:
		print "0"
		return None
	date,time = exif['DateTimeOriginal'].split()
	date = date.replace(":", "/")
	dt = parser.parse(date+" "+time)
	return dt
