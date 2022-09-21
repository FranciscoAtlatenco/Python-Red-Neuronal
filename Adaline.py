import numpy as np
import matplotlib.pyplot as plt

def entrenarHardlims ():
    #hardlims Adaline
    #los valores de P
   p1x = int(input("ingrese p1x:"))
   p1y = int(input("ingrese p1y:"))
   print ("los valores de p1 son", "[", p1x, "]" , "[", p1y, "]")
   
   print (" ____________________________________________")
   p2x = int(input("ingrese p2x:"))
   p2y = int(input("ingrese p2y:"))
   print ("los valores de p1 son", "[", p2x, "]" , "[", p2y, "]")
   
   print (" ____________________________________________")
   p3x = int(input("ingrese p3x:"))
   p3y = int(input("ingrese p3y:"))
   print ("los valores de p1 son", "[", p3x, "]" , "[", p3y, "]")

   print (" ____________________________________________")
   p4x = int(input("ingrese p4x:"))
   p4y = int(input("ingrese p4y:"))
   print ("los valores de p1 son", "[", p4x, "]" , "[", p4y, "]")
   print (" ____________________________________________")
   
   #son los valores de T
   t1 = int(input("ingrese t1:"))
   t2 = int(input("ingrese t2:"))
   t3 = int(input("ingrese t3:"))
   t4 = int(input("ingrese t4:"))
   print ("los valores de t son:", "[", t1 ,"]", "[", t2 ,"]", "[", t3 ,"]", "[", t4 ,"]")
   
   peso1 = float(input("ingrese peso (W1):"))
   peso2 = float(input("ingrese peso (W2):"))
   #hace transpuesta de la matriz inicial
   w = np.transpose(np.array([peso1, peso2]))
   
   #Es el valor de la ganancia de b
   b = float(input("valor de (b):" ))
   alfa = float(input("Ingrese factor de paredizaje (α) : "))
   
   a = 0
   errores_totales = 0
   
   #determina numero de iteraciones
   while errores_totales != 4:
       
       #Declara patrones
       M = [p1x, p2x, p3x, p4x], [p1y, p2y, p3y, p4y]
   
       #Declara T de los patrones 
       A = [t1, t2, t3, t4]
       r = 0
       
       errores_totales = 0
       print("___________")
       print ("Numero de Interacion----->", [a+1])
       a += 1
       errores = []
       
       for i in A:
           P = [fila[r] for fila in M]
          
           print("se encuentra en el patron", P)
           print("___________")
           array = (w * np.transpose(np.array(P)))
           
           #operacion de a1 w * p + b
           a1 = (array[0] + array[1] + b)
           
           #condicion de hardlims
           if(a1 >= 0):
               a1 = 1
           else:
               a1 = -1
           
           #calcula el error
           e1 = (i - a1)
           errores.append(e1)
           
           #condicion del error para modificar peso W
           if(e1 != 0):
               w = (w + ((2) * (alfa) * e1 * np.transpose(np.array(P))))
               #Ajusta b
               b = (b + ((2) * (alfa) * e1))
            
               print("se modifico el peso ")
               print("valor modificado W ", w)
               print("nuevo valor de b ", b )
               r += 1
               
           else:
         
               print("el peso no se modifico")
               print("valor modificado W ", w)
               print("nuevo valor de b ", b )
               r += 1
               errores_totales += 1
               
       print("numeros con error: ")
       for n in errores:
           print(n)
           
   #Separcion lineal 
   else:
      x1 = (-b / array[0])
      print("el valor de x es: ", x1)
      y1 = (-b / array[0])
      print("el valor de y es: ", y1)
      #Para la grafica 
      x = [p1x, p2x, p3x, p4x]
      y = [p1y, p2y, p3y, p4y]
      plt.plot([x1,0], [y1,0] , linewidth=2)
      plt.scatter(x,y)
      plt.show()
      
       
       
