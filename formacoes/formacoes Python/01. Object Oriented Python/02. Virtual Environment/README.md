### Virtual Environment

```https://www.alura.com.br/artigos/ven-poetry-no-python```

&nbsp;
&nbsp;

#### Venv

O Venv é uma ferramenta integrada ao Python que permite criar ambientes virtuais isolados.

O uso de Venv é recomendado pelo PEP 405 (Python Enhancement Proposal), que descreve a padronização para a criação de ambientes virtuais no Python.

&nbsp;

Para utilizar o Venv, deve primeiro criar um novo ambiente virtual, com o comando:

```BASH
python -m venv nome_do_ambiente
```

&nbsp;

Esse comando cria uma nova pasta com todos os arquivos necessários para o ambiente virtual. Para ativar o ambiente, em sistemas Unix ou MacOS, use:

```BASH
source nome_do_ambiente/bin/activate
```

&nbsp;

No Windows, o comando é:

```BASH
nome_do_ambiente\Scripts\activate
```

Quando o ambiente virtual está ativo, qualquer pacote instalado com `pip` será isolado dentro desse ambiente, sem afetar o sistema global.

Para desativar o ambiente virtual, basta usar o comando deactivate. Isso retorna o terminal ao ambiente global do sistema.

Existem alguns comandos importantes no Python que ajudam a manter o ambiente organizado e documentado.

Por exemplo, `pip freeze` é um comando que lista todas as dependências instaladas no ambiente virtual junto com suas versões.

Outro comando essencial é `pip freeze > requirements.txt`, que redireciona a saída do pip freeze para um arquivo chamado `requirements.txt`.

Esse arquivo pode ser compartilhado com outros desenvolvedores para garantir que todos usem as mesmas versões de pacotes.

O comandos como `pip install -r requirements.txt` permite instalar todas as dependências listadas em um arquivo `requirements.txt` de uma só vez.

E `pip list` fornece uma lista detalhada de todos os pacotes instalados, facilitando a gestão e atualização dos pacotes no seu ambiente virtual.

&nbsp;
&nbsp;

#### Evolucao do Ambiente Virtual

O processo de empacotamento de pacotes em `Python` era dominado por três ferramentas essenciais: `setuptools`, `venv` e `pip`.

`Setuptools` usado para criar os pacotes, `virtualenv` para estabelecer ambientes virtuais isolados e `pip` para instalar os pacotes nos ambientes.

Em 2015, `Thomas Kluyver` desenvolveu o `Flit`, alternativa na construção de pacotes `Python` que visava criar e disponibilizar pacotes no repositório `PyPI`.

Em 2016, `Donald Stufft` da equipe do `pip`, explorou o `Pipfile` destinada a substituir os tradicionais arquivos de requisitos, introduzindo um formato de arquivo de bloqueio.

Esses esforços, culminaram em 2017 o lançamento do `Pipenv` por `Kenneth Reitz`, ferramenta que permiti gerenciar dependências e ambientes `Python` de forma reproduzível.

O `Pipenv` não empacotava o aplicativo diretamente, mas sim possibilitava a organização de diversos módulos `Python` em um repositório `Git`.

No ano de 2018, `Sébastien Eustace` iniciou o desenvolvimento do `Poetry`, a ferramenta oferece a integracao de empacotamento, gerenciamento de dependências e ambientes.

&nbsp;
&nbsp;

#### O que é Poetry

O `Poetry` (poesia em portugues) é uma ferramenta para gerenciamento de dependências e empacotamento em `Python`.

Permite declarar as bibliotecas que serao usadas no projeto e irá gerenciá-las, instalá-las e atualizá-las.

Tambem oferece um arquivo de bloqueio para instalações repetíveis e construir seu projeto para distribuição. `Poetry` e uma alternativa ao `pip` e `venv`.

Através do arquivo `pyproject.toml`, `Poetry` permite especificar as dependências de forma declarativa, facilitando a instalação e a atualização.

Visa solucionar a falta de controle das dependências do projeto, jgarantindo a criação do ambiente de desenvolvimento em diferentes máquinas.

Automatizando a criação e gerenciamento de ambientes virtuais, sem o uso de ferramentas como `Venv`.

Enquanto o `pyproject.toml` é usado para especificar as dependências e configurações do projeto, o arquivo `package.json` é a contraparte no ecossistema `Node.js`.

Ambos têm o objetivo de fornecer a estrutura de definir dependências do projeto e versões, além de outras configurações relevantes.

&nbsp;
&nbsp;

#### Instalando e configurando o Poetry

Para usar o `Poetry`, precisa ter o `Python 3.8+` instalado.

Verificar versao de `Python` instalado:

```BASH
python3 --version
```

ou

```BASH
python3 -V
```

Atualizando sistema:

```BASH
sudo apt update
```

Instalando Python:

```BASH
sudo apt install python3
```

Verificando se pacote `pipx` esta instaldo:

```BASH
pipx --version
```

Instalando pacote `pipx`:

```BASH
sudo apt install pipx
```


Instalando `Poetry`:

```BASH
sudo pipx install poetry
```

Configuracoes adicionais:

```BASH
  installed package poetry 1.8.4, installed using Python 3.12.3
  These apps are now globally available
    - poetry
⚠️  Note: '/root/.local/bin' is not on your PATH environment variable. These
    apps will not be globally accessible until your PATH is updated. Run `pipx
    ensurepath` to automatically add it, or manually modify your PATH in your
    shell's config file (i.e. ~/.bashrc).
done! ✨ 🌟 ✨
ernane@linux-Dell:~$ sudo pipx ensurepath
Success! Added /root/.local/bin to the PATH environment variable.

Consider adding shell completions for pipx. Run 'pipx completions' for
instructions.

You will need to open a new terminal or re-login for the PATH changes to take
effect.

Otherwise pipx is ready to go! ✨ 🌟 ✨
```

Para atualizar ou desinstalar o `Poetry`:

```BASH
pipx upgrade poetry
```

```BASH
pipx uninstall poetry
```

&nbsp;
&nbsp;

#### Exemplo pratico

Criando projeto usando `Poetry` e `Flask`:

```BASH
sudo poetry new flask_poetry
```

Criacao do `pyproject.toml`:

```TOML
[tool.poetry]
name = "flask-poetry"
version = "0.1.0"
description = ""
authors = ["ernanecl"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

O arquivo especifica metadados como nome, versão e descrição do projeto. 

Indica que o projeto do Python é a versão 3.12, inclui uma referência ao arquivo README.md para a documentação do projeto.

Também contém a configuração para o sistema de construção, que especifica que o `Poetry Core` é necessário.

E que o `backend` de construção é fornecida pelo módulo `poetry.core.masonry.api`.

&nbsp;

Acessando o diretorio:

```BASH
sudo cd flask_poetry
```

&nbsp;

Podemos adicionar o Flask como dependência do projeto:

```BASH
sudo poetry add flask
```

&nbsp;

Com a execucao do ultimo comando, verificamos o arquivo `pyproject.toml` e notamos que foi atualizado com o pacote `Flask` como dependencia dp projeto.

```TOML
[tool.poetry.dependencies]
python = "^3.12"
flask = "^3.0.3"
```

&nbsp;

Criando e acessando o arquivo `app.py`:

```BASH
sudo vim app.py
```

```PY
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```