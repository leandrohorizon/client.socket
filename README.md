## sobre
essa biblioteca serve para facilitar a conversação com os robôs Jargo, ela também possibilita criar métodos que serão executados pelos robôs

## exemplo de uso
  ```python
    # nickname é o apelido definido na criação do seu robô
    bot = Robot(nickname='jargo')
    
    # aqui estamos definindo um método para o robô executar
    @bot.exec(name='hello_world')
    def hello_world(arguments):
      print('hello world')
    
    # para enviar uma mensagem para o seu robô é só
    bot.speak('Olá')
    resposta = bot.get_response()
    print(f'resposta: {resposta}')
    # resposta: olá amigo
    
    # para executar os processos
    bot.execute_procedures()
```
