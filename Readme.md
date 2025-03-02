# Caderno de Aulas de MC102 - Algoritmos e Programação de Computadores

## O que será necessário para utilizar o caderno:

Vocês precisarão ter acesso a um aplicativo chamado **Terminal**. Ele é uma das ferramentas mais úteis, pois permite interagir diretamente com o sistema operacional e executar praticamente qualquer comando. Usuários de **Mac** e **Linux** provavelmente já estão familiarizados com este aplicativo. No **Windows**, o acesso ao terminal é um pouco diferente, pois a Microsoft tem um ambiente próprio. Recomenda-se instalar um emulador de terminal mais amigável do que o **Prompt de Comando** ou o **PowerShell**, como o [Git Bash](https://git-scm.com/downloads). 

Durante a instalação do Git Bash, certifique-se de selecionar a opção **"Use Windows' default console window"**. Outra alternativa, recomendada para quem deseja se familiarizar com o ambiente **Linux**, é instalar o **Subsistema Windows para Linux (WSL)**, disponível nas versões mais recentes do **Windows 10 e Windows 11**. [Aqui](https://docs.microsoft.com/pt-br/windows/wsl/install) há um guia atualizado para a instalação do WSL.

Para criar um programa, utilizamos um **editor de texto** para escrever o código-fonte (e.g., [Vim](http://www.vim.org/), [Neovim](https://neovim.io/), [VSCode](https://code.visualstudio.com/)), ou uma **IDE** (Ambiente de Desenvolvimento Integrado), como [PyCharm](https://www.jetbrains.com/pycharm/) ou [WingIDE](http://wingware.com/). Além disso, precisaremos de um **interpretador Python**, que executa os comandos diretamente. Será necessário instalar o **Python 3**, disponível no site oficial: [https://www.python.org/downloads](https://www.python.org/downloads).

---

## Jupyter Notebook

O **Jupyter Notebook** tem sido amplamente utilizado na computação científica e no ensino de programação. Ele permite criar e compartilhar documentos interativos contendo código, equações, visualizações e textos explicativos. Você pode encontrar mais informações no site oficial: [https://jupyter.org](https://jupyter.org).

Para utilizar o material deste curso, siga os passos abaixo para instalar o **Jupyter Notebook** e algumas extensões. Com o **Python 3** já instalado, execute no terminal:

```sh
pip install jupyter jupyter_contrib_nbextensions tutormagic
jupyter contrib nbextension install --user
```

Se o comando `pip` não funcionar e sua instalação for apenas `python3`, tente `pip3`:

```sh
pip3 install jupyter jupyter_contrib_nbextensions tutormagic
jupyter contrib nbextension install --user
```

### Ativando Extensões

Para habilitar as extensões necessárias, use os seguintes comandos:

```sh
jupyter nbextension enable codefolding/main
jupyter nbextension enable latex_envs/latex_envs
jupyter nbextension enable python-markdown/main
jupyter nbextension enable toc2/main
```

Agora, seu **Jupyter Notebook** está pronto para ser utilizado. Para iniciá-lo, vá até a pasta onde o material do curso foi baixado e execute:

```sh
jupyter notebook
```

Isso exibirá algumas informações no terminal, incluindo o link para acessar o Jupyter Notebook pelo navegador:

```sh
[I 10:31:03.541 NotebookApp] O Jupyter Notebook está disponível em:
http://localhost:8888/?token=046cfa3064f0b118f56f6ef8859c4ab68d1d202d79445759
[I 10:31:03.541 NotebookApp] Use Control-C para encerrar o servidor e fechar todas as sessões.
```

Ao abrir o navegador, você verá o **Notebook Dashboard**, que listará todos os arquivos e subdiretórios do local onde o servidor foi iniciado. O ideal é iniciar o **Jupyter Notebook** no diretório que contém os materiais do curso **MC102**.

---

## Nota aos professores

Com o **RISE**, uma extensão do Jupyter Notebook, é possível transformar seus notebooks em apresentações interativas com **reveal.js**. Para instalá-lo, execute:

```sh
pip install RISE
jupyter-nbextension install rise --py --sys-prefix
```

Isso adicionará um novo botão chamado **"Enter/Exit RISE Slideshow"** à barra de ferramentas do Jupyter.

---

## Extras

Aqui estão alguns materiais complementares recomendados:

- 📖 Livro **"Practical Vim, 2ª edição - Edit Text at the Speed of Thought"** [The Pragmatic Bookshelf](https://pragprog.com/book/dnvim2/practical-vim-second-edition).
- 🎥 Vídeos de **Derek Wyatt** sobre o **editor Vim** no Vimeo: [Derek Wyatt](https://vimeo.com/user1690209).
- 📖 Livro online sobre o **editor VSCode**: [VSCode Documentation](https://code.visualstudio.com/docs).
- 🎥 Vídeo no YouTube: **"Setting up a Python Development Environment in VSCode"** [Corey Schafer](https://www.youtube.com/watch?v=-nh9rCzPJ20).
- 📘 [Full Stack Python](http://www.fullstackpython.com) – um livro aberto que explica conceitos de programação em linguagem acessível.

---

## Créditos

Durante a elaboração deste caderno de aulas, foram utilizados diversos materiais disponíveis na internet. Embora tenha sido feita a devida atribuição, caso alguma referência tenha sido esquecida, a responsabilidade é inteiramente minha, sem envolvimento da **Universidade de Campinas** ou do **Instituto de Computação**.

### Fontes:

- **"Composing Programs"**, John DeNero, UC Berkeley (Licença: Creative Commons Attribution-ShareAlike 3.0 Unported).
- **"Introduction to Computation and Programming Using Python"**, Ana Bell, Eric Grimson e John Guttag – MIT OpenCourseWare (Creative Commons License).
- **"Explorations in Computing - An Introduction to Computer Science and Python Programming"**, John S. Conery, University of Oregon (Creative Commons License).
- **"Think Python, 2ª Edição"**, Allen B. Downey (Licença: Creative Commons Attribution-NonCommercial CC BY-NC 3.0).
- **Documentação Oficial do Python 3**: [https://docs.python.org/3/](https://docs.python.org/3/) (Licença: PSF, compatível com GPL).
