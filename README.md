
# 📘 Projeto: Agente de Planejamento de Estudos para Geografia (Enem)

## 🎯 Objetivo
Este projeto implementa um **agente de planejamento de estudos** com **Human-in-the-Loop** para a disciplina de Geografia, focado no **ENEM**.  

A ideia é permitir que o usuário:
1. Informe a **dificuldade** de cada tópico.
2. Receba um **cronograma de estudos diário** com base em dificuldade e progresso.
3. Atualize seu **progresso** ao longo dos dias.

---

## 📌 Fluxo de Uso

1. O usuário informa a **dificuldade** de cada tópico (escala de 1 a 5).  
2. O agente gera um **cronograma inicial**, distribuindo as horas disponíveis.  
3. O usuário atualiza o **progresso** (% concluído) ao longo dos dias.  
4. O cronograma é **recalculado automaticamente**, priorizando tópicos mais difíceis e menos concluídos.  
5. O sistema mostra **lembretes diários** no console.  

---

## 📊 Exemplo de Execução

```bash
📌 Informe a dificuldade de cada tópico (1 = fácil, 5 = muito difícil):
Questão Ambiental - Impactos ambientais globais: 4
Questão Ambiental - Biomas brasileiros: 3
...

📌 Informe o progresso de cada tópico (0 a 100%):
Questão Ambiental - Impactos ambientais globais: 20%
...

📅 Cronograma atualizado após progresso:
0.9h - Questão Ambiental: Biomas brasileiros
1.1h - Geopolítica: Blocos econômicos
```
---

## 👩‍💻 Autor
Projeto criado para apoiar estudantes no planejamento de estudos de Geografia para o ENEM.  
