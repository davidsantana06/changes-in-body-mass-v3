from os.path import abspath, dirname

# Diretório com a pasta raiz do projeto
ROOT_FOLDER = dirname(abspath(__file__)).replace('\\', '/') + '/..'

# Indicadores para ganho e perda de peso
GAIN = '(+)'
LOSE = '(-)'

# Limite de pessoas do mini mundo
PERSON_LIM = 10

# Limite de casas decimais para os valores numéricos
ROUND_LIM = 1
