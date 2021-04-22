import utils

dic = {}
dic = utils.processBinFile("lista.lemas.total.N.txt", dic, 'Windows-1252')
dic = utils.processBinFile("lista.formas.total.N.txt", dic, 'Windows-1252')
utils.printSubstantives(dic)
