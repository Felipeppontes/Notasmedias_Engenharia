#Código voltado para auxiliar na organização das notas do meu 1º periodo na faculdade de engenharia
import os

while True:
  print("__MEDIA PONDERADA DO 1º PERIODO - ABI (UFPE)__\n")
   
  print("__SUAS NOTAS EM CALCULO DIFERENCIAL E INTEGRAL 1__\n")
  
  #Entrada dos dados. Dividi a entrada de dados em 5 partes, uma parte para cada disciplina
  c1 = float(input("digite a nota da 1ª unidade de calculo 1:"))
  c2 = float(input("digite a nota da 2ª unidade de caluculo 1:"))
  c3 = float(input("digite a nota da 3ª unidade de calculo 1:"))
  #variaveis: media estão presente em cada subdivisão
  media_c1 =  (c1+c2+c3)/3
   
  print("\n___SUAS NOTAS EM GEOMETRIA ANALÍTICA___")
  ga1 = float(input("\ndigite a nota da 1ª unidade de Geometria Analítica:"))
  ga2= float(input("digite a nota da 2ª unidade de Geometria analítica:"))
  ga3= float(input("digite a nota da 3ª unidade de Geometria Analitica:"))
  media_ga1 =  (ga1+ga2+ga3)/3
   
  print("\n___SUAS NOTAS EM FÍSICA 1___\n")
  f1 = float(input("digite a nota da 1ª unidade de física 1:"))
  f2= float(input("digite a nota da 2ª unidade de física 1:"))
  f3= float(input("digite a nota da 3ª unidade de física 1:"))
  media_f1 =  (f1+f2+f3)/3
   
  print("\n___SUAS NOTAS EM GEOMETRIA GRÁFICA TRIDIMENSIONAL___")
  ggt1 = float(input("\ndigite a nota da 1ª unidade de GGT:"))
  ggt2= float(input("digite a nota da 2ª unidade de GGT:"))
  ggt3 = float(input("digite a nota da 3ª unidade de GGT:"))
  media_ggt =  (ggt1+ggt2+ggt3)/3
   
  print("\n___SUAS NOTAS EM INTRODUÇÃO A ENGENHARIA___")
  i1 = float(input("\ndigite a nota da 1ª unidade de Introdução  a engenharia:"))
  i2= float(input("digite a nota da 2ª unidade de Introdução  a engenharia:"))
  i3= float(input("digite a nota da 3ª unidade de Introdução  a engenharia:"))
  media_ie =  (i1+i2+i3)/3
  
  #saida das medias individuais.
  # O uso da interpolação foi para garantir que as notas tenha apenas 2 casas decimais.
  
  print("\n__ESSAS SÃO SUAS MEDIAS__")
  print("\nA media em calculo 1---> %2.2F "%media_c1)
  print("A media em Geometria Analítica---> %2.2F"% media_ga1)
  print("A media em Física 1---> %2.2F"%media_f1)
  print("A media em GGT---> %2.2F"%media_ggt)
  print("A media em introd. a engenharia--->%2.2F"%media_ie)
  
  #Realização da media das medias com os respectivos pesos de acordo com a UFPE
  media_CR = (media_c1*4+media_ga1*4+media_f1*4+media_ggt*3+media_ie*4)/19
  print("\n*******ESSE É SEU COEFICIENTE DE RENDIMENTO:******\n")
  if media_CR > 10: 
    print("\nHá algum número errado!!!!")
  else:
    print("----------%2.2F " %media_CR,"----------")
  
  #Uso do operador condicional para me informa a possibilidade de passar no curso que quero ou não.
  
  if media_CR >=7:
      print("\n""**********Você tem grandes chances de conseguir passar em qualquer engenharia no ABI!********""\n")
  if media_CR <7 and media_CR >=3:
      print("\n""**********Tem grandes chaces de passar em 70% das engenharias********""\n")
  if media_CR <3:
      print("\n""******Dificilmente você passará em uma engenharia concorrida******""\n")


#USO DO WHLIE E IMPORT.OS PARA REPETIR O PROGRAMA TODAS VEZES QUE QUISER
  print("\n\n-->!!!Fim Do Programa!!!")
  input("\nAperte ENTER para testar novamente! ")
  os.system("clear")
  


    