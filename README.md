Assistente com Memória – Projeto Python
Descrição

Este projeto consiste em um chatbot desenvolvido em Python que utiliza um modelo de linguagem (LLM) para responder perguntas do usuário.
O sistema foi evoluído a partir de uma versão básica de chatbot, adicionando funcionalidades como gerenciamento de memória da conversa, definição de persona do assistente, execução de funções Python e persistência de histórico.

O objetivo principal do projeto é demonstrar como aplicações baseadas em LLM podem integrar memória de conversa, lógica programática e armazenamento de dados.

Como executar o projeto
1. Clonar ou baixar o projeto

Coloque todos os arquivos na mesma pasta.

Estrutura esperada:

projeto04/
│
├── main.py
├── tools.py
├── memoria.json
├── .env
2. Criar o arquivo .env

Dentro do arquivo .env coloque sua chave de API:

GROQ_API_KEY=sua_chave_aqui
3. Instalar dependências

No terminal execute:

python -m pip install openai python-dotenv
4. Executar o chatbot

No terminal:

python main.py

O programa iniciará um chat no terminal onde o usuário poderá conversar com o assistente.

Funcionalidades implementadas
Controle de memória

O chatbot mantém um histórico das mensagens trocadas entre o usuário e o assistente para preservar o contexto da conversa.

Foi implementado também o comando:

/limpar

Esse comando remove todo o histórico da conversa e reinicia a memória do assistente.

Após executar o comando o sistema responde:

Memória da conversa apagada.
Persona do assistente

O assistente possui uma mensagem de sistema que define seu comportamento:

educado

objetivo

levemente bem-humorado

respostas claras e úteis

Essa mensagem é incluída no histórico para orientar o comportamento do modelo.

Limite de memória

Para evitar que o histórico cresça indefinidamente, foi definido um limite de 10 mensagens.

Quando o limite é ultrapassado, as mensagens mais antigas são removidas automaticamente, mantendo apenas o contexto mais recente da conversa.

Integração de funções Python

O assistente também pode executar funções implementadas em Python quando necessário.

Funções implementadas:

1. Data atual

Retorna a data do sistema.

Exemplo:

Hoje é 2026-03-08

2. Cálculo de IMC

O usuário informa peso e altura e o sistema calcula o Índice de Massa Corporal.

Persistência de dados

O histórico de conversa é salvo automaticamente em um arquivo:

memoria.json

Quando o programa é reiniciado, o histórico é carregado novamente, permitindo continuar a conversa anterior.

Reflexão
Se o histórico crescer muito, quais problemas podem ocorrer no uso de LLMs?

Se o histórico de mensagens crescer demais, alguns problemas podem ocorrer:

aumento do consumo de tokens, elevando o custo da API

respostas mais lentas devido ao maior volume de dados enviado ao modelo

possibilidade de ultrapassar o limite máximo de contexto do modelo

dificuldade do modelo em focar nas partes mais relevantes da conversa

Por isso é comum implementar limites de memória ou mecanismos de resumo de histórico em aplicações que utilizam LLMs.

Por que algumas tarefas são melhores resolvidas por funções Python do que pelo próprio LLM?

Algumas tarefas são mais adequadas para execução direta em código porque:

cálculos matemáticos são mais precisos em código

operações com datas são mais confiáveis

geração de valores aleatórios é melhor controlada

processamento de dados estruturados é mais eficiente

LLMs são excelentes para linguagem natural, mas não são ideais para executar operações determinísticas ou cálculos precisos.

Quais riscos existem ao deixar que o LLM tome decisões sobre quando usar uma função?

Permitir que o LLM decida automaticamente quando usar funções pode gerar alguns riscos:

execução de funções incorretas

chamadas desnecessárias de funções

possíveis falhas de segurança caso funções sensíveis estejam disponíveis

comportamento imprevisível em certos tipos de pergunta

Por esse motivo, em sistemas mais complexos é comum utilizar validação adicional ou regras de controle para garantir que funções sejam chamadas apenas quando apropriado.

Dificuldades encontradas

Durante o desenvolvimento do projeto algumas dificuldades foram encontradas:

configuração correta da API do modelo de linguagem

gerenciamento do histórico de mensagens

implementação do limite de memória sem remover a mensagem de sistema

integração entre o chatbot e funções Python externas

Esses desafios ajudaram a compreender melhor como funcionam aplicações baseadas em LLMs e como gerenciar o estado de uma conversa.

Conclusão

O projeto demonstrou como um chatbot simples pode evoluir para uma aplicação mais completa com memória, execução de funções e persistência de dados. Essas técnicas são amplamente utilizadas em assistentes virtuais e sistemas modernos baseados em inteligência artificial.