def entrenarHardlim ():
    #hardlims Adaline
    #los valores de P
    p1x = int(input("ingrese p1x:"))
    p1y = int(input("ingrese p1y:"))
    print ("los valores de p1 son", "[", p1x, "]" , "[", p1y, "]")
    
    print (" ____________________________________________")
    p2x = int(input("ingrese p2x:"))
    p2y = int(input("ingrese p2y:"))
    print ("los valores de p1 son", "[", p2x, "]" , "[", p2y, "]")
    
    print (" ____________________________________________")
    p3x = int(input("ingrese p3x:"))
    p3y = int(input("ingrese p3y:"))
    print ("los valores de p1 son", "[", p3x, "]" , "[", p3y, "]")

    print (" ____________________________________________")
    p4x = int(input("ingrese p4x:"))
    p4y = int(input("ingrese p4y:"))
    print ("los valores de p1 son", "[", p4x, "]" , "[", p4y, "]")
    print (" ____________________________________________")
    
    #son los valores de T
    t1 = int(input("ingrese t1:"))
    t2 = int(input("ingrese t2:"))
    t3 = int(input("ingrese t3:"))
    t4 = int(input("ingrese t4:"))
    print ("los valores de t son:", "[", t1 ,"]", "[", t2 ,"]", "[", t3 ,"]", "[", t4 ,"]")
    
    peso1 = float(input("ingrese peso (W1):"))
    peso2 = float(input("ingrese peso (W2):"))
    #hace transpuesta de la matriz inicial
    w = np.transpose(np.array([peso1, peso2]))
    
    #Es el valor de la ganancia de b
    b = float(input("valor de (b):" ))
    alfa = float(input("Ingrese factor de aprendizaje (α) : "))
    
    a = 0
    errores_totales = 0
    
    #determina numero de iteraciones
    while errores_totales != 4:
        
        #Declara patrones
        M = [p1x, p2x, p3x, p4x], [p1y, p2y, p3y, p4y]
    
        #Declara T de los patrones 
        A = [t1, t2, t3, t4]
        r = 0
        
        errores_totales = 0
        print("___________")
        print ("Numero de Interacion----->", [a+1])
        a += 1
        errores = []
        
        for i in A:
            P = [fila[r] for fila in M]
           
            print("se encuentra en el patron", P)
            print("___________")
            array = (w * np.transpose(np.array(P)))
            
            #operacion de a1 w * p + b
            a1 = (array[0] + array[1] + b)
            
            #condicion de hardlims
            if(a1 >= 0):
                a1 = 1
            else:
                a1 = 0
            
            #calcula el error
            e1 = (i - a1)
            errores.append(e1)
            
            #condicion del error para modificar peso W
            if(e1 != 0):
                w = (w + ((2) * (alfa) * e1 * np.transpose(np.array(P))))
                #Ajusta b
                b = (b + ((2) * (alfa) * e1))
             
                print("se modifico el peso ")
                print("valor modificado W ", w)
                print("nuevo valor de b ", b )
                r += 1
                
            else:
          
                print("el peso no se modifico")
                print("valor modificado W ", w)
                print("nuevo valor de b ", b )
                r += 1
                errores_totales += 1
                
        print("numeros con error: ")
        for n in errores:
            print(n)
            
    #Separcion lineal 
    else:
       x1 = (-b / array[0])
       print("el valor de x es: ", x1)
       y1 = (-b / array[0])
       print("el valor de y es: ", y1)
       #Para la grafica 
       x = [p1x, p2x, p3x, p4x]
       y = [p1y, p2y, p3y, p4y]
       plt.plot([x1,0], [y1,0] , linewidth=2)
       plt.scatter(x,y)
       plt.show()
       
       


#Main Principal
opcion = int(input("elije la opcion;  [1.Hardlims]____[2.Hardlim]---escribala opcion = "))   
if (opcion == 1):
    entrenarHardlims()
elif (opcion == 2):
    entrenarHardlim()

                
                
            
            
            
            
        
        
    
    