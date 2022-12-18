import pygame
import time
pygame.init()
'''создаём окно программы'''
back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
'''закрашиваем окно цветом (200, 255, 255)'''
mw.fill(back)
'''Создаем объект таймера; в дальнейшем внутри цикла установим для него количество кадров в секунду'''
clock = pygame.time.Clock()
'''класс прямоугольник'''
'''Данный класс(Area()) состоит из конструктора (метод __init__, который запускается автоматически при создании объекта данного класса)'''
'''Остальные методы (color(), fill(), outline(), collidepoint()) надо вызывать для определенного объекта, при необходимости'''
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):   #Кроме самого объекта (self-это ссылка на объект), 
                                                                   # передаем координаты расположения прямоугольника,
                                                                   # а также его ширину и высоту, и цвет
                                                                   # Все прописываем со значением по умолчанию, т.е если мы 
                                                                   # не передадим никакие значения, они будут теми, что по умолчанию
      self.rect = pygame.Rect(x, y, width, height) #объект прямоугольника (rectangle)
      self.fill_color = color

  def color(self, new_color):      #Метод для замены цвета прямоугольника
      self.fill_color = new_color

  def fill(self):                  #Метод fill() Принимает только сам объект. Внутри метода мы рисуем прямоугольник, объект rect
      pygame.draw.rect(mw, self.fill_color, self.rect)   #Передаем название окна, цвет и сам прямоугольник rect

  def outline(self, frame_color, thickness): #обводка существующего прямоугольника
      pygame.draw.rect(mw, frame_color, self.rect, thickness)   #передаем цвет и толщину рамки thickness
 
  def collidepoint(self, x, y):   #Метод проверяет был ли клик по области
      return self.rect.collidepoint(x, y)     
 
'''класс надпись'''
'''класс Label() является наследником класса Area(), по-этому все методы и свойства он от него унаследует'''
'''Иначе говоря Area() - суперкласс для Label()'''

class Label(Area):

  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):  #Метод set_text() устанавливает текст
                                                             #При вызове данного метода, кроме самого объекта
                                                             #нам нужно передать желаемый текст, его размер и цвет
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)   #создаем объект надписи

  def draw(self, shift_x=0, shift_y=0): #Метод drow() рисует на прямоугольнике надпись
      self.fill()  #Рисуем прямоугольник
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) #Рисуем надпись self.image, смещая от x и y

'''Задаем цвета:'''
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)

'''Создаем пустой список, в котором будем хранить все карточки'''
cards = []
num_cards = 4 #Количество карточек
x = 70 #Первая карточка будет начинать отрисовываться по горизонтали слева на mw 70px 
start_time = time.time() #Фиксируем время при запуске
cur_time = start_time #current_time - текущее время
 
''' Интерфейс игры'''
 
time_text = Label(0,0,50,50,back)
time_text.set_text('Время:',40, DARK_BLUE)
time_text.draw(20, 20)
 
timer = Label(50,55,50,40,back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)
 
score_text = Label(380,0,50,50,back)
score_text.set_text('Счёт:',45, DARK_BLUE)
score_text.draw(20,20)
 
score = Label(430,55,50,40,back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)

'''Для создания карточек будем делать цикл, внутри которого каждый раз будем создавать''' 
'''новый объект класса Label()'''
for i in range(num_cards):
  new_card = Label(x, 170, 70, 100, YELLOW) #Создаем объект
  new_card.outline(BLUE, 10) #Делаем обводку
  new_card.set_text('CLICK', 26) #Устанавливает текст Click размером 26
  cards.append(new_card) #В пустой список cards каждый раз добавляем новый объект-карточку
                         #В дальнейшем мы отрисуем каждую из этих карточек
  x = x + 100

wait = 0

points = 0   #Количество очков

from random import randint

while True:
  '''Отрисовка карточек и отображение кликов, чтобы надпись отрисовывалась на одной случайной карточке 0,5 секунды'''
  if wait == 0:
      wait = 20 #столько тиков надпись будет на одном месте
      click = randint(1, num_cards)    # В переменной click будет храниться случайное число в диапазоне от 1 до количества карточек(4)
      for i in range(num_cards):       # Количество итераций в цикле будет равно количеству карточек. 
                                       # i-это как счетчик, так и порядковый номер карточки в списке (начиная с 0) 
          cards[i].color(YELLOW)       # Каждую карточку красим в желтый цвет с помощью метода color(), 
                                       # тем самым стирая ненужные надписи CLICK (должна быть только на одной карточке)
          if (i + 1) == click:         # Т.к. случайное число, которое хранится в переменной click от 1 до 4, а i от 0 до 3
              cards[i].draw(10, 40)    # Отрисовываем прямоугольник вместе с надписью на нужной(случайной) карточке
          else:
              cards[i].fill()          # Рисуем прямоугольник без надписи
  else:
      wait -= 1

  ''' Для чего нужен wait в цикле while? wait = 0, if wait == 0? Если убрать условный оператор if wait == 0, то все будет происходить очень быстро'''
  ''' т.к. частота у нас 40 кадров в секунду(clock.tick(40)), соответственно CLICK за одну секунду будет появляться в 40 позициях. Для удержания надписи'''
  ''' 0,5 секунды на карточке вводим переменную wait. В условном операторе задаем ей значение 20 и на каждый тик уменьшаем значение на 1, сравнивая с 0'''
  ''' Таким образом 20 тиков из 40 в секунду надпись будет оставаться на одной карточке '''
  '''Обработка кликов по карточкам'''
  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #Если нажали на левую кнопку мыши (2- правая)
          x, y = event.pos
          for i in range(num_cards):
              #ищем, в какую карту попал клик
              if cards[i].collidepoint(x,y):
                  if i + 1 == click: #если на карте есть надпись перекрашиваем в зелёный, плюс очко
                      cards[i].color(GREEN)
                      points += 1
                  else: #иначе перекрашиваем в красный, минус очко
                      cards[i].color(RED)
                      points -= 1
                  cards[i].fill()
                  score.set_text(str(points),40, DARK_BLUE)
                  score.draw(0,0)
  '''Выигрыш и проигрыш'''
  new_time = time.time()
 
  if new_time - start_time  >= 11:
       win = Label(0, 0, 500, 500, LIGHT_RED)
       win.set_text("Время вышло!!!", 60, DARK_BLUE)
       win.draw(110, 180)
       break
  
  if int(new_time) - int(cur_time) == 1: #проверяем, есть ли разница в 1 секунду между старым и новым временем
       timer.set_text(str(int(new_time - start_time)),40, DARK_BLUE)
       timer.draw(0,0)
       cur_time = new_time
 
  if points >= 5:
       win = Label(0, 0, 500, 500, LIGHT_GREEN)
       win.set_text("Ты победил!!!", 60, DARK_BLUE)
       win.draw(140, 180)
       resul_time = Label(90, 230, 250, 250, LIGHT_GREEN)
       resul_time.set_text("Время прохождения: " + str (int(new_time - start_time)) + " сек", 40, DARK_BLUE)
 
       resul_time.draw(0, 0)
 
       break
 
  pygame.display.update()
  clock.tick(40)
 
pygame.display.update() 