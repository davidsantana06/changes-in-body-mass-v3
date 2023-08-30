# Changes in body mass V3

**PT-BR**

Este repositório representa a última versão do projeto "Changes in Body Mass", correspondente à terceira avaliação da disciplina de Complexidade de Algoritmos do curso de Sistemas de Informação. Nesta versão, foi considerado o segundo cenário da iteração anterior, onde ocorre uma divisão de processamento entre a nuvem e a borda. Entre os novos recursos implementados, destaca-se a adição de uma fonte de aleatoriedade real obtida a partir da extração de ondas sonoras de streaming de  músicas, simulada por meio de um arquivo de áudio no formato MP3. Além disso, todas as transmissões de dados são criptografadas e acompanhadas por sua respectiva chave para a decodificação.
<br /><br /><br />


**EN-US**

This repository represents the latest version of the "Changes in Body Mass" project, corresponding to the third assessment of the Complexity of Algorithms course in the Information Systems program. In this version, the second scenario from the previous iteration was considered, where processing is divided between the cloud and the edge. Among the new implemented features, a notable addition is the incorporation of a real randomness source obtained from the extraction of audio waves from music streaming, simulated through an MP3 audio file. Additionally, all data transmissions are encrypted and accompanied by their respective decryption keys.
<br /><br /><br />



## :rocket: Funcionalidades

1. **Simulação de Dados de Alunos via Threads**: A aplicação gera informações completas para 10 alunos que acabaram de se matricular em uma academia. Para otimizar esse processo, a utilização de threads possibilita a geração simultânea e eficiente desses dados.
  
2. **Geração Aleatória com Ondas Sonoras da Playlist**: A geração de dados dos alunos é enriquecida com aleatoriedade autêntica, utilizando as ondas sonoras de uma playlist como fonte de variação. Isso resulta em informações mais diversificadas e realistas.

3. **Criptografia dos Dados para Nuvem**: Antes de serem enviados para a nuvem (representada pela instância principal da aplicação), os dados dos alunos passam por um processo de criptografia. Isso garante que as informações sensíveis permaneçam protegidas e privadas durante o armazenamento e a transferência.
 
4. **Gráfico de Pesos e Médias**: A aplicação cria um gráfico visual que exibe o peso atual de cada aluno, permitindo um acompanhamento fácil do seu progresso. Além disso, o gráfico também inclui a média das pesagens, fornecendo uma visão geral do desempenho médio dos alunos.
  
5. **Serialização Excel dos Dados de Pesagem**: Os registros de pesagem dos alunos são organizados e armazenados em um formato Excel. Isso possibilita uma análise mais detalhada dos dados ao mesmo tempo que oferece a flexibilidade de utilização em outras ferramentas para estudo e acompanhamento.
<br /><br /><br />


## :page_with_curl: Documentação

Para obter uma perspectiva concreta a respeito deste projeto, incluindo as funcionalidades introduzidas desde a primeira versão, é possível visualizar o documento de apresentação, Changes in Body Mass, disponível via <a href="https://docs.google.com/document/d/1-KEnZwSp1JcZXZn-oJHdjesLoqmEKVqvjtuSPFXiMW8">Google Docs</a>.
<br /><br /><br />



## :computer: Pré-requisitos

Para executar a aplicação, é necessário instalar seis bibliotecas, além da linguagem de programação Python 3. O repositório inclui um arquivo chamado `requirements.txt` que contém todas as bibliotecas necessárias. Portanto, ao baixar ou clonar o repositório e abrir o terminal da sua IDE na pasta raiz do projeto, basta inserir o seguinte comando:

```terminal
pip3 install -r requirements.txt
```

Em seguida, execute o arquivo `src\main.py` e inicie a interação com o terminal.