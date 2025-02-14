import os
import pylatex
import pylatex.config

from datetime import datetime


def gerar_informacoes(doc: pylatex.Document, empresa: str, email: str, celular: str, funcionario: str):
    with doc.create(pylatex.Tabular("|p{16cm}|")) as table:
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Nome da empresa:}")])
        table.add_row([empresa])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{E-mail para contato:}")])
        table.add_row([email])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Celular para contato:}")])
        table.add_row([celular])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Nome do funcionário:}")])
        table.add_row([funcionario])
        table.add_hline()

def gerar_erro(doc: pylatex.Document, codigo: str, data: str, hora: str, linha: str, tipo: str, imagem: str):
    with doc.create(pylatex.Tabular("|p{16cm}|")) as table:
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Código do erro:}")])
        table.add_row([codigo])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Data:}")])
        table.add_row([data])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Hora:}")])
        table.add_row([hora])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Linha:}")])
        table.add_row([linha])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Tipo de maquininha:}")])
        table.add_row([tipo])
        table.add_hline()
        table.add_row([pylatex.NoEscape("\\textbf{Imagem do erro:}")])
        image_path = imagem.replace("\\", "/")
        table.add_row([pylatex.NoEscape(f"\\includegraphics[width=12cm]{{{image_path}}}")])
        table.add_hline()

def gerar_pdf(funcionario: str, erros: list[dict]):
    pylatex.config.active = pylatex.config.Version1(indent=False)

    geometry_options = {"tmargin": "3cm", "lmargin": "3cm", "bmargin": "2cm", "rmargin": "2cm"}
    file_name = str(len(erros)) + "_" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    file_path = os.path.join(os.path.dirname(__file__), "relatorios", file_name)
    doc = pylatex.Document(file_name, geometry_options=geometry_options)

    doc.preamble.append(pylatex.Package('graphicx'))

    gerar_informacoes(doc, "Detectoy", "detectoy@detectoy.com.br", "+55 (92) 99999-9999", funcionario)

    doc.append(pylatex.VerticalSpace("0.5cm"))
    doc.append(pylatex.LineBreak())

    for erro in erros:
        gerar_erro(doc, erro["codigo"], erro["data"], erro["hora"], erro["linha"], erro["tipo"], erro["imagem"])
        doc.append(pylatex.NewPage())

    doc.generate_tex(filepath=file_path)
    doc.generate_pdf(filepath=file_path)
    return file_name + ".pdf"

if __name__ == "__main__":
    erro = {
        "codigo": "TIPO-LINHA_YYYY-MM-DD-HH-MM-SS-mmmm",
        "data": "DD/MM/YYYY",
        "hora": "HH:MM:SS.mmmm",
        "linha": "LINHA",
        "tipo": "TIPO",
        "imagem": os.path.join(os.path.dirname(__file__), "images/erro.jpg")
    }
    gerar_pdf("Fulano de Tal", [erro])
