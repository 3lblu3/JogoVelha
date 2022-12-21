# JOGO DA VELHA
Tem como arquivo principal o 'main.py', não possui interface gráfica e é executado pelo terminal.
Esse é um jogo interativo entre 2 jogadores; não possui interface de usuário, tudo é executado pelo terminal. <br>

## Detalhes
1. A casa que deseja jogar é enumerada de acordo com a linha e a coluna em que ela está inserida.<br/>
   Exemplo: jogada de x na **linha** 2 e **coluna** 2, deve ser digitado '22' (sem espaços):<br />
      11 12 13<br />21 **X** 23<br />31 32 33<br />

2. Por padrão o 1° jogador sempre será o 'x' e o 2° a 'o' 

## Código
É separado em 3 categorias, sendo eles (nome = nome arquivo): <br />

Main = main<br /> 
Função Jogar = jogo_funcoes <br />
Função ganhador = funcoes_ganhador <br />
Função erro = funcoes_erro
### Main

Aqui que pegamos o seu nome e é onde fica o menu principal de opções como:
1. Quantas partidas deseja jogar
2. Qual o tabuleiro (3x3; 4x4; 5x5) que deseja usar;
3. Se deseja jogar novamente.
   1. Por padrão pegamos a quantidade de partidas e o tabuleiro que selecionou préviamente.<br/>
### Função jogar
Onde os tabuleiros fica e onde a jogada é feita.
### Função ganhador
Verifica se há um ganhador ou se deu velha.
### Função erro
Aqui checa-se se há possiveis erros como:
1. Digitar caracteres diferentes de números na hora de escolher a casa a ser jogada;
2. Se o número digitado é correspondente ao jogo, e se essa jogada é livre.
