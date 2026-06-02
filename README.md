🤖 Robô Humanoide v1.0
Sistema de controle de robô humanoide desenvolvido em Python com interface gráfica e reconhecimento de voz em português.

📋 Sobre o projeto
Este projeto foi desenvolvido como parte do Teste Técnico. O sistema simula o controle de um robô humanoide através de uma interface gráfica intuitiva, permitindo enviar comandos via botões ou por reconhecimento de voz.

✨ Funcionalidades

✅ Controle manual por botões na interface gráfica
✅ Reconhecimento de voz em português (pt-BR)
✅ Monitoramento de bateria em tempo real
✅ Sistema de logs com registro de todas as ações
✅ Validação de comandos e estados do robô
✅ Compatível com Windows x64 e ARM64


🖥️ Pré-requisitos

Python 3.8 ou superior
Windows 10 / 11 (x64 ou ARM64)
Conexão com internet (para reconhecimento de voz)
Microfone (apenas para controle por voz)


⚙️ Instalação
1. Clone o repositório
bashgit clone https://github.com/diego-andrade279/projeto-robotica
cd projeto-robotica
2. Descubra sua arquitetura
bashpython -c "import platform; print(platform.machine())"
ResultadoArquiteturaAMD64 ou x86_64x64 — maioria dos notebooksARM64 ou aarch64ARM64 — Snapdragon / Surface
3. Instale as dependências
x64 (AMD64):
bashpip install requests pyaudio
ARM64 (Snapdragon):
bashpip install requests pyaudiowpatch
4. Configure o código conforme sua arquitetura
O arquivo robo_main.py possui duas versões da função abrir_microfone:

ARM64 → função ativa por padrão (usa pyaudiowpatch)
x64 → função comentada logo abaixo (usa pyaudio)

Se você está em x64, comente a função ARM64 e descomente a função x64 no arquivo.

▶️ Como executar
bashpython robo_main.py

🎮 Comandos disponíveis
ComandoAçãoCondiçãoandarRobô inicia locomoçãoNão pode estar sentadopararRobô para imediatamenteFunciona em qualquer estadosentarRobô sentaNão pode estar andandolevantarRobô se levantaDeve estar sentadogirar esquerdaRobô gira 90° à esquerdaNão pode estar sentadogirar direitaRobô gira 90° à direitaNão pode estar sentadoacenarRobô acena com o braçoNão pode estar andando

🎙️ Usando o controle de voz

Clique em "Ativar Controle de Voz"
Aguarde o log exibir Ouvindo...
Fale claramente um dos comandos acima em português
O log exibirá o comando reconhecido e a ação executada
Para desativar, clique novamente no botão


💡 Dica: O sistema ouve em ciclos de 4 segundos. Aguarde o Ouvindo... antes de falar.


🔋 Consumo de bateria
ComandoConsumoandar-5% por usoacenar-5% por usolevantar-3% por usogirar esquerda-3% por usogirar direita-3% por usosentar-2% por usopararsem consumo

⚠️ Abaixo de 20% o sistema emite alerta. A 0% os comandos são bloqueados. Reinicie o programa para restaurar a bateria.


📁 Estrutura do projeto
robo-humanoide/
│
├── robo_main.py               # Código principal do sistema
├── requirements.txt           # Dependências do projeto
├── Manual_RoboHumanoide.docx  # Manual completo do usuário
├── robo_main.exe              # Executável Windows (não requer Python)
├── robo_main.spec             # Configuração do PyInstaller
└── README.md                  # Este arquivo

🛠️ Problemas comuns
ErroSoluçãopyaudio não instaladopip install pyaudio (x64) ou pip install pyaudiowpatch (ARM64)PortAudio library not foundUse pyaudiowpatch e ative a função correta no códigoFLAC conversion errorO código já usa API REST do Google — sem dependência de FLACMicrofone não abreConfigurações → Privacidade → Microfone → PermitirComando não reconhecidoFale mais devagar e aguarde o Ouvindo... antes de falarRobô não andaVerifique se está sentado — execute levantar primeiroBateria esgotadaReinicie o programa para restaurar a bateria para 100%

🧰 Tecnologias utilizadas

Python 3 — linguagem principal
Tkinter — interface gráfica
PyAudio / PyAudioWPatch — captura de áudio
Google Speech-to-Text API — reconhecimento de voz
Requests — requisições HTTP


📄 Licença
Este projeto foi desenvolvido para fins educacionais e de avaliação técnica.
