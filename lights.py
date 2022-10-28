
#In a string we describe a road. There are cars that move to the right and we denote them with ">" and cars that move to the left and we denote them with "<". There are also cameras that are indicated by: ".".
#A camera takes a photo of a car if it moves to the direction of the camera.
#Task
#Your task is to write a function such that, for the input string that represents a road as described, returns the total number of photos that were taken by the cameras. The complexity should be strictly O(N) in order to pass all the tests.
#Examples
#For ">>." - 2 photos were taken
#For ".>>" - 0 photos were taken
#For ">.<." - 3 photos were taken
#For ".><.>>.<<" - 11 photos were taken



def count_photos(road):
	# count all of the instances of cameras. As we see a right facing car, that's how many cameras it will pass!
	cams = road.count(".")
    
	# count the number of cams we have seen as we iterate. this is the number of photos for left facing cars!
    
	seen = 0
	# counter for photos
	total = 0
	# loop over characters
	for char in road:
		# if we have a ".", any upcoming "<" will pass it (add to seen)
		# any upcoming ">" will not pass it (remove from cams)
		if char == ".":
			seen += 1
			cams -= 1
		# left facing car will pass all instances of "."
		elif char == "<":
			total += seen
		# right facing will pass any remaining cams that we have yet to see
		else:
			total += cams
	return total
		
print(count_photos(">>."))





index = [1,2,3,4]

print(index[:6:])





