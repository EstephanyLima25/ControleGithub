from flask import Flask, render_template
from flask import request   #para trabalhar com os mÃ©todos GET e POST
from flask import flash     #para msgs popup
from flask import redirect  #para redirecionar pÃ¡ginas


# os templates coloca em outra pasta. 
# Por padrÃ£o, fica na pasta templates e nÃ£o precisa informar no template_folder,
# mas se quiser armazenar em outra pasta indique nesse parÃ¢metro.
app_Estephany = Flask(__name__, template_folder='t_templates') 
# no caso de usar flash pede a configuraÃ§Ã£o de uma chave secreta
app_Estephany.config['SECRET_KEY'] = "palavra-secreta-IFRO"


@app_Estephany.route("/")       #se no navegador digitar / ou /index
@app_Estephany.route("/index")  
def index():
    return render_template ("t_index.html") #optei por prefixar com t_ os nomes dos arquivos que usam template

@app_Estephany.route("/contato")
def contato():
    return render_template("t_contato.html") 

#rota /usuarios COM passagem de argumentos
@app_Estephany.route("/usuario/<nome_usuario>;<nome_profissao>")
#rota /usuarios SEM passagem de argumentos --> definir valor padrÃ£o com defaults
@app_Estephany.route("/usuario", defaults={"nome_usuario":"usuÃ¡rio?","nome_profissao":""})  

def dados_usuario (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

#new
@app_Estephany.route("/login")
def login():
    return render_template("t_login_flash_js_cadastro.html")
    
#new
"""++++
Para poder recuperar os argumentos passados nos parÃ¢metros na URL precisa importar o pacote
from flask import request

TambÃ©m precisa colocar que essa pÃ¡gina aceita requisiÃ§Ãµes de tipo GET ou POST
O GET Ã© padrÃ£o, mas no caso do POST altere no html method="POST"
"""
@app_Estephany.route("/autenticar", methods=['GET', 'POST']) 
def autenticar():
    #mÃ©todo POST - pega nos fields (campos) do formulÃ¡rio
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    
    if usuario == "admin" and senha == "ifro":
        return f"usuario: {usuario} e senha: {senha}"
    else:
        #para nÃ£o dar msg. na outra pÃ¡gina, vamos manter na prÃ³pria pÃ¡gina com flash
        #adicionar import flash
        flash("Dados invÃ¡lidos!")
        flash("Login ou senha invÃ¡lidos!")
        return redirect ('/login') #adicionar import redirect


if __name__ == "__main__": 
     app_Estephany.run(port = 8000) 
     
