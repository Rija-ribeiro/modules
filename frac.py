import math

class frac():
 def __init__(self,nom,denom):
  nom = int(nom)
  denom = int(denom)
  i = 2
  while i<=math.sqrt(abs(nom))+1:
   if nom/i==int(nom/i) and denom/i==int(denom/i):
    nom = nom/i
    denom = denom/i
   else:
    i += 1
  if denom<0:
   nom *= -1
   denom *= -1

  self.nom = int(nom)
  self.denom = int(denom)

 #### NUMERIC TRANSFORMATION###
 def __str__(self):
  if self.denom != 1:
   return "{}/{}".format(self.nom,self.denom)
  else:
   return str(self.nom)

 def __int__(self):
  return int(self.nom/self.denom)

 def __round__(self):
  return round(self.nom/self.denom)

 def __float__(self):
  return self.nom/self.denom

 def __abs__(self):
  return frac(abs(self.nom),self.denom)

 #### NUMERIC OPERATION #######
 def __add__(self,other):
  if type(other)==int:
   other = frac(other,1)
  nom = self.nom*other.denom+other.nom*self.denom
  denom = self.denom*other.denom
  return frac(nom,denom)
 def __radd__(self,other):
  return self.__add__(other)

 def __sub__(self,other):
  if type(other)==int:
   other = frac(other,1)
  nom = self.nom*other.denom-other.nom*self.denom
  denom = self.denom*other.denom
  return frac(nom,denom)
 def __rsub__(self,other):
  return self.__sub__(other)

 def __mul__(self,other):
  if type(other)==int:
   other = frac(other,1)
  nom = self.nom*other.nom
  denom = self.denom*other.denom
  return frac(nom,denom)
 def __rmul__(self,other):
  return self.__mul__(other)

 def __truediv__(self,other):
  if type(other)==int:
   other = frac(other,1)
  nom = self.nom*other.denom
  denom = self.denom*other.nom
  return frac(nom,denom)
 def __rtruediv__(self,other):
  return self.__pow__(other)

 def __pow__(self,other):
  if type(other)==frac:
   other = other.num/other.denum
  return frac(self.nom**other,self.denom**other)
 def __rpow__(self,other):
  return self.__pow__(other)

 #### TEST CONDITION ##########
 def __eq__(self,other):
  if type(other)==int:
   other = frac(other,1)
  if type(self)==int:
   self = frac(other,1)
  return self.nom==other.nom and self.denom==other.denom

 def __ne__(self,other):
  if type(other)==int:
   other = frac(other,1)
  if type(self)==int:
   self = frac(other,1)
  return self.nom!=other.nom or self.denom!=other.denom

if __name__ == "__main__":
    print(frac(input("e"),input("z"))/frac(input("d"),input("t")))
