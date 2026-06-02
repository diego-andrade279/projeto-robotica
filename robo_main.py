import tkinter as tk
from tkinter import scrolledtext
import threading
import logging
import time


# Configure logging
logging.basicConfig(level=logging.INFO, format='[LOG] %(message)s')

class RoboMain:
    def __init__(self, ui_callback):
        self.bateria = 100
        self.estado_atual = "Parado"
        self.comandos_validos = ["andar", "parar", "girar esquerda", "girar direita", "sentar", "levantar","acenar"]
        self.ui_callback = ui_callback # funçao de callback para atualizar a interface
        
    def registrar_log(self, mensagem, nivel='info'):
        """funaçao para registrar logs e atualizar a interface"""
        if nivel == 'info':
            logging.info(mensagem)
        elif nivel == 'warning':
            logging.warning(mensagem)
        elif nivel == 'error':
            logging.error(mensagem)

        
        self.ui_callback(f"[LOG] {mensagem}") # Atualiza a interface com a nova mensagem de log
    
    def verificar_bateria(self):
        """Verifica o nível da bateria e registra um aviso se estiver baixo."""
        if self.bateria < 20:
            self.registrar_log("Bateria baixa! Por favor, recarregue o robô.", nivel='warning')
        elif self.bateria <= 0:
            self.registrar_log("Bateria esgotada! O robô não pode se mover.", nivel='error')
            self.estado_atual = "Parado"
            self.ui_callback("Bateria esgotada! O robô não pode se mover.")
        return True if self.bateria > 0 else False
    
    def executar_comando(self, comando):
        """Executa um comando se for válido e a bateria estiver suficiente."""
        comando = comando.strip().lower()
        if comando not in self.comandos_validos:
            self.registrar_log(f"Comando inválido: '{comando}'", nivel='error')
            return False
        if not self.verificar_bateria():
            return False
        
        self.registrar_log(f"Executando comando: '{comando}'")

        text_minusculo = self.estado_atual.lower() # Atualiza o estado atual do robô com o comando executado

        # estados do robo 
        if comando == "andar":
            if text_minusculo == "sentado":
                self.registrar_log("O robô precisa se levantar antes de andar.", nivel='warning')
            
            else:
                self.ui_callback("O robô está andando... ")
                self.estado_atual = "Andando"
                self.bateria -= 5
        
        elif comando == "parar":
            self.ui_callback("O robô parou.")
            self.estado_atual = "Parado"

        elif comando == "sentar":
            if text_minusculo == "Andando":
                self.registrar_log("O robô precisa parar antes de sentar.", nivel='warning')
            else:
                self.ui_callback("O robô está sentado.")
                self.estado_atual = "Sentado"
                self.bateria -= 2
        
        elif comando == "levantar":
            if text_minusculo == "Sentado":
                self.ui_callback("O robô se levantou.")
                self.estado_atual = "Parado"
                self.bateria -= 3
            elif text_minusculo == "Andando":
                self.registrar_log("O robô esta em movimento .", nivel='warning')
            else:
                self.registrar_log("O robô ja esta em pe.", nivel='warning')
        
        elif comando == "girar esquerda":
            if text_minusculo == "sentado":
                self.registrar_log("O robô precisa se levantar antes de girar.", nivel='warning')
            else:
                self.ui_callback("O robô está girando à esquerda.")
                self.estado_atual = "Girando Esquerda"
                self.bateria -= 3

            self.ui_callback("O robô girou para a esquerda.")
        
        elif comando == "girar direita":
            if text_minusculo == "sentado":
                self.registrar_log("O robô precisa se levantar antes de girar.", nivel='warning')
            else:
                self.ui_callback("O robô está girando à direita.")
                self.estado_atual = "Girando Direita"
                self.bateria -= 3
            
            self.ui_callback("O robô girou para a direita.")

        elif comando == "acenar":
            if text_minusculo == "Andando":
                self.registrar_log("O robô precisa parar antes de acenar.", nivel='warning')
            else:
                self.ui_callback("O robô está acenando.")
                self.estado_atual = "Acenando"
                self.bateria -= 5
            
        self.ui_callback(f"Nível de bateria: {self.bateria}%") # Atualiza a interface com o nível de bateria atual

class AppGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Robo Main - Controle de Robô")
        self.root.geometry("900x800") # Define o tamanho da janela

        self.robo = RoboMain(self.atualizar_interface) # Cria uma instância do RoboMain e passa a função de callback
        self.escutando = False

        # Configura a interface gráfica
        self.construir_interface()

    def construir_interface(self):
        """Constrói a interface gráfica."""
        # painel de LOGS
        tk.Label(self.root, text="Logs de Atividade:", font=("Arial", 14)).pack(pady=10)
        self.painel_texto = scrolledtext.ScrolledText(self.root, width=55, height=15, state='disabled', font=("Arial", 12), bg="#f4f4f4")
        self.painel_texto.pack(pady=10)

        # Controles manuais
        tk.Label(self.root, text="Controles Manuais:", font=("Arial", 14)).pack(pady=10)
        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack()

        for cmd in ["Andar", "Parar", "Girar Esquerda", "Girar Direita", "Sentar", "Levantar","Acenar"]:
            btn = tk.Button(frame_botoes, text=cmd, width=15, height=2, font=("Arial", 12), command=lambda c=cmd: self.enviar_comando(c))
            btn.pack(side=tk.LEFT, padx=5)

        # Controle de voz
        tk.Label(self.root, text="Controle de Voz:", font=("Arial", 14, 'bold')).pack(pady=10)
        self.btn_voz = tk.Button(self.root, text="Ativar Controle de Voz", bg='lightblue', command=self.toggle_controle_voz)
        self.btn_voz.pack(pady=20)

        self.atualizar_interface("Sistema iniciado. Aguardando comandos.")

    def atualizar_interface(self, mensagem):
            """Atualiza a interface gráfica com uma nova mensagem."""
            self.painel_texto.config(state='normal')
            self.painel_texto.insert(tk.END, mensagem + "\n")
            self.painel_texto.see(tk.END) # Rola para a última linha
            self.painel_texto.config(state='disabled')
    
    def enviar_comando(self, comando):
        """Envia um comando para o RoboMain."""
        self.robo.executar_comando(comando.lower())

    def toggle_controle_voz(self):
        """Ativa ou desativa o controle de voz."""
        if not self.escutando:
            self.escutando = True
            self.btn_voz.config(text="Click para Parar Controle por Voz", bg='salmon')
            threading.Thread(target=self.abrir_microfone, daemon=True).start()
        else:
            self.escutando = False
            self.btn_voz.config(text="Ativar Controle de Voz", bg='lightblue')
            self.atualizar_interface("Controle de voz desativado.")
    # A função abrir_microfone foi adaptada para usar a API REST do Google Speech-to-Text, eliminando a dependência do SpeechRecognition e PyAudio, e garantindo compatibilidade com o ambiente atual.
    # Ela grava o áudio do microfone, converte para WAV em memória, codifica em base64 e envia para a API do Google, processando a resposta para extrair o comando de voz reconhecido.
    # essa versao que esta a baixo e devido ao notebbok que estou usando ser arquitetura ARM e nao ser compativel com o PyAudio, entao tive que adaptar a funçao para usar a API REST do Google Speech-to-Text, eliminando a dependência do SpeechRecognition e PyAudio, e garantindo compatibilidade com o ambiente atual.
    """
    def abrir_microfone(self):
        import io
        import json
        import base64
        import requests
        import wave
        import pyaudiowpatch as pyaudio

        SAMPLE_RATE = 16000
        CHUNK = 1024
        DURACAO_SEGUNDOS = 4
        FORMATO = pyaudio.paInt16
        CANAIS = 1

        self.atualizar_interface("Microfone ativado. Fale um comando...")

        try:
            p = pyaudio.PyAudio()
            stream = p.open(
                format=FORMATO,
                channels=CANAIS,
                rate=SAMPLE_RATE,
                input=True,
                frames_per_buffer=CHUNK
            )
        except Exception as e:
            self.atualizar_interface(f"Erro ao abrir microfone: {e}")
            self.escutando = False
            self.root.after(0, lambda: self.btn_voz.config(
                text="Ativar Controle de Voz", bg='lightblue'))
            return

        while self.escutando:
            try:
                self.atualizar_interface("Ouvindo...")
                frames = []
                for _ in range(0, int(SAMPLE_RATE / CHUNK * DURACAO_SEGUNDOS)):
                    data = stream.read(CHUNK, exception_on_overflow=False)
                    frames.append(data)

                # Monta WAV em memória
                buffer = io.BytesIO()
                wf = wave.open(buffer, 'wb')
                wf.setnchannels(CANAIS)
                wf.setsampwidth(p.get_sample_size(FORMATO))
                wf.setframerate(SAMPLE_RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                audio_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

                # Envia para API REST do Google
                payload = {
                    "config": {
                        "encoding": "LINEAR16",
                        "sampleRateHertz": SAMPLE_RATE,
                        "languageCode": "pt-BR"
                    },
                    "audio": {"content": audio_b64}
                }
                url = "https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
                resp = requests.post(url, json=payload, timeout=10)
                resultado = resp.json()

                if "results" in resultado:
                    transcricao = resultado["results"][0]["alternatives"][0]["transcript"].lower()
                    self.atualizar_interface(f"Comando reconhecido: '{transcricao}'")
                    for cmd in self.robo.comandos_validos:
                        if cmd in transcricao:
                            self.robo.executar_comando(cmd)
                            break
                else:
                    self.atualizar_interface("Não entendi. Tente novamente.")

            except Exception as e:
                if self.escutando:
                    self.atualizar_interface(f"Erro: {e}")

        stream.stop_stream()
        stream.close()
        p.terminate()
        self.atualizar_interface("Microfone desativado.")
        """
    # ============================================================
    # FUNÇÃO DE VOZ PARA x64
    # Se você está em x64, comente a função abrir_microfone atual
    # e descomente esta acima.
    # Instale a dependência: pip install pyaudio requests
    # ============================================================

    def abrir_microfone(self):
         import io
         import base64
         import requests
         import wave
         import pyaudio
     
         SAMPLE_RATE = 16000
         CHUNK = 1024
         DURACAO_SEGUNDOS = 4
         FORMATO = pyaudio.paInt16
         CANAIS = 1
     
         self.atualizar_interface("Microfone ativado. Fale um comando...")
     
         try:
             p = pyaudio.PyAudio()
             stream = p.open(
                 format=FORMATO,
                 channels=CANAIS,
                 rate=SAMPLE_RATE,
                 input=True,
                 frames_per_buffer=CHUNK
             )
         except Exception as e:
             self.atualizar_interface(f"Erro ao abrir microfone: {e}")
             self.escutando = False
             self.root.after(0, lambda: self.btn_voz.config(
                 text="Ativar Controle de Voz", bg='lightblue'))
             return
     
         while self.escutando:
             try:
                 self.atualizar_interface("Ouvindo...")
                 frames = []
                 for _ in range(0, int(SAMPLE_RATE / CHUNK * DURACAO_SEGUNDOS)):
                     data = stream.read(CHUNK, exception_on_overflow=False)
                     frames.append(data)
     
                 buffer = io.BytesIO()
                 wf = wave.open(buffer, 'wb')
                 wf.setnchannels(CANAIS)
                 wf.setsampwidth(p.get_sample_size(FORMATO))
                 wf.setframerate(SAMPLE_RATE)
                 wf.writeframes(b''.join(frames))
                 wf.close()
                 audio_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
     
                 payload = {
                     "config": {
                         "encoding": "LINEAR16",
                         "sampleRateHertz": SAMPLE_RATE,
                         "languageCode": "pt-BR"
                     },
                     "audio": {"content": audio_b64}
                 }
                 url = "https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
                 resp = requests.post(url, json=payload, timeout=10)
                 resultado = resp.json()
     
                 if "results" in resultado:
                     transcricao = resultado["results"][0]["alternatives"][0]["transcript"].lower()
                     self.atualizar_interface(f"Comando reconhecido: '{transcricao}'")
                     for cmd in self.robo.comandos_validos:
                         if cmd in transcricao:
                             self.robo.executar_comando(cmd)
                             break
                 else:
                     self.atualizar_interface("Não entendi. Tente novamente.")
     
             except Exception as e:
                 if self.escutando:
                     self.atualizar_interface(f"Erro: {e}")
     
         stream.stop_stream()
         stream.close()
         p.terminate()
         self.atualizar_interface("Microfone desativado.")
         
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()