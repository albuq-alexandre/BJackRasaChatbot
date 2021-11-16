# BJack-Rasa-chatbot-demo
Single Blackjack python chatbot project using Rasa Open Source
  
![Badge](https://img.shields.io/badge/license-MIT-green) 
![Badge](https://img.shields.io/badge/python-v3.8-blue) 
![Badge](https://img.shields.io/badge/Rasa_Open_Source-v2.8.13-blue) 
![Badge](https://img.shields.io/badge/spaCy-v3.1.3-green)
![Badge](https://img.shields.io/badge/spaCy_pt--core--news--md-v3.1.0-orange)

<!--ts-->  Tabela de Conteúdo:
 * [Identificação](#bjack-rasa-chatbot-demo)  
 * [Autores](#disciplina)    
 * [Sobre](#sobre)    
 * [Instalação](#instalação-local)  
 * [Run App](#run-app)
 * [Help](#help)  
 * [Créditos Adicionais](#crditos-adicionais-para-os-projetos)
<!--te-->  
  
  
###  Disciplina 

> *P8902-IANA-Chatbot*  
>**Professor**: Rafael Brasileiro de Araújo  
###  Alunos  
>- **Alexandre de Sousa Albuquerque**
>- **Celso de Melo**
>- **Juliano Ortigoso Gaspar**

## Sobre  

 BJackRasaChatbot é um Chatbot que joga Single BlackJack. Utiliza o Rasa Open Source como NLP e a API do Deck of Cards para o baralho.

## Instalação local

``pip install -r requirements.txt ``

``pip install rasa[spacy]``

``python3 -m spacy download pt_core_news_md``


Para configuração da integração com o telegram, configure a sessão correspondente no arquivo credentials.yml:

``
telegram:
  access_token: "`<bot_token>`"
  verify: "<bot_name>"
  webhook_url: "<https_webhook_url_from_ngrok>/webhooks/telegram/webhook"
``

Use o ngrok para obter uma url https para executar a integração localmente:

``
ngrok http 5005
``

## Run app

Você precisará de 2 terminais para executar o **rasa server** e o **rasa action server**

``rasa run --enable api``

``rasa run actions``

## Help

Utilize linguagem natural, via texto para usar uma das funcionalidades. Use a palavra ***menu*** pra ver:

- **Iniciar:** Inicia o  Jogo ***BlackJack!***;
  - **Mais uma:** durante o jogo, para receber uma carta;
  - **Parar:** para finalizar seu turno.
- **Listar:** Lista suas partidas de BlackJack no jogo atual;
- **Estatística:** Mostra seu percentual de vitórias;
- **Créditos:** Mostra os créditos do projeto;
- **Encerrar:** Quando estiver perdido, diga ***Tchau*** que a gente começa de novo!</i>


## Créditos adicionais para os projetos:
* https://github.com/crobertsbmw/deckofcards
* https://github.com/rafaelbr/MovieBot
* https://github.com/d-Rickyy-b/Python-BlackJackBot
* https://github.com/python-telegram-bot/python-telegram-bot
