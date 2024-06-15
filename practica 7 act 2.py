def holacomova():
    arc=open("act_2.csv","r")
    lst=arc.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(";")
        linea1[0]=int(linea1[0])
        linea1[1]=int(linea1[1])
        linea1[2]=int(linea1[2])
        linea1[3]=int(linea1[3])
        lst1.append(linea1)
    arc.close()
    arc1=open("act_2.csv","w")
    lst2=[]
    
    for j in range(len(lst1)):
        tot=0
        ele=len(lst1[j])
        for i in range(len(lst1[j])):
            tot=tot+lst1[j][i]
            arc1.write(str(lst1[j][i]))
            arc1.write(";")
        pro=tot//ele
        lst2.append(lst1[j])
        arc1.write("\n")
        arc1.write(str(pro))
        arc1.write("\n")
        lst2.append(pro)
    arc1.close()
    
    return lst2

print(holacomova())

"""VERSION ALTERNATIVA PARA CUANDO NO SE NUM DE ELEMENTOS EN CADA LINEA"""
# 
# def holacomova():
#     arc=open("act_2.csv","r")
#     lst=arc.readlines()
#     lst1=[]
#     for linea in lst:
#         linea=linea[:-1]
#         linea1=linea.split(";")
#         for carac in range(len(linea1)):
#             linea1[carac]=int(linea1[carac])
#         lst1.append(linea1)
#     arc.close()
#     arc1=open("act_2.csv","w")
#     lst2=[]
#     ele=len(lst1)
#     for j in range(len(lst1)):
#         tot=0
#         ele=len(lst1[j])
#         for i in range(len(lst1[j])):
#             tot=tot+lst1[j][i]
#             arc1.write(str(lst1[j][i]))
#             arc1.write(";")
#         pro=tot//ele
#         lst2.append(lst1[j])
#         arc1.write("\n")
#         arc1.write(str(pro))
#         arc1.write("\n")
#         lst2.append(pro)
#     arc1.close()
#     
#     return lst2
# 
# print(holacomova())