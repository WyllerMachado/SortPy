# coding=utf-8
from resources.names import MES_ANO


def CONFIRM(working_folder):
    return (f"Os arquivos da pasta:"
            f"\n'{working_folder}'\n"
            f"Serão organizados de acordo "
            f"com os seus tipos.\n\n"
            f"DESEJA CONTINUAR?")


def MOVED(f):
    return f"\n[#] ARQUIVO '{f.file_name}{f.file_extension}' MOVIDO PARA: '{f.category_name}'\n"


def IGNORED(f):
    return f"\n[!] ARQUIVO '{f.file_name}{f.file_extension}' IGNORADO."


def DESTINATION(folder):
    return f"\n[!] OS ARQUIVOS SERÃO MOVIDOS PARA:\n'{folder}'\n"


def EXISTING(folder):
    return f"\n[!] UTILIZANDO PASTA EXISTENTE:\n'{folder}'\n"


def CREATED(folder):
    return f"\n[#] PASTA '{folder}' CRIADA.\n"


def WORKING(folder):
    return f"\n[#] TRABALHANDO NA PASTA:\n'{folder}'\n"


def DRAWN(view):
    return f"\nJANELA DESENHADA: {view}\n"


APP_TITLE = 'Organizador de Pastas'

FACTORY = '\nCRIANDO APLICAÇÃO...\n'

STARTED = '\nAPLICAÇÃO INICIALIZADA.\n'

SELECT_FOLDER = 'Escolha uma pasta bagunçada para organizar:'

DONE = (f"\nPASTA ORGANIZADA!\n"
        f"PRESSIONE OK PARA ABRI-LA.\n\n"
        f"O arquivo de log também abrirá "
        f"para que você possa ver quais "
        f"arquivos foram movidos para "
        f"quais pastas.\n\n"
        f"Tenha um ótimo dia!\n")

EXTS_LOADED = "\nEXTENSÕES CARREGADAS.\n"

CANCELLED = "\nOPERAÇÃO ABORTADA.\n"

CONFIRMED = "\nOPERAÇÃO CONFIRMADA.\n"

FINISHED = '\nOPERAÇÃO FINALIZADA.\n'

SUBDIR_CHECK = f'Organizar arquivos na subpasta "{MES_ANO()}"'

SUBDIR_CHECK_TOOLTIP = "Se desmarcado, os arquivos serão organizados dentro da própria pasta escolhida."

CONFIGURE_TOOLTIP = "Alterar as extensões detectadas pelo programa"

CONFIGURE_HELP = ("\nVocê pode alterar as extensões detectadas "
                  "pelo programa do jeito que quiser!"
                  "\n\n"
                  "Basta alterar o arquivo .json que será aberto "
                  "e salvá-lo.\n"
                  "Em seguida, reinicie o programa."
                  "\n\n"
                  "Você pode criar novas categorias ou alterar "
                  "categorias existentes.\n\n"
                  "(Apenas não altere o nome da categoria ignorados,"
                  " mas sinta-se livre para acrescentar extensões a ela.)\n\n"
                  "Deseja alterar?\n")

INFO_HELP = ("\nOi! Te ajudei de alguma forma?\n"
             "Um café seria legal =)\n\n"
             "Chave PIX: wyllerhacks@gmail.com\n")
