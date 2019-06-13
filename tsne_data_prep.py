import argparse
import os
import random
from shutil import copyfile

def main(TRAIN_DATA_PATH, SAVE_DATA_PATH, sample_size):
	data = list(os.walk(TRAIN_DATA_PATH))
	class_size = len(data)
	if not os.path.exists(SAVE_DATA_PATH): 
		os.mkdir(SAVE_DATA_PATH)
	for path_header, _, file_list in data[1:]:
		random.shuffle(file_list)
		for item_name in file_list[:sample_size]:
			copyfile(os.path.join(path_header, item_name), os.path.join(SAVE_DATA_PATH, path_header[path_header.rfind('/')+1:]+ item_name))


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--size', type=int, default=4, help="number of sample images taken from the data")
	parser.add_argument('-tp', '--train_path', type=str, default='data/cars_train', help="source directory of images")
	parser.add_argument('-sp', '--save_path', type=str, default='data/tsne_data', help="save directory for images used in tsne")


	args = parser.parse_args()
	TRAIN_DATA_PATH = args.train_path
	SAVE_DATA_PATH = args.save_path
	sample_size = args.size
	main(TRAIN_DATA_PATH, SAVE_DATA_PATH, sample_size)