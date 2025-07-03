# ChatbotAI

## Instruções do Agente

- Este agente conversacional foi desenvolvido para responder perguntas relacionadas ao curso de Sistemas de Informação, utilizando uma base de conhecimento construída a partir dos planos de ensino e documentos oficiais do curso;

    - O agente deve responder somente com base na base de conhecimento fornecida, evitando respostas especulativas ou “alucinações”;

    - As perguntas são enviadas via interface frontend, que se comunica com o backend através da API RESTful;

    - A autenticação na API é feita via chave de API, que o usuário insere na interface frontend e é enviada no header `X-API-Key` nas requisições ao backend;

    - As respostas retornam em formato JSON contendo a resposta gerada ou mensagens de erro, caso haja problemas na requisição;

    - O sistema foi desenvolvido com foco em garantir precisão, clareza e confiabilidade nas respostas, respeitando os limites de uso da API do Google Gemini;

### Guia de como iniciar o Agente
    -git clone https://github.com/wilmarconsilva/ChatbotAI
    -cd ChatbotAI

    - Criar ambiente virtual:
    - python3 -m venv venv
    - source venv/bin/activate  # Linux/macOS
    - venv\Scripts\activate     # Windows

    - Instalar dependencia:
    - pip install -r requirements.txt

    - Se não existir o requirements.txt, crie-o com o conteúdo: "pip install flask streamlit google-generativeai"

    - Para iniciar o backend, siga as instruções:

      Acessar a pasta cd Backend e execute o comando "python3 app.py"
     
    - Para iniciar o frontend,  siga as instruções:
      
      Acessar a pasta cd Frontend e execute o comando "python3 -m streamlit run app.py"

    - Após acessar o site, no canto superior direito, terá um botão em forma de engrenagem, após clicar, deverá ser inserido a API KEY, crucial para o funcionamento do chat bot .

    -Agora, realize perguntas, que em questão de segundos, será respondido.

## Pré-requisitos

- Python 3.10 ou superior
- Conta no Google com acesso à API Gemini (https://aistudio.google.com/app/apikey)
- Navegador moderno (Google Chrome, Firefox, etc.)
- Git instalado

## Diário de Bordo de Contribuições


### Wilson - Engenheiro de Dados

#### Semana 1

- Criação do grupo no WhatsApp para definição das demandas e responsabilidades;

- Criação do repositório no GitHub;

- Levantamento das informações a serem tratadas;

    - Informações a serem tratadas:
        - Planos de Ensino do Curso de Sistemas de Informação:
            1. Administração e Gerência de Redes  
            2. Algoritmos e Estrutura de Dados  
            3. Algoritmos e Lógica de Programação  
            4. Aplicações Distribuídas  
            5. Arquitetura de Computadores  
            6. Banco de Dados 1  
            7. Banco de dados 2  
            8. Carreira e Certificação  
            9. Ciência de Dados  
            10. Contabilidade Básica  
            11. Engenharia de Software  
            12. Estatistíca  
            13. Fundamentos Antropológicos e Sociologicos  
            14. Fundamentos ao Desenvolvimento Web  
            15. Fundamentos da Administração  
            16. Fundamentos de Matemática Discreta  
            17. Gerência da Infraestrutura de TI  
            18. Gerência de Projetos  
            19. Gestão da Sustentabilidade  
            20. Governança de TI  
            21. Inteligência Artificial  
            22. Inteligência de Negócios  
            23. Interação Humano Computador  
            24. Introdução ao Hardware  
            25. Linguagem e Método Científico  
            26. Modelagem de Processos  
            27. Modelagem de Sistemas  
            28. Pesquisa Operacional  
            29. Prática Integrada 1  
            30. Prática Integrada 2  
            31. Prática Integrada 3  
            32. Princípios e Aplicações da Computação  
            33. Programação 1  
            34. Programação 2  
            35. Programação 3  
            36. Qualidade de Software  
            37. Redes de Computadores  
            38. Segurança e Auditoria de Sistemas  
            39. Sistemas Operacionais  
            40. Trabalho de Conclusão de Curso 1  
            41. Ética e Cidadania  

        - Projeto Pedagógico do Curso Sistemas de Informação.

#### Semana 2 

- Tratamento das informações;
- Criação do arquivo MarkDown com a base de conhecimento do Chatbot.

### Gabriel Lunelli - Desenvolvedor Frontend

#### Semana 1

- Discussão no grupo acerca das atribuições de cada membro e a definição da responsabilidade pelas interfaces;
- Clone do repositório git;

#### Semana 2

- Estudo da plataforma Streamlit;
- Obtenção das rotas que serão chamadas;
- Definição do fluxo das interfaces;
- Desenvolvimento das interfaces;
- Comando para rodar a aplicação: streamlit run app.py

### Saulo Benedetti - Desenvolvedor Backend

#### Semana 1

- Participação nas discussões iniciais do grupo para definição do escopo e das responsabilidades de cada integrante.
- Análise dos requisitos para o backend, focando na integração com a API do Google Gemini e na lógica de comunicação com o frontend.
- Desenvolvimento da estrutura inicial do servidor backend utilizando Python e Flask.
- Criação da primeira versão do endpoint ``POST /perguntar``, capaz de receber e processar requisições.
- Projeto do "cérebro" do agente: elaboração do prompt de sistema com as diretrizes de comportamento, incluindo a regra crucial para não "alucinar" e responder apenas com base no conteúdo fornecido.

#### Semana 2

- Realização de uma chamada de alinhamento com a equipe para definir a arquitetura final de autenticação da API.
- Com base na decisão da equipe, refatorei o backend para adotar o modelo de chave de API via header (``X-API-Key``), onde o usuário final fornece sua própria chave na interface.
- Depuração (debugging) e otimização da comunicação com a API do Gemini, resolvendo erros de status ``404 (Not Found)`` e ``429 (Quota Exceeded)``.
- Finalização da documentação da API para o Desenvolvedor Frontend, detalhando o endpoint, método, headers, corpo da requisição e os possíveis formatos de resposta (sucesso e erro).


### Lucas Miotto Siarpinski - Gerente de Projetos e QA

#### Semana 1

- Contribuição nas reuniões iniciais do grupo para estabelecer o escopo do projeto e definir as responsabilidades de cada membro.
- Acompanhei o processo de entregas do que ia sendo conversado durante a semana no grupo do WhatsApp.
#### Semana 2

- Acompanhamento da atividade no grupo.
- Realização de testes para averiguar o funcionamente do AgenteIA.
- Atualização do arquivo README com guias e instruções claras de como funciona o sistema.
- Documentação dos testes realizados.


## Garantia da Qualidade (QA)

#### Planejamento de Testes e Validação
-A seguir está a lista com perguntas-chave criadas com base nas disciplinas do curso de Sistemas de Informação da UNOESC Chapecó. Essas perguntas foram utilizadas para validar o chatbot FAQ com base na base de conhecimento oficial.

- Cada pergunta foi classificada como Correta, Parcial ou Incorreta após a comparação da resposta gerada com o conteúdo programático das disciplinas.

- link da planilha: https://docs.google.com/spreadsheets/d/1DFPyT9kk7VqowkOFtXk4ebkwjg3pW0MqmuXpiddmHkw/edit?usp=sharing

