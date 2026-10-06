from flask import Flask, render_template, request

app_Estephany = Flask(__name__,template_folder='t_templates')  #cria o objeto Flask, que Ã© a aplicaÃ§Ã£o web, e define a pasta templates como pasta de templates


@app_Estephany.route('/ola')
def raiz():   #esta funÃ§Ã£o estÃ¡ vinculada a rota  /ola
    return render_template('homepage.html')  #retorna o arquivo index.html que estÃ¡ na pasta templates

#veja que o id Ã© um parÃ¢metro da rota e faz parte da URL, e nÃ£o vai confundir com a rota /ola
@app_Estephany.route('/ola/<id>') 
def saudacao(id):
   return render_template('homepage_nome.html', campoNome= id) 
   #retorna o arquivo homepage.html que estÃ¡ na pasta templates. No .html tem o campo {{campoNome}} que vai receber o valor do parÃ¢metro id da rota


#@app_Estephany.route('/ola/<id>')
#def saudacao():
#    nome = request.args.get("id")
#    return render_template('homepage_nome.html', campoNome= nome) #retorna o arquivo homepage.html que estÃ¡ na pasta templates

@app_Estephany.route('/')
@app_Estephany.route('/index')
def index():   #esta funÃ§Ã£o estÃ¡ vinculada a rota raÃ­z / e rota /index
    return render_template('t_index.html', nome ="Turma 2025") 

@app_Estephany.route('/contato')
def contato():
    return render_template('t_contato.html')  

@app_Estephany.route('/usuario')
def dados_usuario():
    #nome_usuario="Mariela"
    dados_usu = {"nome": "Mariela", "profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("t_usuario.html", dados = dados_usu)
                                           #parÃ¢metro recebe argumento
                                           #colocar o site no ar

@app_Estephany.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {"nome": p_nome, "profissao": p_profissao, "disciplina": p_disciplina}
    return render_template("usuario.html", dados = dados_usu)

@app_Estephany.route('/login')
def login():
    return render_template("t_login.html")

#esta funÃ§Ã£o nÃ£o estÃ¡ vinculado a rota, mas pode ser usada dentro de uma rota ou outra funÃ§Ã£o ou invocada de fora
def saudacaoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

#maiores detalhes nos slides que estÃ£o no AVA.
if __name__ == '__main__':  #verifica se o arquivo estÃ¡ sendo executado diretamente, e nÃ£o importado
    app_Estephany.run(port=7000)

app_Estephany.run( port=6000)    #executa caso o o arquivo seja importado, mas nÃ£o Ã© uma boa prÃ¡tica, pois pode gerar conflito de portas
