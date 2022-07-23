#Arquivos em Python
#O Python possui algumas funções prontas para manipular arquivos binários puros (onde, conhecendo a estrutura interna de qualquer formato, podemos salvar qualquer tipo de arquivo) e para manipular arquivos de texto (onde os binários são decodificados como strings).

#Focaremos no básico de manipulação de arquivo de texto, pois, na prática, quando formos trabalhar com arquivos mais complexos, é provável que usaremos bibliotecas específicas para lidar com eles, e elas já terão funções próprias para ler e salvar esses arquivos da maneira correta.

#Abrindo e fechando arquivos
#Podemos criar arquivos novos ou abrir arquivos já existentes utilizando a função open. Ela possui 2 argumentos: uma com o caminho do arquivo e outra com o modo de operação.

#Modo	Símbolo	Descrição
#read	r	lê um arquivo existente
#write	w	cria um novo arquivo
#append	a	abre um arquivo existente para adicionar informações ao seu final
#update	+	ao ser combinado com outros modos, permite alteração de arquivo já existente (ex: r+ abre um arquivo existente e permite modificá-lo)
#Após abrirmos (ou criarmos) um arquivo, podemos realizar diversas operações. Ao final de todas elas, devemos fechar o nosso arquivo usando a função close. Essa etapa é importante por 2 motivos:

#Se alteramos o arquivo mas não o fechamos, as alterações não serão salvas.
#Se esquecermos de fechar um arquivo, outros programas podem ter problemas de acesso a ele.
#Roteiro básico
#Vamos seguir os seguintes passos para manipular nossos arquivos:

# 1) Abrir ou criar um arquivo:

arquivocriado = open("criado.txt", "w")
# a linha acima abre (ou cria se não existe) um arquivo chamado "exemplo.txt" para escrita ("w", de write) e guarda na variável
# "arquivo" as informações para manipulá-lo

arquivolido = open("teste.txt", "r")
# a linha acima lê ("r", de read) um arquivo já existente chamado exemplo2.txt e guarda em
# "arquivolido" as informações para manipulá-lo

# 2) Carregar os dados do arquivo (leitura)
dados = arquivolido.read()
print(dados)
# read() retorna todo o conteúdo do arquivo como uma string
# Precisamos carregar o conteúdo do arquivo para variáveis, em algum formato
# que sabemos trabalhar. A read() carrega o conteúdo de um arquivo de texto
# em uma string.

# 2) Manipular os dados do arquivo (escrita)

arquivocriado.write("teste")
arquivocriado.write("teste2")
arquivocriado.write("teste3")
# Em casos mais complexos, iremos manipular o conteudo LIDO no passo anterior
# para posteriormente reescrevê-lo.
# Em outros mais simples, podemos escrever diretamente no arquivo.

# 3) Fechar o arquivo

arquivocriado.close()
arquivolido.close()

# Essa etapa é muito importante para garantir a integridade dos novos dados
# no arquivo.
# Ao fechar é que todas as modificações são salvas.


# Um jeito mais inteligente de trabalhar com arquivos é utilizar a sintaxe do "with":

with open('teste.txt', 'r') as arquivolido:
   dados = arquivolido.read()
   print(dados)

# É possível ler o arquivo linha a linha:

with open('teste.txt', 'r') as arquivolido:
   linha = arquivolido.readline()
   print(linha)
   linha = arquivolido.readline()
   print(linha)

with open('teste.txt', 'r') as arquivolido:
    for linha in arquivolido:
        print(linha, end='')

# O mesmo pode ser feito para escrever no arquivo:

with open('teste.txt', 'r') as arquivolido:
    with open('copiateste.txt', 'w') as arquivocriado:
        for linha in arquivolido:
            arquivocriado.write(linha)