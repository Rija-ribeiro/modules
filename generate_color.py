def generate(color_num,number_of_color,lum=255):
 color = [0,0,0]
 for i in range(int(3*255*color_num/number_of_color)+lum):
  if i>int(3*255*color_num/number_of_color):
   color[int(i/255)%3] += 1
 return color
