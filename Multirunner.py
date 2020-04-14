import shutil
import subprocess
import Configuration.config as conf
from colorama import Fore, Style
from tabulate import tabulate


def header():
    head = Fore.RED+r"""
               /|                                        |\
             /  |                                        |  \
           /   <              ,,''''|'''',,               >  \
          |     \         ,,''      |      ``,,         /     |
          |       \    ,''         | |         `,     /       |
           \        \,'            | |           `',/        /
             \     ,'              | |              ',     /
               \_,' Made by        | |                ',_/
                 Stason Jatham    |   |             ____;
                |____~~~---_______|   |_______---~~~____;
                //   ~~~---_______|~-~|_______---~~~   ;\\
              ///;    ,,=====,,,  ~~-~~  ,,,=====,,    ;|\|\
             |/|/   '"          `'     '"          "'   ;|\|
             ||/`;   _--~~~~--__         __--~~~~--_   ;/|\|
             /|||;  :  /       \~~-___-~~/       \  :  ;|\|\
             /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;||\
             |\|;      ~-____--~'  ; ;  '~--____-~      ;\||
             /||;            ,`   ;   ;   ',            ;||\
            |/|\ ;        ,'`    (  _  )    `',        ;/|\||
            /|//|/;    ,'`        ~~ ~~        `',    ;|\\|\|\
           |/||\/||;  '                           '  ;\|/||\|\|
           ///|||/||;         _--~~---~~--_         ;|\||/|\\|\
          |\||/\/|/||;      ,~-------------~,      ;\\|\||/|\\||
         //||\|/|/||/;       ~~~~--------~~~       ;||\\|\|||\/|\
        ||/|/|||/||/;;`;,           -            ;';;\|\\|\\|/|\||
       /|\|/||//|,,`    `;       -- _ --       ;'    `,,|\|\\|\||\\
      ||/||//,,'`         `~--__         __--~`         `',,|\||\\||
     /|||,,'`                   ~~-----~~                   `',,|\|\|
    |,,'`                                                      `',,|
    """ +Fore.YELLOW+"""            
                    ______   _______   _____   ______   
                   |_____/   |_____|     |     |     \  
                   |    \_ . |     | . __|__ . |_____/ .v1.
    """+Fore.WHITE+"""
                   Real Awesome Interactive Destroyer
                    Your network ain't save from us.
    """
    print(head.center(shutil.get_terminal_size().columns))
    print(Style.RESET_ALL)


def tool(toolname: str) -> tuple:
    for tool in conf.toolsdict:
        if tool in toolname:
            return (1,str(toolname))
    return (0,the_helper())


def the_helper():
    print("This is the R.A.I.D. help menu. Even Vikings need help sometimes.")
    toolsdict = conf.toolsdict
    print(Fore.BLUE)
    headers = ['Toolname', 'Description']
    data = sorted([(v,k) for v,k in toolsdict.items()]) # flip the code and name and sort
    print(tabulate(data, headers=headers,tablefmt="github"))
    print(Fore.GREEN + "Per default R.A.I.D. gets target from config file\nYou can overwrite this behavior with typing 'set'")
    print(Style.RESET_ALL)


def attack(toolname):
    run_tool = tool(toolname)
    if run_tool[0]:
        run_tool = run_tool[1]
        try:
            s = subprocess.call(run_tool, shell=True,stderr=subprocess.STDOUT)
            try:
                s = s.decode('latin-1')
            except AttributeError as e:
                print(f'-Error: {e}')
        except subprocess.CalledProcessError as e:
            s = subprocess.call(run_tool, shell=True, stderr=subprocess.STDOUT)
