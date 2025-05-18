# 🕒 Sistema de Registro de Presença com QR Code

Este projeto registra a presença de usuários via formulário web, com autenticação opcional via QR Code. Os registros são armazenados localmente em uma planilha Excel (`presencas.xlsx`) com proteção contra duplicidade.

---

## 🚀 Funcionalidades

- ✅ Formulário SPA com validação de CPF e máscara
- ✅ Geração automática de horário e localização
- ✅ Armazenamento em Excel com cache e sem duplicações
- ✅ Interface em carrossel: QR Code ⇄ Formulário
- ✅ QR Code funcional para celulares
- ✅ Design temático de Festa Junina 🎉

---

## 🧰 Tecnologias utilizadas

| Tecnologia      | Uso principal                        |
|------------------|--------------------------------------|
| **FastAPI**      | Backend da API                       |
| **Uvicorn**      | Servidor ASGI para FastAPI           |
| **Jinja2**       | Renderização de páginas HTML         |
| **OpenPyXL**     | Registro e leitura da planilha Excel |
| **QRcode**       | Geração de códigos QR                |
| **JavaScript**   | Máscara de CPF, envio de dados       |
| **HTML/CSS**     | Interface carrossel SPA              |

---

## 📁 Estrutura de Diretórios

```bash
frequence-controller/
├── presence_service/
│   ├── main.py         # Rota API para registro
│   └── sheets.py       # Lógica de Excel otimizada com cache
├── web_service/
│   ├── main.py         # Interface + QR Code
│   ├── templates/
│   │   └── landing.html
│   └── static/
│       ├── css/
│       │   └── landing.css
│       └── js/
│           └── landing.js
├── presencas.xlsx      # Planilha gerada automaticamente
├── requirements.txt    # Dependências Python
└── README.md           # Este arquivo :)
