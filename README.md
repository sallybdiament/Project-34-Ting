# Ting - Computer Science Project

Projeto em **Python** para implementar um programa que simule um algoritmo de indexação de documentos similar ao do Google, capaz de identificar ocorrências de termos em arquivos TXT.

Projeto 34 da [Trybe](https://wwww.betrybe.com), módulo de Ciência da Computação.

## O Projeto

* Criar método que implementa uma fila para os arquivos TXT que serão lidos.
* Criar método que Implementa uma função ```txt_importer``` dentro do módulo ```file_management``` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
* Implementar a função ```process``` no módulo ```file_process```, capaz de transformar o conteúdo da lista gerada pela função ```txt_importer``` em um dicionário que será armazenado dentro da Queue.
* Implementar uma função ```remove``` dentro do módulo ```file_process``` capaz de remover o primeiro arquivo processado.
* Implementer uma função ```file_metadata``` dentro do módulo ```file_process``` capaz de apresentar as informações superficiais de um arquivo processado.
* Implementar uma função ```exists_word```, dentro do módulo ```word_search```, que verifique a existência de uma palavra em todos os arquivos processados.


## Instalação 

#### 1- Clonar o repositório

```git clone git@github.com:sallybdiament/Project-34-Ting.git```

#### 2 - Crie o ambiente virtual para o projeto

```python3 -m venv .venv && source .venv/bin/activate```

#### 3 - Instalar as dependências

```python3 -m pip install -r dev-requirements.txt```


## Tecnologias
- Python
- Flake8 e Black
- Queue
- Stack
- Lists
