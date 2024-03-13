from tkinter import *
from tkinter import ttk
from fpdf import FPDF
from tkinter import filedialog
import os

fonte_comum = ("Arial", 10)

def criar_contrato_locacao(texto_adicional, filename):
    # Função para criar o contrato de locação com as informações fornecidas e texto adicional

    # Obter as informações do locador e locatário dos campos de entrada
    name_locador = entry_locador_nome.get()
    civil_locador = entry_locador_civil.get()
    profi_locador = entry_locador_profissao.get()
    rg_locador = entry_locador_rg.get()
    cpf_locador = entry_locador_cpf.get()
    ender_locador = entry_locador_endereco.get()
    cep_locador = entry_locador_cep.get()

    name_locatario = entry_locatario_nome.get()
    civil_locatario = entry_locatario_civil.get()
    profi_locatario = entry_locatario_profissao.get()
    rg_locatario = entry_locatario_rg.get()
    cpf_locatario = entry_locatario_cpf.get()

    # Cria o objeto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do contrato
    pdf.set_font("Arial", style="B")  # Negrito
    pdf.cell(0, 10, "CONTRATO DE LOCAÇÃO DE IMÓVEL RESIDENCIAL", ln=True, align="C")
    pdf.ln(10)  # Adiciona espaço após o título

    # Define o estilo do texto para o restante do contrato
    pdf.set_font("Arial", size=11)

    # Texto do contrato com as informações fornecidas
    texto_contrato = f"""
    LOCADOR (A): {name_locador} estado civil {civil_locador}, profissão: {profi_locador}, RG nº {rg_locador} e CPF: {cpf_locador} residente e domiciliada em {ender_locador}, CEP:{cep_locador}.\n
    LOCATÁRIO (A): {name_locatario} estado civil {civil_locatario}, profissão: {profi_locatario}, RG nº {rg_locatario} e CPF: {cpf_locatario}, residente e domiciliado (a) no endereço do imóvel objeto do presente contrato.\n
    As partes acima mencionadas, pelo presente contrato particular, ajustam a locação de um imóvel residencial, de acordo com as cláusulas que seguem.\n"""

    # Remover espaços em branco no início e no final de cada linha
    texto_contrato = '\n'.join([linha.strip() for linha in texto_contrato.split('\n')])

    # Adiciona o texto ao PDF sem espaços entre as linhas
    pdf.multi_cell(0, 6, texto_contrato)

    # Adiciona o texto adicional ao PDF
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 6, texto_adicional)

    # Salva o PDF
    pdf.output(filename)
    if os.path.exists(filename):
        print(f"File {filename} created successfully!")
        exit()
    else:
        print(f"Failed to create file {filename}!")


# Função para obter o texto adicional inserido pelo usuário
def obter_texto_adicional():
    texto_adicional = entry_texto_adicional.get("1.0", END)
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if filename:
        criar_contrato_locacao(texto_adicional, filename)

# Criar a janela principal
root = Tk()
root.title("Criar Contrato de Locação")
# Aplicar a fonte comum a todos os elementos de texto
root.option_add("*Font", fonte_comum)

# Criar frame para o locador
frame_locador = Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame_locador.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Rótulos e campos de entrada para as informações do locador
label_locador_nome = Label(frame_locador, text="Nome do Locador:")
label_locador_nome.grid(row=0, column=0, sticky=W)
entry_locador_nome = Entry(frame_locador)
entry_locador_nome.grid(row=0, column=1)

label_locador_civil = Label(frame_locador, text="Estado Civil do Locador:")
label_locador_civil.grid(row=1, column=0, sticky=W)
entry_locador_civil = Entry(frame_locador)
entry_locador_civil.grid(row=1, column=1)

label_locador_profissao = Label(frame_locador, text="Profissão do Locador:")
label_locador_profissao.grid(row=2, column=0, sticky=W)
entry_locador_profissao = Entry(frame_locador)
entry_locador_profissao.grid(row=2, column=1)

label_locador_rg = Label(frame_locador, text="RG do Locador:")
label_locador_rg.grid(row=3, column=0, sticky=W)
entry_locador_rg = Entry(frame_locador)
entry_locador_rg.grid(row=3, column=1)

