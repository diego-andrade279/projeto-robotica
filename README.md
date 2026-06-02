# 🤖 Robô Humanoide v1.0

Sistema de controle de robô humanoide desenvolvido em Python com interface gráfica e reconhecimento de voz em português.

---

## 📋 Sobre o projeto

Este projeto foi desenvolvido como parte do **Teste Técnico para a vaga de Operador(a) & Trainer de Robô Humanoide**. O sistema simula o controle de um robô humanoide através de uma interface gráfica intuitiva, permitindo enviar comandos via botões ou por reconhecimento de voz.

---

## ✨ Funcionalidades

- ✅ Controle manual por botões na interface gráfica
- ✅ Reconhecimento de voz em português (pt-BR)
- ✅ Monitoramento de bateria em tempo real
- ✅ Sistema de logs com registro de todas as ações
- ✅ Validação de comandos e estados do robô
- ✅ Compatível com Windows x64 e ARM64

---

## 🖥️ Pré-requisitos

- Python 3.8 ou superior
- Windows 10 / 11 (x64 ou ARM64)
- Conexão com internet (para reconhecimento de voz)
- Microfone (apenas para controle por voz)

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/robo-humanoide.git
cd robo-humanoide
```

### 2. Descubra sua arquitetura

```bash
python -c "import platform; print(platform.machine())"
```

| Resultado            | Arquitetura                      |
|----------------------|----------------------------------|
| `AMD64` ou `x86_64`  | x64 — maioria dos notebooks      |
| `ARM64` ou `aarch64` | ARM64 — Snapdragon / Surface     |

### 3. Instale as dependências

**x64 (AMD64):**
```bash
pip install requests pyaudio
```

**ARM64 (Snapdragon):**
```bash
pip install requests pyaudiowpatch
```

### 4. Configure o código conforme sua arquitetura

O arquivo `robo_main.py` possui duas versões da função `abrir_microfone`:

- **ARM64** → função ativa por padrão (usa `pyaudiowpatch`)
- **x64** → função comentada logo abaixo (usa `pyaudio`)

Se você está em **x64**, comente a função ARM64 e descomente a função x64 no arquivo.

---

## ▶️ Como executar

```bash
python robo_main.py
```

---

## 🎮 Comandos disponíveis

| Comando          | Ação                          | Condição                    |
|------------------|-------------------------------|-----------------------------|
| `andar`          | Robô inicia locomoção         | Não pode estar sentado      |
| `parar`          | Robô para imediatamente       | Funciona em qualquer estado |
| `sentar`         | Robô senta                    | Não pode estar andando      |
| `levantar`       | Robô se levanta               | Deve estar sentado          |
| `girar esquerda` | Robô gira 90° à esquerda      | Não pode estar sentado      |
| `girar direita`  | Robô gira 90° à direita       | Não pode estar sentado      |
| `acenar`         | Robô acena com o braço        | Não pode estar andando      |

---

## 🎙️ Usando o controle de voz

1. Clique em **"Ativar Controle de Voz"**
2. Aguarde o log exibir `Ouvindo...`
3. Fale claramente um dos comandos acima em português
4. O log exibirá o comando reconhecido e a ação executada
5. Para desativar, clique novamente no botão

> 💡 **Dica:** O sistema ouve em ciclos de 4 segundos. Aguarde o `Ouvindo...` antes de falar.

---

## 🔋 Consumo de bateria

| Comando          | Consumo     |
|------------------|-------------|
| `andar`          | -5% por uso |
| `acenar`         | -5% por uso |
| `levantar`       | -3% por uso |
| `girar esquerda` | -3% por uso |
| `girar direita`  | -3% por uso |
| `sentar`         | -2% por uso |
| `parar`          | sem consumo |

> ⚠️ Abaixo de 20% o sistema emite alerta. A 0% os comandos são bloqueados. Reinicie o programa para restaurar a bateria.

---

## 📁 Estrutura do projeto

```
robo-humanoide/
│
├── robo_main.py               # Código principal do sistema
├── requirements.txt           # Dependências do projeto
├── Manual_RoboHumanoide.docx  # Manual completo do usuário
├── robo_main.exe              # Executável Windows (não requer Python)
├── robo_main.spec             # Configuração do PyInstaller
└── README.md                  # Este arquivo
```

---

## 🛠️ Problemas comuns

| Erro                           | Solução                                                            |
|--------------------------------|--------------------------------------------------------------------|
| `pyaudio` não instalado        | `pip install pyaudio` (x64) ou `pip install pyaudiowpatch` (ARM64)|
| `PortAudio library not found`  | Use `pyaudiowpatch` e ative a função correta no código             |
| `FLAC conversion error`        | O código já usa API REST do Google — sem dependência de FLAC       |
| Microfone não abre             | Configurações → Privacidade → Microfone → Permitir                 |
| Comando não reconhecido        | Fale mais devagar e aguarde o `Ouvindo...` antes de falar          |
| Robô não anda                  | Verifique se está sentado — execute `levantar` primeiro            |
| Bateria esgotada               | Reinicie o programa para restaurar a bateria para 100%             |

---

## 🧰 Tecnologias utilizadas

- [Python 3](https://www.python.org/) — linguagem principal
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — interface gráfica
- [PyAudio](https://pypi.org/project/PyAudio/) / [PyAudioWPatch](https://pypi.org/project/PyAudioWPatch/) — captura de áudio
- [Google Speech-to-Text API](https://cloud.google.com/speech-to-text) — reconhecimento de voz
- [Requests](https://pypi.org/project/requests/) — requisições HTTP

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de avaliação técnica.
