class Carro:
      def __init__(self, modelo, ano, fabricante, capacidade=5):
            self.modelo = modelo
            self.ano = ano
            self.fabricante = fabricante
            self.capacidade = capacidade
            
      def criar_carro():
            ...

      def gerando_multa(self, velocidade):
            if velocidade >= 120:
                  print (f"O carro {self.modelo} está andando a {velocidade} km/h e será multado")
            else:
                  print (f"O carro {self.modelo} está andando a {velocidade} km/h, 'sem notificação'")
            return 0
      
      def carro_andando(self, velocidade):
            print(f"Seu {self.modelo} está à {velocidade} km/h")
            return 0
      
      def carro_parado(self):
            if not self.carro_andando:
                  print(f"Seu {self.carro} está parado")
            else:
                  print(f"Seu {self.carro} está a parado")
            return 0
      
     


            
            