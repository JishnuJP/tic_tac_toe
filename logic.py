def randomDecision(screenshot,player_symbol,bot_symbol):
	for i in range(len(screenshot)):
		if screenshot[i] ==' ':
			return i
		else:
			continue
	return -1 # Game Over
def status(screenshot, symbol, enemy):
	winners = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	ind =[i for i,x in enumerate(screenshot) if x== symbol]
	if ind in winners:
		return 'WIN'
	ind = [i for i, x in enumerate(screenshot) if x==enemy]
	if ind in winners:
		return 'LOST'
	elif ' '  not in screenshot:
		return 'OVER'
	else:
		return 'NO'

