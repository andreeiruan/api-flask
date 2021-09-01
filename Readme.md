# Api Sicredi

# Como rodar o projeto
* Inicialmente precisa se ter o python 3 instalado na máquina.
* Criamos um ambiente virtual para nosso projeto.
  ```
    python3 -m venv env
  ```
* Após a criação desse ambiente, ativamos ela para instalarmos nossas dependencias e assim deixar nossa máquina "limpa" separando as depêndencias por projeto.
  ```
    source env/bin/activate
  ```
* Após a ativação desse ambiente virtual, instalamos as depedências do projeto que estão no arquivo requirements.txt
  ```
    pip install -r requirements.txt
  ```
* Agora já estamos com nossa máquina configurada para rodar a api, lembre-se que o ambiente virtual precisa estar ativado para rodar com as dependências corretamente, para rodar, execute o segundo comando.
  ```
    FLASK_APP=src/index.py flask run
  ```


# Documentação
  Por padrão o flask rodará na porta 5000, então a url base será <i>http://127.0.0.1:5000</i>

  ## Listagem de maiores devedores
  ## /open_contracts
  ### Query Params
  * top_n (inteiro): Número de contratos à ser retornado.<br>

  ### Resumo
  * Busca de maiores devedores que ainda não possuem seus débitos renegociados.
  A chamada busca os contratos em abertos e os contratos renegociados, verificando então quais os devedores e ordenando do maior para o menor devedor.

  ### Response
  * open_contracts: Lista de todos os contratos.
  * renegotiated_contracts: Lista Com os identificadores de contratos renegociados.
  * top_n_open_contracts: Lista com os identificadores de contratos em aberto, ordenando do maior para o menor

  ## Cálculo de viagens 
  ## /combined_orders
  ### Resumo
  * Busca as viagens com seus valores monetários, e separa essas viagens em pares respeitando o valor máximo monetário permitido por viagem, e retorna o número de viagens necessárias para concluir a lista de viagens.

  ### Response  
  * combined_orders: Número inteiro de viagens necessárias.
  * requests: Lista com os valores monetários de cada viagem.






