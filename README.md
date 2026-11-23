# Quiz de Conhecimentos Gerais
Aplicativo de linha de comando desenvolvido em Python para a atividade prática sobre **funcoes (`def`)**.

## Descricao

Jogo de perguntas e respostas no terminal. A cada partida, 5 perguntas de conhecimentos gerais sao sorteadas e o usuário responde escolhendo uma alternativa (A, B, C ou D). Ao final, o programa mostra a pontuação e uma classificação, e guarda o histórico das partidas jogadas.
Obs: Duas perguntas troll kkk

## Funcionalidades
1. **Jogar:** inicia uma partida com 5 perguntas sorteadas
2. **Ver regras:** explica como o jogo funciona
3. **Ver historico:** mostra o resultado de cada partida e o melhor desempenho
0. **Sair:** encerra o programa

## Como executar

```bash
python quiz_conhecimentos_gerais.py
```

## Conceitos aplicados

- Funcoes com `def` (`exibir_menu`, `exibir_regras`, `fazer_pergunta`, `classificar`, `jogar`, `exibir_historico`, `main`)
- Funcoes com parametros (`fazer_pergunta(pergunta)` e `classificar(acertos, total)`)
- Funcoes com retorno (`fazer_pergunta` retorna `True`/`False` e `classificar` retorna um texto)
- Estruturas condicionais: `if`, `elif`, `else`
- Estrutura de repeticao: `while` (menu principal e validaçao das respostas)
- Entrada e saida: `input()` e `print()`

## Autores
- Jonatan Ferreira Angelim
- Aquiles Calixto Guedes
