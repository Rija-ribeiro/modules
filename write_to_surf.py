from pygame import font,surface
font.init()

def init(**options):
 global var,tipo
 for i in options:
  var[i] = options[i]
 tipo = font.SysFont(var["tipo"],var["size"])


def get_size(text):
 size = [0,0]
 for i in text:
  if tipo.size(i)[0]>size[0]:
   size[0] = tipo.size(i)[0]
  if tipo.size(i)[1]>size[1]:
   size[1] = tipo.size(i)[1]
 return size

var = {}
var["color"] = (0,0,0)
var["size"] = 12
var["place"] = ("center","center")
var["tipo"] = font.get_default_font()
tipo = font.SysFont(var["tipo"],var["size"])

def write(text,surf):
 text = str(text)
 text = text.split("\n")
 for i in range(len(text)):
  pos = [None,None]
  if var["place"][0]=="left":
   pos[0] = 0
  elif var["place"][0]=="center":
   pos[0] = int((surf.get_size()[0]-tipo.size(text[i])[0])/2)
  elif var["place"][0]=="right":
   pos[0] = surf.get_size()[0]-tipo.size(text[i])[0]

  if var["place"][1]=="up":
   pos[1] = i*tipo.size(text[0])[1]
  elif var["place"][1]=="center":
   pos[1] = int((surf.get_size()[1]-len(text)*tipo.size(text[0])[1])/2+i*tipo.size(text[0])[1])
  elif var["place"][1]=="down":
   pos[1] = surf.get_size()[1]-(i+1)*tipo.size(text[0])[1]
  surf.blit(tipo.render(text[i],True,var["color"]),pos)
