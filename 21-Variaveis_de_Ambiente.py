"""
Variáveis de ambiente são variáveis que são definidas no Sistema Operacional ao invés de serem 
definidas no próprio programa. Sendo assim, essas variáveis podem ser definidas previamente e isoladas 
dos arquivos que serão utilizados na execução/interpretação.
Isso é vantajoso caso seja necessário manter anônimos alguns dados como usuário e senha de aplicações,
que poderão ser definidos somente na máquina/servidor/sistema do administrador e que serão apenas importadas
na aplicação.

No Windows, para criar uma variável, usar o powershell ou cmd, com o comando
set USUARIO luciano
set SENHA 1919

E no programa que for necessário utilizar essas variáveis

import os #biblioteca exigida para permitir a importação de variáveis de ambiente
usuario = os.environ.get('USUARIO')
senha = os.environ.get('SENHA')

Assim, as variáveis usuario e senha da aplicação recebem os valores das variáveis de ambiente USUARIO e SENHA, sem
precisar explicitar no código da aplicação, seus valores.

Outra aplicação pertinente das variáveis de ambiente é a diferenciação entre ambiente de desenvolvimento e ambiente de produção.
Caso a aplicação esteja alocada no servidor de desenvolvimento, usa-se uma variável, por exemplo, AMBIENTE, que recebe valor dev

set AMBIENTE dev

E com esse valor, na minha aplicação eu crio condicionais que só serão executadas caso essa variável AMBIENTE tenha valor dev, ou seja, alugmas aplicação só são acessíveis durante o ambiente de desenvolvimento.
Dessa mesma forma, posso criar funcionalidades que só serão acessíveis no ambiente de produção, definindo nesse servidor do ambiente de produção, a variável AMBIENTE com valor prod

set AMBIENTE prod
"""