import os

def get_all_files_ending_with(path, pattern):
	image_files = []
	for dirpath, dirnames, filenames in os.walk(path):
			for _file in filenames:
				if _file.endswith(pattern):
					image_files.append(dirpath+"/"+_file)
	return image_files

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)


def extract_filename_from_path(filepath):
	try:
		last_slash = filepath.rindex("/")
		return filepath[last_slash+1:]
	except:
		return filepath