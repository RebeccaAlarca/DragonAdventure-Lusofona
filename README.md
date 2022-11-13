# DragonAdventure-Lusofona
Python game text RPG - Introdução a Computação
___
* Autoria: Rebecca Barros Alarça
* Número de aluno: 22010373
___
Projeto feito individualmente.

**Arquitetura do Projeto:**
* A primeira coisa feita foi a função de Introdução (função start()), na qual já havia encontrado meios de ajustar a interface.
 Depois, pensei em meios de guardar as informações dos personagens: a primeira tentativa foi por uma classe onde abrangia
todos os atributos em comum de todos os personagens, incluindo inimigos. Visto que não consegui mexer com isto, fiz uma 
classe para cada um individualmente. 
* Após todos os personagens já terem sido guardados na memória, criei uma função whoinit() que usa um d20 de número 
 aleatório para descobrir qual deles começariam a fase de ataque. 
* A partir disto, o personagem escolhido pela função anterior começa o round, com uma função cheia de "if's" para cada caso específico.
Quando este round termina, os outros são lançados em loop para cada personagem, e só acaba quando os personagens jogáveis 
morrem(Game Over) ou quando todos os inimigos morrem, levando assim para uma opção de EXIT ou voltar para o MENU.
* Faço o uso do **import random**; para os dados, **import os**; para limpar a tela do MENU; e **import sys**; para o comando EXIT.
---
**Referências:**
* [Cores Interface](https://www.geeksforgeeks.org/print-colors-python-terminal/)
* [Ajuda para achar o maior de uma lista](https://www.pythonprogressivo.net/2018/10/Funcao-Mostra-Maior-Menor-Numero-Python.html) > Me ajudou a pensar em como criar a função whoinit().
* Troca de ideias com o meu pai(programador), que me explicou quando compilava erros dos quais eu não entendia
e me tirou dúvidas necessárias para a execução do projeto.
