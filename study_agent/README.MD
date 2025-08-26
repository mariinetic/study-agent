
# 📘 Projeto: Agente de Planejamento de Estudos para Geografia (Enem)

## 🎯 Objetivo
Este projeto implementa um **agente de planejamento de estudos** com **Human-in-the-Loop** para a disciplina de Geografia, focado no **ENEM**.  

A ideia é permitir que o usuário:
1. Informe a **dificuldade** de cada tópico.
2. Receba um **cronograma de estudos diário** com base em dificuldade e progresso.
3. Atualize seu **progresso** ao longo dos dias.
4. Receba **lembretes automáticos** no console.

---

## 📂 Estrutura do Projeto

\`\`\`
study_agent/
│
├── app.py                 # Script principal
├── data/
│   └── topics.json         # Base de tópicos de Geografia
├── modules/
│   ├── scheduler.py        # Gera o cronograma com base em prioridade
│   ├── human_input.py      # Recebe dificuldade do usuário
│   ├── reminders.py        # Exibe lembretes no console
│   └── progress.py         # Atualiza progresso de cada tópico
└── README.md               # Documentação do projeto
\`\`\`

---

## 🚀 Como Executar

1. Entre na pasta do projeto:

\`\`\`bash
cd study_agent
\`\`\`

2. Execute o agente de estudos:

\`\`\`bash
python app.py
\`\`\`

---

## 📌 Fluxo de Uso

1. O usuário informa a **dificuldade** de cada tópico (escala de 1 a 5).  
2. O agente gera um **cronograma inicial**, distribuindo as horas disponíveis.  
3. O usuário atualiza o **progresso** (% concluído) ao longo dos dias.  
4. O cronograma é **recalculado automaticamente**, priorizando tópicos mais difíceis e menos concluídos.  
5. O sistema mostra **lembretes diários** no console.  

---

## 📊 Exemplo de Execução

\`\`\`bash
📌 Informe a dificuldade de cada tópico (1 = fácil, 5 = muito difícil):
Questão Ambiental - Impactos ambientais globais: 4
Questão Ambiental - Biomas brasileiros: 3
...

⏰ Lembrete diário de estudo:
1.2h - Questão Ambiental: Impactos ambientais globais
0.8h - Geopolítica: Globalização
1.0h - Espaço Agrário: Conflitos por terra

📌 Informe o progresso de cada tópico (0 a 100%):
Questão Ambiental - Impactos ambientais globais: 20
...

📅 Cronograma atualizado após progresso:
0.9h - Questão Ambiental: Biomas brasileiros
1.1h - Geopolítica: Blocos econômicos
\`\`\`

---

## 🔮 Melhorias Futuras

- Integração com **Telegram/WhatsApp** para envio de lembretes.  
- Interface gráfica (Tkinter/Streamlit).  
- Histórico de estudo salvo por dia.  
- Algoritmo adaptativo que ajusta automaticamente prioridades.  
- Geração de cronograma **completo até a data da prova**.  

---

## 👩‍💻 Autor
Projeto criado para apoiar estudantes no planejamento de estudos de Geografia para o ENEM.  