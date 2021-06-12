import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock

import logic


class new_game(App):
	def build(self):
		return gameConsole()

class gameConsole(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.pop = Popup(title = 'TickTac',content = Label(text = 'Nothing'))
		self.bot_score = 0
		self.player_score = 0
		self.player_symbol = 'X'
		self.bot_symbol = '0'
		self.cols = 3
		self.buts = []
		self.screenshot = [' ']*9
		for i in range(9):
			self.buts.append(Button(text = ' ',font_size = 40))
			self.buts[i].bind(on_press = self.playerChance)
			self.add_widget(self.buts[i])

		self.score_left = Label(text =f'Player: {self.player_score}',font_size = 30)
		self.add_widget(self.score_left)
		self.resetBtn = Button(text = 'Reset',font_size = 30,
					size_hint = (1,0.3), 
					background_color = (48/255,84/255,150/255,1),
					background_normal = '')
		self.resetBtn.bind(on_press = self.resetGame)
		self.add_widget(self.resetBtn)
		self.score_right = Label(text = f'Bot: {self.bot_score}',font_size = 30)
		self.add_widget(self.score_right)
	def botChance(self):
		i = logic.randomDecision(self.screenshot,self.player_symbol,self.bot_symbol)
		if i==-1:
			self.gameOver()
		else: 
			self.buts[i].text = self.bot_symbol
			self.buts[i].disabled = True
			self.screenshot[i] = self.bot_symbol
			Clock.schedule_once(self.checkStatus,0.5)
	def playerChance(self,instance):
		instance.text = self.player_symbol
		print(self.buts.index(instance))
		self.screenshot[self.buts.index(instance)]=self.player_symbol
		instance.disabled = True
		Clock.schedule_once(self.checkStatus,0.5)
		self.botChance()
	def checkStatus(self,stat =None):
		stat = logic.status(self.screenshot,self.player_symbol,self.bot_symbol)
		if stat == 'WIN':
			self.player_score += 1
			self.gameOver('Congratzz.. You Won')
		elif stat == 'LOST':
			self.bot_score +=1
			self.gameOver('Sorry.. You Loose')
		elif stat == 'OVER':
			self.gameOver()
		else:
			pass

	def resetGame(self, instance):
		for but in self.buts:
			but.text = ' '
			but.disabled = False
		self.score_left.text =f'Player : {self.player_score}'
		self.score_right.text = f'Bot : {self.bot_score}'
		self.screenshot = [' ']*9

	def gameOver(self,pop_text = ' '):
		pop_text = 'Game Over'+pop_text
		self.pop.content = Label(text = pop_text)
		self.pop.size_hint = (1*0.5,1*0.5)
		self.pop.open()
		print('pop open',pop_text)
		Clock.schedule_once(self.pop.dismiss,2)
		self.resetGame(None)

if __name__ == '__main__':
	new_game().run()

