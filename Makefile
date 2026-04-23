APP_ID := br.com.vitordevsp.TodoList
BUNDLE := todolist.flatpak
BUILDDIR := build/flatpak-build
REPO := build/repo
STATE_DIR := build/.flatpak-builder-state
MANIFEST := $(APP_ID).yml
PYTHON := python3
FLATPAK_BUILDER_FLAGS := --disable-download --disable-rofiles-fuse

.PHONY: run dev build flatpak bundle uninstall uninstall-data clean check-build-tools check-flatpak-tools

run:
	$(PYTHON) -m src.main

dev:
	$(PYTHON) dev.py

check-build-tools:
	@$(PYTHON) -m PyInstaller --version >/dev/null

check-flatpak-tools:
	@command -v flatpak-builder >/dev/null
	@command -v flatpak >/dev/null

build: check-build-tools
	@echo "🛠️ Gerando binário com PyInstaller..."
	$(PYTHON) -m PyInstaller --noconfirm --onefile --windowed \
		--collect-all gi \
		--add-data "src/styles/style.css:src/styles" \
		--name "todolist-gtk" \
		src/main.py
	@echo "✅ Build concluído! O executável está em dist/todolist-gtk"

flatpak: build check-flatpak-tools
	@echo "📦 Construindo e instalando Flatpak..."
	flatpak-builder $(FLATPAK_BUILDER_FLAGS) --user --install --force-clean --state-dir=$(STATE_DIR) $(BUILDDIR) $(MANIFEST)
	@echo "🎉 Instalado! Procure por 'Todo List GTK' no seu menu de aplicativos."

bundle: check-flatpak-tools
	@echo "🎁 Gerando bundle .flatpak oficial..."
	+$(MAKE) clean
	flatpak-builder $(FLATPAK_BUILDER_FLAGS) --repo=$(REPO) --force-clean --state-dir=$(STATE_DIR) $(BUILDDIR) $(MANIFEST)
	flatpak build-bundle --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo $(REPO) $(BUNDLE) $(APP_ID)
	@echo "✅ Pronto! O arquivo '$(BUNDLE)' foi criado na raiz."

uninstall: check-flatpak-tools
	@echo "🗑️ Desinstalando Flatpak do usuário atual..."
	flatpak uninstall --user -y $(APP_ID)
	@echo "✅ Flatpak desinstalado."

uninstall-data: check-flatpak-tools
	@echo "🗑️ Desinstalando Flatpak e removendo dados do sandbox..."
	flatpak uninstall --user --delete-data -y $(APP_ID)
	@echo "✅ Flatpak e dados locais removidos."

clean:
	@echo "🧹 Limpando todos os arquivos temporários e pacotes..."
	rm -rf build/ dist/ __pycache__ src/__pycache__ *.spec
	rm -f $(BUNDLE)
	@echo "✨ Tudo limpo!"
