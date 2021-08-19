

#the array or the xo

"""
	[[00,01,02],
	 [10,11,12],
	 [20,21,22]]
"""
def p_r_box(box):
	"""Prints the xo box when called"""
	print(f"{box[0]}\n{box[1]}\n{box[2]}\n")

def lispi(a):
	"""for splitting user input"""
	a = int(a)
	a_1 = (a)//10
	a_2 = (a)%10
	return a_1,a_2

	
def checkbox(xo_fill):
	a,b,c = '00' in xo_fill,'01' in xo_fill,'02' in xo_fill
	d,e,f = '10' in xo_fill,'11' in xo_fill,'12' in xo_fill
	g,h,i = '20' in xo_fill,'21' in xo_fill,'22' in xo_fill
	#diagonal_check
	if (a and e and i) or (c and e and g):
		return True
	#horizontal_check
	elif (a and b and c) or (d and e and f) or (g and h and i):
		return True
	#vertical_check
	elif (a and d and g) or (b and e and h) or (c and f and i):
		return True
	else:
		return False
		

#game_program


xo_fill = []
flag = True
while flag:

	player_1 = input("Player 1 [X] Name: ")
	player_2 = input("Player 2 [O] Name: ")

	play_1_score = 0
	play_2_score = 0
 
	gbox = [
			[' ',' ',' '],
			[' ',' ',' '],
			[' ',' ',' ']
			]

	while True:		
		p_r_box(gbox)
		print("-"*20+f"[Score :: {player_1}-{play_1_score} : {player_2}-{play_2_score}]")
		while len(xo_fill)<9:
#X's	
			play_1 = input("X's positional input: ")		
			xo_fill.append(play_1)
			a_1,a_2 = lispi(play_1)
			ob = 'x'
			gbox[a_1][a_2] = ob
			p_r_box(gbox)
	
			if checkbox(xo_fill[::2]):
				print("X is Winner")
				play_1_score += 1
				break
	
			
#O's	
			play_2 = input("O's positional input: ")
			xo_fill.append(play_2)
			a_1,a_2 = lispi(play_2)
			ob = 'o'
			gbox[a_1][a_2] = ob
			p_r_box(gbox)

			if checkbox(xo_fill[1::2]):
				print("O is Winner")
				play_2_score += 1
				break
	
#----
		p_ = int(input("\nWant to continue?\n1.Continue\n2.New game\n3.Quit\n(select number):"))
		if p_ == 1:
			continue 
		elif p_ == 2:
			break
		else:
			flag = False
			break
			
	

