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
      
     


            
            