label_locador_cpf = Label(frame_locador, text="CPF do Locador:")
label_locador_cpf.grid(row=4, column=0, sticky=W)
entry_locador_cpf = Entry(frame_locador)
entry_locador_cpf.grid(row=4, column=1)

label_locador_endereco = Label(frame_locador, text="Endereço do Locador:")
label_locador_endereco.grid(row=5, column=0, sticky=W)
entry_locador_endereco = Entry(frame_locador)
entry_locador_endereco.grid(row=5, column=1)

label_locador_cep = Label(frame_locador, text="CEP do Locador:")
label_locador_cep.grid(row=6, column=0, sticky=W)
entry_locador_cep = Entry(frame_locador)
entry_locador_cep.grid(row=6, column=1)

# Criar frame para o locatário
frame_locatario = Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame_locatario.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Rótulos e campos de entrada para as informações do locatário
label_locatario_nome = Label(frame_locatario, text="Nome do Locatário:")
label_locatario_nome.grid(row=0, column=0, sticky=W)
entry_locatario_nome = Entry(frame_locatario)
entry_locatario_nome.grid(row=0, column=1)

label_locatario_civil = Label(frame_locatario, text="Estado Civil do Locatário:")
label_locatario_civil.grid(row=1, column=0, sticky=W)
entry_locatario_civil = Entry(frame_locatario)
entry_locatario_civil.grid(row=1, column=1)

label_locatario_profissao = Label(frame_locatario, text="Profissão do Locatário:")
label_locatario_profissao.grid(row=2, column=0, sticky=W)
entry_locatario_profissao = Entry(frame_locatario)
entry_locatario_profissao.grid(row=2, column=1)

label_locatario_rg = Label(frame_locatario, text="RG do Locatário:")
label_locatario_rg.grid(row=3, column=0, sticky=W)
entry_locatario_rg = Entry(frame_locatario)
entry_locatario_rg.grid(row=3, column=1)

label_locatario_cpf = Label(frame_locatario, text="CPF do Locatário:")
label_locatario_cpf.grid(row=4, column=0, sticky=W)
entry_locatario_cpf = Entry(frame_locatario)
entry_locatario_cpf.grid(row=4, column=1)

# Criar frame para o texto adicional
frame_texto_adicional = Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame_texto_adicional.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

