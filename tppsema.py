import sys
import os

from sys import argv, exit

import logging

logging.basicConfig(
     level = logging.DEBUG,
     filename = "sema.log",
     filemode = "w",
     format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()


import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from tpplex import tokens

from mytree import MyNode
from anytree.exporter import DotExporter, UniqueDotExporter
from anytree import RenderTree, AsciiStyle

from myerror import MyError

error_handler = MyError('SemaErrors')

root = None

check_tpp = False
check_key = False


## Implementação da Semântica.




# Programa Principal.
def main():
    global check_tpp
    global check_key

    check_ttp = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        # print("Argument #{} is {}".format(idx, arg))
        aux = arg.split('.')
        if aux[-1] == 'tpp':
            check_tpp = True
            idx_tpp = idx

        if(arg == "-k"):
            check_key = True
    
    # print ("No. of arguments passed is ", len(sys.argv))

    if(not check_key and len(sys.argv) < 2):
        raise TypeError(error_handler.newError(check_key, 'ERR-SEM-USE'))
    elif (check_key and len(sys.argv) < 3):
        raise TypeError(error_handler.newError(check_key, 'ERR-SEM-USE'))


    if not check_tpp:
      raise IOError(error_handler.newError(check_key, 'ERR-SEM-NOT-TPP'))
    elif not os.path.exists(argv[idx_tpp]):
        raise IOError(error_handler.newError(check_key, 'ERR-SEM-FILE-NOT-EXISTS'))
    else:
        data = open(argv[idx_tpp])
        source_file = data.read()
        
        # Executar a semântica.


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError):
        print(e)