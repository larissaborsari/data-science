while True: 
    try: 
          perna = input('informe qual a situação de levantamento de pernas do papagaio: ')
          perna = perna.lower()
          
          if perna == "esquerda":
            print("ingles")
          
          elif perna =="direita":
            print("frances")
          
          elif perna == "nenhuma":
            print("portugues")
          
          elif perna == "ambas":
            print("caiu")
      
          else:
            print("Saindo ...")
            break     
        
          
    except EOFError: 
        break