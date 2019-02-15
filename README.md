# Ranking CTF-BR 2019


## Registro
1. Você deve ter uma conta no GitHub e [configurar uma chave SSH nas suas configurações de conta](https://github.com/settings/keys).

2. Você deve ter um cliente git [corretamente configurado](https://git-scm.com/book/pt-br/v2/Começando-Configuração-Inicial-do-Git). Se você nunca usou git antes, execute:
   ```bash
   git config --global user.name "Fulano de Tal"
   git config --global user.email fulanodetal@exemplo.com.br
   ```

3. Clone o repositório e instale as dependências:
   ```bash
   git clone git@github.com:ctf-br/ranking.git
   cd ranking
   sudo apt-get install libsodium18
   curl https://bootstrap.pypa.io/get-pip.py | sudo -H python
   sudo -H python -m pip install -r pip-requirements.txt
   ```
   **Note**: Se você estiver usando Ubuntu 14.04, adicione [ppa:elt/libsodium](https://launchpad.net/~elt/+archive/ubuntu/libsodium) no seu sistema para poder instalar o `libsodium18`.

4. Se as dependencias estiverem corretamente instaladas, você deve conseguir ver o menu de ajuda executando:
   ```bash
   ./ctf -h
   ```

5. Execute o seguinte comando e seguir as instruções para registrar o time (lembrando que para o ranking interno deve haver um único player por time):
   ```bash
   ./ctf init
   ```


## Challenges

Os challenges estão disponíveis em https://ctf-br.github.io/ranking.

Se você preferir, pode consultar localmente subindo um servidor usando `./ctf serve`, ou listar os challenges na Interface de Linha de Comando:
```bash
./ctf challs
```

## Submissão de flags

Para submeter uma flag:
```bash
./ctf submit --chall chall-id 'CTF-BR{fl4g}'
```

Você pode omitir o `--chall chall-id` do comando, mas vai demorar mais para submeter. Nesse caso, será tentada a flag para cada um dos challenges liberados até então.

## Placar

Se preferir consultar o placar via linha de comando, execute:
```bash
./ctf score --names --pull
```

