import os
from pathlib import Path
import shutil
import datetime

class OrganizadorDownloads:
    def __init__(self, pasta_downloads=None):
        """
        Inicializa o organizador com a pasta de downloads
        Se não especificada, usa a pasta Downloads padrão do usuário
        """
        if pasta_downloads is None:
            self.pasta_downloads = Path.home() / "Downloads"
        else:
            self.pasta_downloads = Path(pasta_downloads)
        
        # Dicionário que mapeia extensões para tipos de arquivo
        self.tipos_arquivo = {
            'imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'],
            'documentos': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'],
            'planilhas': ['.xls', '.xlsx', '.csv', '.ods'],
            'apresentacoes': ['.ppt', '.pptx', '.odp', '.key'],
            'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'audios': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'compactados': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            'executaveis': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg'],
            'codigo': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.php', '.rb']
        }
    
    def identificar_tipo_arquivo(self, arquivo):
        """Identifica o tipo do arquivo baseado na extensão"""
        extensao = arquivo.suffix.lower()
        
        for tipo, extensoes in self.tipos_arquivo.items():
            if extensao in extensoes:
                return tipo.capitalize()
        
        return "Outros"
    
    def criar_pastas_organizacao(self):
        """Cria as pastas de organização se não existirem"""
        pasta_organizada = self.pasta_downloads / "Arquivos_Organizados"
        
        for tipo in self.tipos_arquivo.keys():
            pasta_tipo = pasta_organizada / tipo.capitalize()
            pasta_tipo.mkdir(parents=True, exist_ok=True)
        
        # Pasta para arquivos sem categoria definida
        (pasta_organizada / "Outros").mkdir(parents=True, exist_ok=True)
        
        return pasta_organizada
    


    def mover_arquivo(self, arquivo_origem, pasta_destino):
        """Move um arquivo para a pasta destino, evitando conflitos de nome"""
        nome_arquivo = arquivo_origem.name
        arquivo_destino = pasta_destino / nome_arquivo
        
        # Se já existe um arquivo com o mesmo nome, adiciona timestamp
        if arquivo_destino.exists():
            nome_base = arquivo_origem.stem
            extensao = arquivo_origem.suffix
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            novo_nome = f"{nome_base}_{timestamp}{extensao}"
            arquivo_destino = pasta_destino / novo_nome
        
        try:
            shutil.move(str(arquivo_origem), str(arquivo_destino))
            return True, arquivo_destino
        except Exception as e:
            return False, str(e)
        
    def organizar_downloads(self, mostrar_progresso=True):
        """Organiza todos os arquivos da pasta Downloads"""
        
        if not self.pasta_downloads.exists():
            print(f"❌ Pasta {self.pasta_downloads} não encontrada!")
            return
        
        # Criar estrutura de pastas
        pasta_organizada = self.criar_pastas_organizacao()
        
        # Listar todos os arquivos (exceto pastas)
        arquivos = [f for f in self.pasta_downloads.iterdir() 
                   if f.is_file() and f.name != '.DS_Store']
        
        if not arquivos:
            print("📁 Nenhum arquivo encontrado para organizar!")
            return
        
        print(f"🔍 Encontrados {len(arquivos)} arquivo(s) para organizar...")
        print("=" * 50)
        
        estatisticas = {}
        sucessos = 0
        erros = 0
        
        for arquivo in arquivos:
            tipo_arquivo = self.identificar_tipo_arquivo(arquivo)
            pasta_destino = pasta_organizada / tipo_arquivo
            
            if mostrar_progresso:
                print(f"📄 {arquivo.name} → {tipo_arquivo}/")
            
            sucesso, resultado = self.mover_arquivo(arquivo, pasta_destino)
            
            if sucesso:
                sucessos += 1
                estatisticas[tipo_arquivo] = estatisticas.get(tipo_arquivo, 0) + 1
                if mostrar_progresso:
                    print(f"   ✅ Movido com sucesso!")
            else:
                erros += 1
                if mostrar_progresso:
                    print(f"   ❌ Erro: {resultado}")
            
            if mostrar_progresso:
                print()
        
        # Mostrar relatório final
        self.mostrar_relatorio(sucessos, erros, estatisticas, pasta_organizada)
    
    def mostrar_relatorio(self, sucessos, erros, estatisticas, pasta_organizada):
        """Mostra um relatório final da organização"""
        print("=" * 50)
        print("📊 RELATÓRIO DE ORGANIZAÇÃO")
        print("=" * 50)
        print(f"✅ Arquivos organizados: {sucessos}")
        print(f"❌ Erros: {erros}")
        print(f"📁 Pasta de destino: {pasta_organizada}")
        print()
        
        if estatisticas:
            print("📋 Arquivos por categoria:")
            for tipo, quantidade in sorted(estatisticas.items()):
                print(f"   {tipo}: {quantidade} arquivo(s)")
        
        print("=" * 50)
        print("🎉 Organização concluída!")