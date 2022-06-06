import re


class Clase_Lexemas:

    def __init__(self,texto):
        self.estado = []
        self.texto = texto

    def getValor(self):
        return self.estado

    def iniciar(self):
        numlinea=0 
        error=0
        totlineas=len(self.texto)

        NUL=re.compile('[0-9]*[\.][-] ')
        IDS=re.compile('[a-z|_][a-z|_|0-9]*')   #Identificadores
        NOI=re.compile('[^a-z][0-9][0-9]*[0-9]*')   #Números enteros
        NOF=re.compile('[0-9][0-9]*[\.][0-9][0-9]*')    #Números flotantes
        OPR=re.compile('[<][=]|[>][=]|[=][=]|[!][=]|[<]|[>]')   #Operadores relacionales
        OPA=re.compile('[\+]|[^.][\-]|[\*]|[\/]|[\%]|[\^]')         #Operadores aritmeticos 
        PAL=re.compile('[F][I][N][D][E][S][D][E]|[E][N][T][O][N][C][E][S]|[D][E][S][D][E]|[H][A][S][T][A]|[I][N][C][R][E][M][E][N][T][O][S]|[E][N]|[H][A][S][T][A][Q][U][E]|[F][I][N][H][A][S][T][A][Q][U][E]|[M][I][E][N][T][R][A][S][Q][U][E]|[F][I][N][M][I][E][N][T][R][A][S]|[S][I]|[I][N][I][C][I][O]|[F][I][N]|[P][E][D][I][R]|[H][A][C][E][R]|[M][O][S][T][R][A][R]') #Palabras reservadas
        OAS=re.compile('[\w][=][\w]|[ ][=][ ]')  #Operador de asignación
        SEP=re.compile('[\s][,]|[,][\s]|[,]')  #Operador de separación
        PAR=re.compile('[(]|[)]')  #Paréntesis
        TEX=re.compile('[\"].+[\"]')  #Texto
        self.estado.append("------------------------------------------------------------------")
        self.estado.append("  Patron ->  Descripción             Posicion      Cadena ")
        self.estado.append("                                                Inicial | Final")
        self.estado.append("------------------------------------------------------------------")

        for x in range(len(self.texto)):
            txt=self.texto[x]
            revisando=list(txt[:])
            numlinea=numlinea+1
            self.estado.append("")
            self.estado.append(txt)
            
            #Número de línea
            if NUL.search(txt):
                result=NUL.search(txt)
                result2=NUL.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    self.estado.append("   {:<28}".format("NUL -> Número de línea")+"  "+'   {0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"    {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)
        
            #Palabra reservada
            if PAL.search(txt):
                result=PAL.search(txt)
                result2=PAL.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    self.estado.append("   {:<28}".format("PAL  ->  Palabra reservada")+"  "+'  {0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"    {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)
                        
            #Cadena de texto
            while TEX.search(txt):
                result=TEX.search(txt)
                result2=TEX.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    pos=txt[inicio+1:].find('"')
                    if pos!=-1 and inicio+pos<fin:
                        fin=inicio+pos+2
                    self.estado.append("   {:<28}".format("TEX  ->  Cadena de texto")+"  "+'   {0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"    {:<10}".format(txt[inicio:fin]))
                    #txt1=txt[0:inicio]
                    #txt=txt1+txt[fin:]
                    for k in range(inicio,fin):
                        revisando[k]=" "
                    txt="".join(revisando)

            #Pares de paréntesis
            while PAR.search(txt):
                result=PAR.search(txt)
                result2=PAR.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    pos=txt[inicio:].find(')')
                    if pos!=-1 and inicio+pos<fin:
                        fin=inicio+pos+1
                    self.estado.append("   {:<28}".format("PAR -> Paréntesis")+"        "+'{0:3d}'.format(inicio)+"  "+'{0:4d}'.format(inicio+1)+"     {:<10}".format(txt[inicio:inicio+1]))
                    
                    revisando[inicio]=" "
                    revisando[fin-1]=" "
                    txt="".join(revisando)

            #Operador relacional
            if OPR.search(txt):
                result=OPR.search(txt)
                result2=OPR.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    self.estado.append("   {:<28}".format("OPR  ->  Operador relacional")+"  "+'   {0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"    {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "

            txt="".join(revisando)
            
            #Operador aritmético
            if OPA.search(txt):
                result=OPA.search(txt)
                result2=OPA.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    self.estado.append("   {:<28}".format("OPA -> Operador aritmético")+"  "+'{0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"   {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)

            #Operador de asignación
            if OAS.search(txt):
                result=OAS.search(txt)
                result2=OAS.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    inicio=inicio+1
                    fin=fin-1
                    self.estado.append("   {:<28}".format("OAS -> Op. de asignación    ")+" "+'  {0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"   {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)
            
            #Número flotante
            if NOF.search(txt):
                result=NOF.search(txt)
                result2=NOF.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    self.estado.append("   {:<28}".format("NOF->Número flotante")+"  "+'{0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"   {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)

            #Separador
            if SEP.search(txt):
                result=SEP.search(txt)
                result2=SEP.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    self.estado.append("   {:<28}".format("SEP -> Separador")+"        "+'{0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"   {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)

            #Número entero
            if NOI.search(txt):
                result=NOI.search(txt)
                result2=NOI.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    inicio=inicio+1
                    self.estado.append("   {:<28}".format("NOI -> Número entero")+"     "+'{0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"   {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)


            #Identificador
            if IDS.search(txt):
                result=IDS.search(txt)
                result2=IDS.finditer(txt)
                for match in result2:
                    [inicio,fin]=match.span()
                    self.estado.append("   {:<28}".format("ID -> Identificador")+"          "+'{0:3d}'.format(inicio)+"  "+'{0:4d}'.format(fin)+"   {:<10}".format(txt[inicio:fin]))
                    for k in range(inicio,fin):
                        revisando[k]=" "
            txt="".join(revisando)

            #Detectando los errores

            #Comilla
            revisando2=""
            for k in range(len(revisando)):
                if revisando[k]!=' ':
                    if revisando[k]!='\t':
                        if revisando[k]!='\n':
                            revisando2=revisando2+revisando[k]
                    
            if len(revisando2)!=0:
                
                self.estado.append("\nErrores encontrados en esta línea.")
                for k in range(len(revisando)):
                    if revisando[k]!=' ':
                        if revisando[k]!='\t':
                            if revisando[k]!='\n':
                                error=error+1
                                self.estado.append("              Caracter suelto --> "+'      {0:3d}'.format(k)+"  "+'{0:4d}'.format(k+1)+"   {:<10}".format(revisando[k]))

        if error != 0:
            self.estado.append("\nNo. de Errores en total = {}".format(error))
        else:
            self.estado.append("\nNo se han encontrado errores.")
