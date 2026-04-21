"""Ferramenta de Desenvolvimento: Watcher de Live Reload.

Este script monitora alteracoes nos arquivos fonte e reinicia o aplicativo
automaticamente, proporcionando um workflow agil (similar ao Hot Reload).
"""

import os
import sys
import time
import subprocess
from datetime import datetime

# Configuracoes de monitoramento
WATCH_DIRS = ['src', 'data']
EXTENSIONS = ('.py', '.css')
CMD = [sys.executable, '-m', 'src.main']

def get_last_mtime():
    """Calcula o timestamp da ultima modificacao em todos os arquivos monitorados.

    Percorre recursivamente as pastas em WATCH_DIRS procurando por extensoes validas.

    Returns:
        float: O maior (mais recente) mtime encontrado.
    """
    max_mtime = 0
    for d in WATCH_DIRS:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for f in files:
                if f.endswith(EXTENSIONS):
                    path = os.path.join(root, f)
                    max_mtime = max(max_mtime, os.path.getmtime(path))
    return max_mtime

def main():
    """Loop principal que monitora o sistema de arquivos e gerencia o processo do app."""
    print("🚀 Iniciando Modo Live Reload...")
    print(f"👀 Monitorando: {', '.join(WATCH_DIRS)}")
    
    process = None
    last_mtime = get_last_mtime()

    def start_app():
        """Finaliza o processo anterior (se houver) e inicia uma nova instancia do app."""
        nonlocal process
        if process:
            # Tenta encerrar graciosamente primeiro
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                # Forca o encerramento se travar
                process.kill()
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 🔃 Reiniciando aplicativo...")
        process = subprocess.Popen(CMD)

    # Inicia a primeira instancia
    start_app()

    try:
        while True:
            time.sleep(1) # Intervalo de verificacao (1 segundo)
            current_mtime = get_last_mtime()
            
            # Se algo mudou, reinicia
            if current_mtime > last_mtime:
                last_mtime = current_mtime
                start_app()
                
    except KeyboardInterrupt:
        print("\nStopping Live Reload...")
        if process:
            process.terminate()

if __name__ == "__main__":
    main()
