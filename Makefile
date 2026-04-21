.PHONY: run dev build flatpak clean

run:
	python3 -m src.main

dev:
	python3 dev.py

build:
	@echo "🛠️ Gerando binário com PyInstaller..."
	pip install pyinstaller
	pyinstaller --noconfirm --onefile --windowed \
		--add-data "data/style.css:data" \
		--name "todolist-gtk" \
		src/main.py
	@echo "✅ Build concluído! O executável está em dist/todolist-gtk"

flatpak: build
	@echo "📦 Construindo e instalando Flatpak..."
	flatpak-builder --user --install --force-clean build-dir com.vitordevsp.TodoList.yml
	@echo "🎉 Instalado! Procure por 'Todo List GTK' no seu menu de aplicativos."

bundle: build
	@echo "🎁 Gerando bundle .flatpak (para simular download da web)..."
	flatpak-builder --force-clean build-dir com.vitordevsp.TodoList.yml
	flatpak build-bundle build-dir todolist.flatpak com.vitordevsp.TodoList
	@echo "✅ Pronto! O arquivo 'todolist.flatpak' foi criado na raiz."

clean:
	@echo "🧹 Limpando arquivos temporários..."
	rm -rf build/ dist/ __pycache__ src/__pycache__ *.spec build-dir/
	@echo "✨ Limpo!"
