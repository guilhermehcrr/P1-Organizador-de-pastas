# 🗂️ Download Organizer

Um sistema automatizado e inteligente para organizar arquivos da pasta Downloads, categorizando-os por tipo de arquivo.

## ✨ Funcionalidades

- 🎯 **Categorização Inteligente**: Organiza automaticamente em 9+ categorias
- 🔄 **Resolução de Conflitos**: Renomeia arquivos duplicados com timestamp
- 📊 **Relatórios Detalhados**: Estatísticas completas da organização
- 🛡️ **Operação Segura**: Confirmação do usuário e tratamento de erros
- 🎨 **Interface Amigável**: Output colorido com emojis e progresso em tempo real

## 🚀 Instalação e Uso

### Requisitos
- Python 3.6+
- Biblioteca `pathlib` (incluída no Python 3.4+)

### Execução
```bash
python organizador.py

### Uso Programático

from organizador import OrganizadorDownloads

# Usar pasta Downloads padrão
organizador = OrganizadorDownloads()
organizador.organizar_downloads()

# Usar pasta customizada
organizador = OrganizadorDownloads("/caminho/para/pasta")
organizador.organizar_downloads()