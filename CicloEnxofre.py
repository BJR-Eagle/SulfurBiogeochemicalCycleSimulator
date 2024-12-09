import tkinter as tk
from tkinter import StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class CicloEnxofre:
    def __init__(self, emissao_enxofre=10, precipitacao=5, absorcao_biosfera=3, sedimentacao_oceanos=2,
                 mineralizacao=2, oxigenacao_sulfetos=2, emissao_compostos_nao_sulfuricos=1, decomposicao_biosfera=2,
                 absorcao_oceanos=1, emissao_oceanos=1, erosoes_solo=2):
        # Definindo as variáveis iniciais do ciclo
        self.emissao_enxofre = emissao_enxofre
        self.precipitacao = precipitacao
        self.absorcao_biosfera = absorcao_biosfera
        self.sedimentacao_oceanos = sedimentacao_oceanos
        self.mineralizacao = mineralizacao
        self.oxigenacao_sulfetos = oxigenacao_sulfetos
        self.emissao_compostos_nao_sulfuricos = emissao_compostos_nao_sulfuricos
        self.decomposicao_biosfera = decomposicao_biosfera
        self.absorcao_oceanos = absorcao_oceanos
        self.emissao_oceanos = emissao_oceanos
        self.erosoes_solo = erosoes_solo
        
        # Compartimentos de enxofre em cada parte do ciclo
        self.atmosfera = 100
        self.hidrosfera = 100
        self.litosfera = 100
        self.biosfera = 100
    
    def passo(self):
        # Simulando o fluxo de enxofre entre os compartimentos
        
        # Emissão de enxofre para a atmosfera
        self.atmosfera += self.emissao_enxofre
        
        # Precipitação que remove enxofre da atmosfera e o envia para a hidrosfera
        self.atmosfera -= self.precipitacao
        self.hidrosfera += self.precipitacao
        
        # Processos na hidrosfera
        self.hidrosfera -= self.sedimentacao_oceanos
        self.litosfera += self.sedimentacao_oceanos
        
        # Processos na biosfera
        self.biosfera += self.absorcao_biosfera
        self.hidrosfera -= self.absorcao_biosfera
        
        # Erosão e mineralização
        self.litosfera -= self.erosoes_solo
        self.hidrosfera += self.mineralizacao
        
        # Oxidação e outros processos
        self.hidrosfera -= self.oxigenacao_sulfetos
        self.atmosfera += self.emissao_compostos_nao_sulfuricos
        
        # Decomposição e absorção pelos oceanos
        self.hidrosfera += self.decomposicao_biosfera
        self.biosfera -= self.decomposicao_biosfera
        self.hidrosfera += self.absorcao_oceanos
        self.atmosfera -= self.emissao_oceanos
    
    def simular(self, passos=50):
        atmosfera_hist = []
        hidrosfera_hist = []
        litosfera_hist = []
        biosfera_hist = []
        
        for _ in range(passos):
            self.passo()
            atmosfera_hist.append(self.atmosfera)
            hidrosfera_hist.append(self.hidrosfera)
            litosfera_hist.append(self.litosfera)
            biosfera_hist.append(self.biosfera)
        
        return atmosfera_hist, hidrosfera_hist, litosfera_hist, biosfera_hist

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador do Ciclo Biogeoquímico do Enxofre")
        
        # Frame para controle das variáveis
        self.frame_controle = tk.Frame(self.root)
        self.frame_controle.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título do simulador
        tk.Label(self.frame_controle, text="Simulador do Ciclo Biogeoquímico do Enxofre", font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Variáveis e entradas
        self.emissao_var = tk.IntVar(value=10)
        self.precipitacao_var = tk.IntVar(value=5)
        self.absorcao_var = tk.IntVar(value=3)
        self.sedimentacao_var = tk.IntVar(value=2)
        self.mineralizacao_var = tk.IntVar(value=2)
        self.oxigenacao_var = tk.IntVar(value=2)
        self.emissao_compostos_var = tk.IntVar(value=1)
        self.decomposicao_var = tk.IntVar(value=2)
        self.absorcao_oceanos_var = tk.IntVar(value=1)
        self.emissao_oceanos_var = tk.IntVar(value=1)
        self.erosoes_var = tk.IntVar(value=2)
        
        # Entradas
        tk.Label(self.frame_controle, text="Emissão de Enxofre:").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.emissao_var).grid(row=1, column=1)
        
        tk.Label(self.frame_controle, text="Precipitação:").grid(row=2, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.precipitacao_var).grid(row=2, column=1)
        
        tk.Label(self.frame_controle, text="Absorção pela Biosfera:").grid(row=3, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.absorcao_var).grid(row=3, column=1)
        
        tk.Label(self.frame_controle, text="Sedimentação Oceanos:").grid(row=4, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.sedimentacao_var).grid(row=4, column=1)
        
        tk.Label(self.frame_controle, text="Mineralização:").grid(row=5, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.mineralizacao_var).grid(row=5, column=1)
        
        tk.Label(self.frame_controle, text="Oxidação de Sulfetos:").grid(row=6, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.oxigenacao_var).grid(row=6, column=1)
        
        tk.Label(self.frame_controle, text="Emissão Compostos Não Sulfúricos:").grid(row=7, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.emissao_compostos_var).grid(row=7, column=1)
        
        tk.Label(self.frame_controle, text="Decomposição Biosfera:").grid(row=8, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.decomposicao_var).grid(row=8, column=1)
        
        tk.Label(self.frame_controle, text="Absorção pelos Oceanos:").grid(row=9, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.absorcao_oceanos_var).grid(row=9, column=1)
        
        tk.Label(self.frame_controle, text="Emissão pelos Oceanos:").grid(row=10, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.emissao_oceanos_var).grid(row=10, column=1)
        
        tk.Label(self.frame_controle, text="Erosão do Solo:").grid(row=11, column=0, sticky=tk.W)
        tk.Entry(self.frame_controle, textvariable=self.erosoes_var).grid(row=11, column=1)
        
        tk.Button(self.frame_controle, text="Iniciar Simulação", command=self.iniciar_simulacao).grid(row=12, column=0, columnspan=2, pady=10)
        
        # Adiciona Labels para resultados
        self.resultados_label = tk.Label(self.frame_controle, text="", font=('Arial', 12))
        self.resultados_label.grid(row=13, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        # Frame para os cenários predefinidos
        self.frame_cenarios = tk.Frame(self.root)
        self.frame_cenarios.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título dos cenários predefinidos
        tk.Label(self.frame_cenarios, text="Cenários Predefinidos", font=('Arial', 14, 'bold')).pack(pady=10)
        
        tk.Button(self.frame_cenarios, text="Cenário 1: Emissão Alta", command=self.cenario_1).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 2: Precipitação Alta", command=self.cenario_2).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 3: Absorção Alta", command=self.cenario_3).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 4: Sedimentação Alta", command=self.cenario_4).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 5: Erosão Alta", command=self.cenario_5).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 6: Mineralização Alta", command=self.cenario_6).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 7: Oxidação Alta", command=self.cenario_7).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 8: Decomposição Alta", command=self.cenario_8).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 9: Emissão Oceanos Alta", command=self.cenario_9).pack(fill=tk.X, pady=5)
        tk.Button(self.frame_cenarios, text="Cenário 10: Absorção Oceanos Alta", command=self.cenario_10).pack(fill=tk.X, pady=5)
        
        # Gráfico
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def iniciar_simulacao(self):
        emissao = self.emissao_var.get()
        precipitacao = self.precipitacao_var.get()
        absorcao = self.absorcao_var.get()
        sedimentacao = self.sedimentacao_var.get()
        mineralizacao = self.mineralizacao_var.get()
        oxigenacao = self.oxigenacao_var.get()
        emissao_compostos = self.emissao_compostos_var.get()
        decomposicao = self.decomposicao_var.get()
        absorcao_oceanos = self.absorcao_oceanos_var.get()
        emissao_oceanos = self.emissao_oceanos_var.get()
        erosoes = self.erosoes_var.get()

        ciclo = CicloEnxofre(
            emissao_enxofre=emissao,
            precipitacao=precipitacao,
            absorcao_biosfera=absorcao,
            sedimentacao_oceanos=sedimentacao,
            mineralizacao=mineralizacao,
            oxigenacao_sulfetos=oxigenacao,
            emissao_compostos_nao_sulfuricos=emissao_compostos,
            decomposicao_biosfera=decomposicao,
            absorcao_oceanos=absorcao_oceanos,
            emissao_oceanos=emissao_oceanos,
            erosoes_solo=erosoes
        )
        
        atmosfera_hist, hidrosfera_hist, litosfera_hist, biosfera_hist = ciclo.simular()

        self.ax.clear()
        self.ax.plot(atmosfera_hist, label="Atmosfera")
        self.ax.plot(hidrosfera_hist, label="Hidrosfera")
        self.ax.plot(litosfera_hist, label="Litosfera")
        self.ax.plot(biosfera_hist, label="Biosfera")
        self.ax.set_xlabel("Periodos")
        self.ax.set_ylabel("Quantidade de Enxofre")
        self.ax.set_title("Grafico dos Niveis de Enxofre")
        self.ax.legend()
        self.canvas.draw()

        # Atualiza resultados
        resultados_texto = (f"Litosfera: {ciclo.litosfera:.2f}\n"
                            f"Hidrosfera: {ciclo.hidrosfera:.2f}\n"
                            f"Biosfera: {ciclo.biosfera:.2f}\n"
                            f"Atmosfera: {ciclo.atmosfera:.2f}")
        self.resultados_label.config(text=resultados_texto)

    def cenario_1(self):
        self.emissao_var.set(15)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(5)
        self.iniciar_simulacao()

    def cenario_2(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(10)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

    def cenario_3(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(5)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

    def cenario_4(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(5)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

    def cenario_5(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(5)
        self.iniciar_simulacao()

    def cenario_6(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(5)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

    def cenario_7(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(5)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

    def cenario_8(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(5)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

    def cenario_9(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(1)
        self.emissao_oceanos_var.set(5)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

    def cenario_10(self):
        self.emissao_var.set(10)
        self.precipitacao_var.set(5)
        self.absorcao_var.set(3)
        self.sedimentacao_var.set(2)
        self.mineralizacao_var.set(2)
        self.oxigenacao_var.set(2)
        self.emissao_compostos_var.set(1)
        self.decomposicao_var.set(2)
        self.absorcao_oceanos_var.set(5)
        self.emissao_oceanos_var.set(1)
        self.erosoes_var.set(2)
        self.iniciar_simulacao()

# Cria a janela principal e a interface
root = tk.Tk()
app = App(root)
root.mainloop()
