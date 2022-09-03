with open("prueba.txt") as f:
    Mensaje = f.read().replace('\n', ' ')
ascii = []
binario =[]
hamming =[]
traduccion =[]
for caracter in Mensaje:
    ascii.append(ord(caracter))
    binario.append(format(ord(caracter), "b"))
    traduccion.append(caracter)

paridad = len(binario)
for k in range(paridad):
    let = binario[k]
    d1 = int(let[0])
    d2 = int(let[1])
    d3 = int(let[2])
    d4 = int(let[3])
    d5 = int(let[4])
    d6 = int(let[5])
    d7 = int(let[6])
    p1 = d1^d2^d4^d5^d7
    p2 = d1^d3^d4^d6^d7
    p4 = d2^d3^d4
    p8 = d5^d6^d7
    ham = str(p1)+str(p2)+str(d1)+str(p4)+str(d2)+str(d3)+str(d4)+str(p8)+str(d5)+str(d6)+str(d7)   
    hamming.append(ham)

print("Ascii :",ascii)
print ("Binario :",binario)
print ("Hamming :",hamming)
print ("Traduccion :",traduccion)

largo= len(hamming)
for k in range(largo):
    d=hamming[k]
    data=list(d)
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[] 

    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):

            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse()

        
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))

    if((error)==0):
        print('No hay ningún error en el codigo Hamming recibido')

    elif((error)>=len(h_copy)):
        print('No se puede detectar el error')

    else:
        print('El error esta en',error,'bit')

        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'


        
        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
           
        h_copy.reverse()
        print('Despues de corregir el codigo Hamming es:- ', int(''.join(map(str, h_copy))))
  



