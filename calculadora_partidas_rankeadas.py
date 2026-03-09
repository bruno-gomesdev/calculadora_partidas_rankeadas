class partidas_rankeadas:
    def calculadora(self, vitorias, derrotas):
        self.vitorias = vitorias
        self.derrotas = derrotas
        saldo_vitorias =  vitorias - derrotas
    
        if saldo_vitorias < 10:
            nivel = "Ferro" 
        elif saldo_vitorias > 10 and saldo_vitorias <= 20:
            nivel = "Bronze"
        elif saldo_vitorias > 20 and saldo_vitorias <= 50:
            nivel = "Prata"
        elif saldo_vitorias > 50 and saldo_vitorias <= 80:
            nivel = "Ouro"
        elif saldo_vitorias > 80 and saldo_vitorias <= 90:
            nivel = "Diamante"
        elif saldo_vitorias > 90 and saldo_vitorias <= 100:
            nivel = "Lendário"
        else:
            nivel = "Imortal"

        print(f"O Herói tem saldo de {saldo_vitorias} está no nível de {nivel}")

rank_heroi = partidas_rankeadas()
rank_heroi.calculadora(50, 30)
