#Gravando informações em arquivos: 
#As linhas comentadas funcionam da mesma forma, porém a forma
#não comentada é mais 'pythonica'

#arq = open('arquivo.txt','w')

texto = '''
Aprendendo python
machine learning
python é muito legal
Agora com équio!!!
'''

with open('arquivo.txt', 'w') as f:
    f.write(texto)


#arq.write(texto)
#arq.write('machine learning')
#arq.write('\naprendando python')
#arq.close