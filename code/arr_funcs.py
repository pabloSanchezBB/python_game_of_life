# This Code is for the Array Functions like Checking Neighbors in the GOL Program

# Returns the Number of Living Neighbors around a Cell
def get_neighbors(arr, ind_y, ind_x):
	# Define Edge Cases:
	#	i,j == 0: Top Left Corner
	#	i=0, j=arr.len: Top Right Corner
	#	i=arr.len, j=0: Bottom Left Corner
	#	i=arr.len, j=arr.len: Bottom Right Corner
	if i == 0: # Top Edge 
		if j == 0: # Top Left Corner
			pass
		elif j == len(arr[i])-1: # Top Right Corner
			pass
		else:
			pass
	elif i == len(arr)-1: # Bottom Edge
		if j == 0: # Bottom Left Corner
			pass
		elif j == len(arr[i]) - 1: # Bottom Right Corner
			pass
		else:
			pass
	else: # Not Top Or Bottom Edges
		if j == 0: # Left Edge
			pass
		elif j == len(arr[i]): # Right Edge
			pass
		else:
			pass

			
	