# Rótulo e caixa de texto para o texto adicional
label_texto_adicional = Label(frame_texto_adicional, text="Cláusulas adicionais:")
label_texto_adicional.grid(row=0, column=0, sticky="w")
entry_texto_adicional = Text(frame_texto_adicional, wrap="word", width=100, height=20)
entry_texto_adicional.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Pré-digitar texto na caixa de texto
texto_add = f"""CLÁUSULA PRIMEIRA:O objeto de locação é o imóvel residencial, localizado na Av. Rei Davi , nº 0000 cidade Paraminas CEP:00000-000.\n
CLÁUSULA SEGUNDA:Oprazo da locação é de 12 meses, tendo início na data da assinatura do presente contrato, ocasião em que é entregue as chaves do imóvel ao (à) LOCATÁRIO (A).\n
PARÁGRAFO PRIMEIRO:Se o (a) LOCATÁRIO (A) desocupar o imóvel antes do prazo estipulado na Cláusula Segunda, ficará obrigado a pagar, a título de multa, o valor equivalente a 3 (três) meses de aluguel, podendo ser isentado a critério do (a) LOCADOR (A) quando da desocupação, mediante termo aditivo expresso e formal.\n
CLÁUSULA TERCEIRA:O valor do aluguel mensal será de R$ 1.000,00 (Um mil reais), que deverá ser pago obrigatoriamente até o dia 20 de cada mês, em moeda corrente e em mãos do (a) LOCADOR (A).\n
PARÁGRAFO PRIMEIRO:Em caso de atraso no pagamento do aluguel no prazo estipulado na Cláusula Terceira, será aplicada automaticamente multa de 3 % (três por cento) sobre o valor do aluguel, juros de mora de 3 % (três por cento) e correção pelo INPC do montante devido.\n
PARÁGRAFO SEGUNDO:O (A) LOCATÁRIO (A) não poderá reter o pagamento do aluguel mensal ou outros encargos, sob a alegação de não atendimento de suas eventuais exigências.\n
CLÁUSULA QUARTA:O atraso no pagamento do aluguel, bem como das despesas ordinárias que incidam sobre o imóvel por mais de 30 dias, serão causa de rescisão do contrato de locação, ficando (a) LOCATÁRIO (A) sujeito a multa equivalente a 1 (Um) mês de aluguel, mais os valores devidos até então.\n
CLÁUSULA QUINTA:Em caso de atraso no pagamento do aluguel será realizada a cobrança por meio de escritório de advocacia, e ficará o (a) LOCATÁRIO (A) sujeito ao pagamento dos honorários advocatícios no valor de 20% (vinte por cento) sobre o valor do débito atualizado, independentemente das multas e demais cominações legais.\n
PARÁGRAFO PRIMEIRO:Os honorários advocatícios de 20% descritos na Cláusula Quinta, se aplicam para qualquer outra medida judicial ou extrajudicial adotada em desfavor do (da) LOCATÁRIO (A).\n
CLÁUSULA SEXTA :O (A) LOCATÁRIO (A) está obrigado a devolver o imóvel nas condições em que recebeu, limpo e conservado, e em pleno funcionamento, ao término do contrato, ainda que rescindido antecipadamente.\n
PARÁGRAFO PRIMEIRO:Caso o imóvel, suas dependências e utensílios nele existentes, não forem restituídos nas mesmas condições, o aluguel e seus acessórios continuarão a correr,até que o (a) LOCATÁRIO (A) cumpra todas as exigências do (a) LOCADOR (A), ficando ainda, sujeito a multa equivalente a 12 (doze) de aluguel.\n
CLÁUSULA SÉTIMA:O (A) LOCATÁRIO (A) declara, que o imóvel ora locado, destina-se única e exclusivamente para o seu uso residencial e de sua família, sendo expressamente proibido sublocar, transferir ou ceder o imóvel, sendo nulo de pleno direito qualquer ato praticado com este fim sem o consentimento prévio e por escrito do (a) LOCADOR (A).\n
CLÁUSULA OITAVA:É vedadoao (à) LOCATÁRIO (A) a colocação de placas, bandeiras, cartazes, painéis, luminosos, antenas, ou quaisquer outras, nas paredes externas do imóvel, sem a prévia e expressa autorização do (a) LOCADOR (A), respondendo pelos danos que forem causados ao imóvelainda que eventualmente autorizado.\n
CLÁUSULA NONA:O (A) LOCATÁRIO (A) obriga-se por si e sua família, a respeitar toda legislação, normas e regulamentos municipais, estaduais e federais, ficando responsável por eventuais multas a que der causa.\n
CLÁUSULA DÉCIMA:O (A) LOCATÁRIO (A), se responsabiliza em zelar pela limpeza e conservação do imóvel, incluída a pintura, sendo vedadas reformas e quaisquer alterações no imóvel sem a prévia e expressa autorização da LOCADORA.\n
CLÁUSULA DÉCIMA PRIMEIRA:Deve o (a) LOCATÁRIO (A) realizar a imediata reparação dos danos causados no imóvel provocados por si, seus dependentes, familiares ou visitantes, vedada a retenção do aluguel.\n
CLÁUSULA DÉCIMA SEGUNDA:O (A) LOCADOR (A) não se responsabiliza por eventuais danos sofridos pelo (a) LOCATÁRIO (A) em caso de acidentes ocasionados por caso fortuito ou de força maior.\n\n
Locador (a):_____________________________________________________________________\n
Locatário (a):_____________________________________________________________________\n
Testemunha:_____________________________________________________________________"""


# Pré-digitar texto na caixa de texto
entry_texto_adicional.insert(END, texto_add)

# Configurar peso das linhas e colunas dentro do frame
frame_texto_adicional.rowconfigure(1, weight=1)

# Botão para criar o contrato de locação
button_criar_contrato = Button(root, text="Criar Contrato de Locação", command=obter_texto_adicional, bg="lightblue", fg="black", font=("Arial", 12, "bold"))
button_criar_contrato.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

# Definir peso das linhas e colunas para ajuste do tamanho dos elementos
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

frame_locador.columnconfigure(1, weight=1)
frame_locatario.columnconfigure(1, weight=1)

# Executar a interface
root.mainloop()
