import svgwrite as svg
import xml
import sys
import os

def get_images(path):
	lst = []

	for image in os.listdir(path):
		if ".xml" in image:
			lst.append(int(image.split('.')[0]))
	
	lst.sort()
	lst = [str(i)+".xml" for i in lst]
	a = []
	os.chdir(path)
	for i in lst:
		a.append(xml.etree.ElementTree.parse(i).getroot())
		
	return a
	
#appends b to the right of a
def horizontal_append(root,root2):
	width = 0
	for poly in root[0]:
		for point in poly.find('Points'):
			x = int(point.find('X').text)
			if x > width:
				width = x

	for poly in root2[0]:
		for point in poly.find('Points'):
			point.find('X').text  = str(int(point.find('X').text) +width)
		root[0].append(poly)
	
#appends b below a	
def vertical_append(root,root2):
	height= 0
	for poly in root[0]:
		for point in poly.find('Points'):
			y = int(point.find('Y').text)
			if y > height:
				height = y
	
	for poly in root2[0]:
		for point in poly.find('Points'):
			point.find('Y').text  = str(int(point.find('Y').text) +height)
		root[0].append(poly)

def combine(lst,width):
	lst= [lst[i:i+width] for i in range(0, len(lst), width)]
	strips = []
	for row in lst:
		head = row[0]
		for i in row:
			if i is not head:
				horizontal_append(head,i)
		
		strips.append(head)
	
	result = strips[0] 
	for strip in strips:
		if strip is not result:
			vertical_append(result,strip)
	
	return result

def stitch(directory, width, output):
	orgdir = os.getcwd()
	res = xml.etree.ElementTree.ElementTree()
	files = get_images(directory)
	res._setroot(	combine(files ,width))
	os.chdir(orgdir)	
	res.write(output)
	
if __name__ == "__main__":
	if (len(sys.argv) != 4):
		print("stitches together a directory of DNA xml files to a single xml file.")
		print("please name images numerically\n")
		print("usage: python stitch.py <directory> <output.xml> <INT num_images_in_row>")
	else:
		direc = sys.argv[1]
		output = sys.argv[2]
		width = int(sys.argv[3])
		stitch(direc,width,output)
