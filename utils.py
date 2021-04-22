validChars = ":-0123456789AÃÁÂÀBCÇDEÉÊFGHIÎÍJKLMNOÕÓÔPQRSTUÚÛVWXYZaãáâàbcçdeéêfghiíîjklmnoóôõpqrstuúûvwxyz\0"
letters = "-.AÃÁÂÀBCÇDEÉÊFGHIÎÍJKLMNOÕÓÔPQRSTUÚÛVWXYZaãáâàbcçdeéêfghiíîjklmnoóôõpqrstuúûvwxyz"
numbers = "0123456789"


def processBinFile(fqfn, dic, codepage):
    word = ''
    f = open(fqfn, "rb")
    c = f.read(1)
    while c != b'':
        if c == b'\n' or c == b'\t':
            word = word.strip().lower()
            if len(word) > 1 and not(word in dic.keys()):
                dic[word] = {'type': "''"}
            word = ''
        try:
            c = c.decode(codepage)
        except:
            c = ' '
        if not (c in letters):
            c = ' '
        word = word + c
        c = f.read(1)
    f.close()
    return dic


def printSubstantives(d):
    f = open("substantivos.py", "w", encoding='utf-8')
    f.write('# Para uso futuro está reservado um campo para o tipo de substantivo:\n')
    f.write('# SNS - Substantivo neutro sigular\n')
    f.write('# SNP - Substantivo neutro plural\n')
    f.write('# SMS - Substantivo masculino singular\n')
    f.write('# SMP - Substantivo masculino plural\n')
    f.write('# SFS - Substantivo feminino singular\n')
    f.write('# SFP - Substantivo feminino plural\n')
    f.write('# A lista de substantivos foi aproveitada do projeto Liguateca:\n')
    f.write('# https://www.linguateca.pt/acesso/contabilizacao.php\n')
    f.write('#\n')
    f.write('substantivos = {' + '\n')
    for subs in d.keys():
        f.write('\t' + subs + ':{' + '\n')
        for field in d[subs]:
            f.write("\t\t\t" + field + ":" + str(d[subs][field]) + "," + "\n")
        f.write('\t' + '},' + '\n')
    f.write('}' + '\n')
    f.close()
