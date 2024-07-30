import os
import re
import subprocess

import automatic_code_review_commons as commons

def __check_regex_ignore(regexs, name):
    for regex in regexs:
        if re.search(regex, name):
            return True

    return False

def __comparar_formatacao(arquivo, texto):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            conteudo_arquivo = file.read()
        
        linhas_arquivo = conteudo_arquivo.splitlines()
        linhas_texto = texto.splitlines()

        if len(linhas_arquivo) != len(linhas_texto):
            return False
        
        for linha_arquivo, linha_texto in zip(linhas_arquivo, linhas_texto):
            if linha_arquivo.strip() != linha_texto.strip():
                return False
        
        return True
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False
    

def __verificar_indentacao_arquivo(arquivo, config):
    comando = [config['command']] + config['arguments'] + [arquivo]
    
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return __comparar_formatacao(arquivo, resultado.stdout)


def review(config): 
    path_source = config['path_source']
    regex_file = config['regexFile']
    regex_ignore = config['regexIgnore']
    

    comments = []

    for root, _, files in os.walk(path_source):
        for file in files:
            file_path = os.path.join(root, file)

            if re.search(regex_file, file_path) and not __check_regex_ignore(regex_ignore, file):
                qml_format = config['qmlFormat']
                
                if not __verificar_indentacao_arquivo(file_path, qml_format):
                    relative_path = file_path.replace(path_source, "")[1:]
                    descr_comment = config['message']
                    descr_comment = descr_comment.replace("${FILE_PATH}", relative_path)
                    
                    comments.append(
                        commons.comment_create(
                            comment_id=commons.comment_generate_id(file_path),
                            comment_path=relative_path,
                            comment_description=descr_comment,
                            comment_snipset=False,
                            comment_end_line=1,
                            comment_start_line=1,
                            comment_language="QML"
                        ))

    return comments