para esse projeto funcionar você precisa instalar as dependências, recomendo também criar um ambiente virtual utilizando python.

comando para criação do ambiente virtual, o segundo "venv" é o nome que será dado a pasta, 
você pode escolher, é recomendado algo que lembre um ambiente virtual, venv = VirtualENVironment.

```bash
py -m venv venv
```

comando para iniciar o ambiente virtual, substituir ".\venv" por ".\nome_do_seu_ambiente_virtual" caso você o criou com um nome diferente.
```
.\venv\Scripts\activate
```

comando para instalar os requisitos.
```python
pip install -r requirements.txt
```
rode o programa com
```
py ./manage.py runserver
```

caso encontre um erro relacionado a permissão de Scripts durante a inicialização do ambiente virtual, tente essa solução:

utilize o comando comando abaixo em um terminal powershell **inicializado como admnistrador** para verificar seu "nível de hierarquia" atual nas permissões
```
Get-ExecutionPolicy
```

em seguida, no mesmo terminal, utilize o comando abaixo para mudar o nível de hierarquia para o necessário para executar scripts:
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

em seguida, utilize novamente o primeiro comando para verificar o seu nível de hierarquia, verifique se recebe "RemoteSigned" no terminal:
```
Get-ExecutionPolicy
```

se mesmo após você verificar o nível de hierarquia, receber "RemoteSigned" e ainda assim você não conseguir executar o script para iniciar o ambiente virtual, tente reiniciar o computador, se ainda assim o erro persistir (ou receber um erro diferente) procure uma solução diferente.

para que você possa utilizar a integração com a Gemini você deve obter uma chave para a API [aqui](https://aistudio.google.com/), após isso você deverá criar um arquivo chamado .env na raiz do projeto e dentro dele inserir a chave como no seguinte exemplo: 

```
GEMINI_API_KEY=B2xWq4YTmK98LpRfZ6oCNvJh3A7PiD9EsQr5Ut
```
