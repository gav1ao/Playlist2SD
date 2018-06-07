#encoding: utf-8
import os

print("Insira o caminho da playlist:")
filePath = str(input())

print("Insira o caminho do destino:")
sdPath = str(input())

try:
    file = open(filePath, "r", encoding="utf-8")

    try:
        musics = file.readlines()
    except:
        print("Houve um erro na hora de ler as músicas da playlist.")

    file.close()
    print("Leitura da playlist concluída.")
    erro = []
    try:
        for i in range(2, len(musics), 2):
            mPath = musics[i]
            mPath = mPath.replace('\\', '/')
            mPath = mPath.replace(' ', '\ ')
            try:
                os.system('cp --backup=t /media/vitor/OS' + mPath[2:-1] + ' ' + sdPath)
            except:
                erro.append(str(mPath[2:-1]))
                continue
            #print('cp --backup=t /media/vitor/OS' + mPath[2:-1] + ' ' + sdPath)
            #copy2('/media/vitor/OS' + mPath[2:-1], sdPath)
            #print('/media/vitor/OS' + mPath[2:])

        print("Todas as músicas foram transferidas.")
    except:
        print("Houve erro na hora de transferir as músicas.")
        for m in erro:
            print(m)

except:
    print("Houve um erro na hora de ler a playlist.")


