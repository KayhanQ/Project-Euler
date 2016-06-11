import numpy

width = 32
height = 10

# draws a wall in ascii
def drawWall(wall):
	for i in xrange(len(wall)):
		print '|',
		for j in xrange(len(wall[i])):
			for x in xrange(wall[i][j]):
				print "_",
			print '|',
		print ""

# returns array of arrays with permutations of row configurations
def getPerms(row, perms):
	cur_width = sum(row)

	if cur_width == width:
		perms.append(row)
	elif cur_width < width:
		getPerms(row + [2], perms)
		getPerms(row + [3], perms)

# NOTUSED
# creates all possible walls
def createWalls(wall, allWalls, perms):
	cur_height = len(wall)
	if cur_height < height:
		for i in xrange(0, len(perms)):
			createWalls(wall + [perms[i]], allWalls, perms);
	elif cur_height == height:
		allWalls.append(wall)

# NOTUSED
# checks if a whole wall has a crack
def hasCrack(wall):
	for i in xrange(0, len(wall)-1):
		high_cur_width = 0
		for j in xrange(0, len(wall[i])-1):
			high_cur_width = high_cur_width + wall[i][j]
			low_cur_width = 0
			for k in xrange(0, len(wall[i+1])):
				low_cur_width = low_cur_width + wall[i+1][k]
				if high_cur_width == low_cur_width:
					return True
				elif low_cur_width > high_cur_width:
					continue
	return False

# NOTUSED
def numWellFormedWalls(allWalls):
	cnt = 0
	for i in xrange(0, len(allWalls)):
		if not hasCrack(allWalls[i]):
			cnt = cnt + 1

	return cnt
		
# checks if two rows have a crack
def rowsHaveCrack(row1, row2):
	high_cur_width = 0
	for j in xrange(0, len(row1)-1):
		high_cur_width = high_cur_width + row1[j]
		low_cur_width = 0
		for k in xrange(0, len(row2)):
			low_cur_width = low_cur_width + row2[k]
			if high_cur_width == low_cur_width:
				return True
			elif low_cur_width > high_cur_width:
				continue
	return False

# generates matrix of crack relations between rows
def getCrackMatrix(perms):
	numPerms = len(perms)
	crackMatrix = numpy.zeros((numPerms, numPerms))

	for i in xrange(0,numPerms):
		for j in xrange(i,numPerms):
			if rowsHaveCrack(perms[i], perms[j]):
				crackMatrix[i,j] = 1
				crackMatrix[j,i] = 1

	return crackMatrix

# make all the walls that are well formed
def createWellFormedWalls(wall, allWalls, crackMatrix):
	cur_height = len(wall)
	if cur_height < height:
		for i in xrange(0, len(perms)):
			
			if cur_height > 0:
				curRow = wall[-1]
				if crackMatrix[curRow, i] == 0:
					createWalls(wall + [i], allWalls, perms)
			else:
				createWalls(wall + [i], allWalls, perms)
	elif cur_height == height:
		allWalls.append(wall)


row = []
perms = []
getPerms(row, perms)
print 'perms created'

crackMatrix = getCrackMatrix(perms)
print 'crack matrix created'
print crackMatrix


# too slow to generate all good walls
# wall = []
# allWalls = []
# createWellFormedWalls(wall, allWalls, crackMatrix)

# print 'well formed walls created'

# print allWalls
# print 'Answer: ', len(allWalls)





