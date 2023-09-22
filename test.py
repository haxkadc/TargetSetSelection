import snap
import random
import matplotlib.pyplot as plt
SOGLIA = 0.40
# Rnd = snap.TRnd(42)
# Rnd.Randomize()

PATH = "C:/Users/ilcai/Downloads/Progetto_RS/email-Eu-core.txt"
PATH = "C:/Users/ilcai/Downloads/Progetto_RS/political.csv"
DIRECTORY = "C:/Users/ilcai/Downloads/Progetto_RS/"
LoadedGraph = snap.LoadEdgeList(snap.TNEANet, PATH, 0, 1)

#
# labels = {}
# for NI in LoadedGraph.Nodes():
#     labels[NI.GetId()] = str(NI.GetId())
# LoadedGraph.DrawGViz(snap.gvlNeato, "output.png", " ", labels)

Lista = []
i = 0
for j in range (0,10):
    for k in range(0,1):
        LoadedGraph = snap.LoadEdgeList(snap.TNEANet, PATH, 0, 1,",")
        #LoadedGraph = snap.LoadEdgeList(snap.TNEANet, "email-Eu-core.txt", 0, 1,)

        #LoadedGraph = snap.LoadEdgeList(snap.TNEANet, "CA-GrQc.txt", 0, 1,)
        # LoadedGraph.Dump()

        S = snap.TNEANet.New()

        for EI in LoadedGraph.Nodes():
            # LoadedGraph.AddFltAttrDatN(EI.GetId(),0.3+(EI.GetDeg()/10000),"Pr")
            #LoadedGraph.AddIntAttrDatN(EI.GetId(),1+round(EI.GetDeg()*SOGLIA),"Tr")
            #LoadedGraph.AddIntAttrDatN(EI.GetId(),1+int(SOGLIA*EI.GetDeg()),"Tr")
            #LoadedGraph.AddIntAttrDatN(EI.GetId(),5,"Tr")
            LoadedGraph.AddIntAttrDatN(EI.GetId(),j,"Tr")
        # for EI in LoadedGraph.Nodes():
        #     print(LoadedGraph.GetIntAttrDatN(LoadedGraph.GetNI(EI.GetId()),"Tr"))
        while LoadedGraph.Empty() == False:
            #NiD = LoadedGraph.BegNI().GetId()
            #print("Numero Nodi: "+str(LoadedGraph.GetNodes()))
            flag = False
            flag2 = False
            for Ni in LoadedGraph.Nodes():
                # print("Primo Caso")
                NiD = Ni.GetId()
                if LoadedGraph.GetIntAttrDatN(NiD, "Tr") == 0:
                    #print("Caso 1")
                    for i in range(0,LoadedGraph.GetNI(NiD).GetDeg()):
                        TrU = LoadedGraph.GetIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i), "Tr")
                        if TrU > 0:
                            TrU = TrU -1
                            LoadedGraph.AddIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i),TrU,"Tr")
                    LoadedGraph.DelNode(NiD)
                    #print("Nodo Eliminato: "+str(NiD))
                    flag = True
                    break
            if flag == False:
                # print("Secondo Caso")
                for Nii in LoadedGraph.Nodes():
                    NiD = Nii.GetId()
                    if LoadedGraph.GetNI(NiD).GetDeg() < LoadedGraph.GetIntAttrDatN(NiD, "Tr"):
                        #print("Caso 2")
                        S.AddNode(NiD)
                        for i in range(0,LoadedGraph.GetNI(NiD).GetDeg()):
                            TrU = LoadedGraph.GetIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i), "Tr")
                            if TrU > 0:
                                TrU = TrU -1
                                LoadedGraph.AddIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i),TrU,"Tr")
                        LoadedGraph.DelNode(NiD)
                        flag2 = True
                        #print("Nodo aggiunto: "+str(NiD))
                        break
            if flag == False and flag2 == False:
                # print("Terzo Caso")
                vMax = 0
                NmaxId = -1
                for v in LoadedGraph.Nodes():
                    NiD = v.GetId()
                    if v.GetDeg()!=0:
                        argmax = LoadedGraph.GetIntAttrDatN(NiD, "Tr") /(v.GetDeg()*(v.GetDeg()+1))
                        # print(argmax)
                        if argmax > vMax:
                            NmaxId = v.GetId()
                            vMax = argmax
                #print("Caso 3 Nodo Eliminato: "+str(NmaxId))
                if NmaxId >= 0:
                    LoadedGraph.DelNode(NmaxId)
        Lista.append(S.GetNodes())
    # print("NODI S: "+str(S.GetNodes()))
Lista2 = []
random.seed(10)
Lista2
len(Lista2)
#LoadedGraph = snap.LoadEdgeList(snap.TNEANet, "CA-GrQc.txt", 0, 1,)
# LoadedGraph.Dump()
for j in range(0,10):
    for k in range(0,10):
        for p in range(0,10):
            S = snap.TNEANet.New()
            LoadedGraph = snap.LoadEdgeList(snap.TNEANet, PATH, 0, 1,",")
            for EI in LoadedGraph.Edges():
                LoadedGraph.AddFltAttrDatE(EI.GetId(),j/10,"Pr")
                #LoadedGraph.AddFltAttrDatE(EI.GetId(),1/(LoadedGraph.GetNI(EI.GetSrcNId()).GetDeg()+LoadedGraph.GetNI(EI.GetDstNId()).GetDeg()),"Pr")
                #LoadedGraph.AddFltAttrDatE(EI.GetId(),0.3,"Pr")
                #print((1/(LoadedGraph.GetNI(EI.GetSrcNId()).GetDeg()+LoadedGraph.GetNI(EI.GetDstNId()).GetDeg())))
                #LoadedGraph.AddFltAttrDatN(EI.GetId(),0.3+(EI.GetDeg()/10000),"Pr")
                # LoadedGraph.AddIntAttrDatN(EI.GetId(),1+round(EI.GetDeg()*SOGLIA),"Tr")
            for EI in LoadedGraph.Edges():
                Number = random.random()
                # print("Edge")
                # print(EI.GetSrcNId(),EI.GetDstNId())
                # print(Number)
                if Number < LoadedGraph.GetFltAttrDatE(EI.GetId(),"Pr"):
                    LoadedGraph.DelEdge(EI.GetId())

            for NI in LoadedGraph.Nodes():
                 #LoadedGraph.AddIntAttrDatN(NI.GetId(),1+round(NI.GetDeg()*SOGLIA),"Tr")
                 #LoadedGraph.AddIntAttrDatN(NI.GetId(),5,"Tr")
                 LoadedGraph.AddIntAttrDatN(NI.GetId(),k,"Tr")
            # for EI in LoadedGraph.Nodes():
            #     print(LoadedGraph.GetIntAttrDatN(LoadedGraph.GetNI(EI.GetId()),"Tr"))
            while LoadedGraph.Empty() == False:
                #NiD = LoadedGraph.BegNI().GetId()
                #print("Numero Nodi: "+str(LoadedGraph.GetNodes()))
                flag = False
                flag2 = False
                for Ni in LoadedGraph.Nodes():
                    # print("Primo Caso")
                    NiD = Ni.GetId()
                    if LoadedGraph.GetIntAttrDatN(NiD, "Tr") == 0:
                        #print("Caso 1")
                        for i in range(0,LoadedGraph.GetNI(NiD).GetDeg()):
                            TrU = LoadedGraph.GetIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i), "Tr")
                            if TrU > 0:
                                TrU = TrU -1
                                LoadedGraph.AddIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i),TrU,"Tr")
                        LoadedGraph.DelNode(NiD)
                        #print("Nodo Eliminato: "+str(NiD))
                        flag = True
                        break
                if flag == False:
                    # print("Secondo Caso")
                    for Nii in LoadedGraph.Nodes():
                        NiD = Nii.GetId()
                        if LoadedGraph.GetNI(NiD).GetDeg() < LoadedGraph.GetIntAttrDatN(NiD, "Tr"):
                            #print("Caso 2")
                            S.AddNode(NiD)
                            for i in range(0,LoadedGraph.GetNI(NiD).GetDeg()):
                                TrU = LoadedGraph.GetIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i), "Tr")
                                if TrU > 0:
                                    TrU = TrU -1
                                    LoadedGraph.AddIntAttrDatN(LoadedGraph.GetNI(NiD).GetNbrNId(i),TrU,"Tr")
                            LoadedGraph.DelNode(NiD)
                            flag2 = True
                            #print("Nodo aggiunto: "+str(NiD))
                            break
                if flag == False and flag2 == False:
                    # print("Terzo Caso")
                    vMax = 0
                    NmaxId = -1
                    for v in LoadedGraph.Nodes():
                        NiD = v.GetId()
                        if v.GetDeg()!=0:
                            argmax = LoadedGraph.GetIntAttrDatN(NiD, "Tr") /(v.GetDeg()*(v.GetDeg()+1))
                            # print(argmax)
                            if argmax > vMax:
                                NmaxId = v.GetId()
                                vMax = argmax
                    #print("Caso 3 Nodo Eliminato: "+str(NmaxId))
                    if NmaxId >= 0:
                        LoadedGraph.DelNode(NmaxId)
            Lista2.append(S.GetNodes())
            # print("NODI S: "+str(S.GetNodes()))
#
# #Per lista Th Crescente
# ListaDet = []
# for j in range(0,10):
#     if len(Lista)>0:
#         Inizio = j*10
#         Fine = 10*(j+1)
#         ListaDet.append(sum(Lista[Inizio:Fine]) /10)

Listavg = []

#Per lista2 Th o Ph crescente
for j in range(0,10):
    if len(Lista2)>0:
        Inizio = j*10
        Fine = 10*(j+1)
        Listavg.append(sum(Lista2[Inizio:Fine]) /10)

#
# #Per Th Crescente e Pr crescente
# for j in range(0,100):
#     if len(Lista2)>0:
#         Inizio = j*10
#         Fine = 10*(j+1)
#         Listavg.append(sum(Lista2[Inizio:Fine]) /10)


#Probabilita 50% Threshold Crescente
x = [k for k in range(0,10)]
plt.plot(x, Listavg,label = "Probabilistico")
plt.xlabel("Threshold")
plt.ylabel("TSS", rotation=0,)
plt.plot(x, Lista,label = "Deterministico")
plt.legend()
plt.title('Probabilita 50% Threshold Crescente\nDataset:Email_core.csv')
#plt.savefig(DIRECTORY+"Plot-Th-j_Pr_50_Email_core.png")
plt.show()


avg = sum(Lista2)/len(Lista2)
Listavg = [avg for k in range(0,10)]

#Probabilita 50% Threshold 5
x = [k for k in range(0,10)]
plt.plot(x, Listavg,label = "Probabilistico")
plt.xlabel("Threshold")
plt.ylabel("TSS", rotation=0,)
plt.plot(x, Lista,label = "Deterministico")
plt.legend()
plt.title("Probabilita 50% Threshold 5\nDataset:Email_core.txt")
#plt.savefig(DIRECTORY+"Plot-Th-5_Pr_50_Email_core.txt.png")
plt.show()


#Probabilita Proporzionale al Grado Threshold 5
x = [k for k in range(0,10)]
plt.plot(x, Listavg,label = "Probabilistico")
plt.xlabel("Threshold")
plt.ylabel("TSS", rotation=0,)
plt.plot(x, Lista,label = "Deterministico")
plt.legend()
plt.title("Probabilita Proporzionale al Grado Threshold 5\nDataset:Email_core.txt")
#plt.savefig(DIRECTORY+"Plot-Th-5_Pr_Proporzionale_Email_core.png")
plt.show()



#Probabilita Proporzionale al Grado Threshold Crescente
x = [k for k in range(0,10)]
plt.plot(x, Listavg,label = "Probabilistico")
plt.xlabel("Threshold")
plt.ylabel("TSS", rotation=0,)
plt.plot(x, Lista,label = "Deterministico")
plt.legend()
plt.title("Probabilita Proporzionale al Grado Threshold Crescente\nDataset:Email_core.csv")
#plt.savefig(DIRECTORY+"Plot-Th-j_Pr_Proporzionale_Email_core.png")
plt.show()




#Probabilita Proporzionale al Grado Threshold Proporzionale al Grado 40% dei nodi
x = [k for k in range(0,10)]
plt.plot(x, Listavg,label = "Probabilistico")
plt.xlabel("Threshold")
plt.ylabel("TSS", rotation=0,)
plt.plot(x, Lista,label = "Deterministico")
plt.legend()
plt.title("Probabilita Proporzionale al Grado\nThreshold Proporzionale al Grado 40% dei nodi\nDataset:Political.csv")
#plt.savefig(DIRECTORY+"Plot-Th-Proporzionale-40%_Pr_Proporzionale_Political.png")
plt.show()


#Probabilita 30% Threshold Proporzionale al Grado 40% dei nodi
x = [k for k in range(0,10)]
plt.plot(x, Listavg,label = "Probabilistico")
plt.xlabel("Threshold")
plt.ylabel("TSS", rotation=0,)
plt.plot(x, Lista,label = "Deterministico")
plt.legend()
plt.title("Probabilita 30%\nThreshold Proporzionale al Grado 40% dei nodi\n Dataset:Political.csv")
#plt.savefig(DIRECTORY+"Plot-Th-Proporzionale-40%_Pr_30%_Political.png")
plt.show()



#Probabilita Crescente Threshold 5
x = [0,10,20,30,40,50,60,70,80,90]
plt.plot(x, Listavg,label = "Probabilistico")
plt.xlabel("1-Probabilita")
plt.ylabel("TSS", rotation=0,)
plt.plot(x, Lista,label = "Deterministico")
plt.legend()
plt.title("Probabilita Crescente Threshold 5\nDataset:Email_core.txt")
#plt.savefig(DIRECTORY+"Plot-Th-5-Pr-crescente_Email_Core.png")
plt.show()

#Probabilita Crescente Threshold Crescente
# x = [0,10,20,30,40,50,60,70,80,90]
x2 = [k for k in range(0,10)]
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.plot(x2,Listavg[0:10],label = "Probabilistico 0 %")
ax1.plot(x2,Listavg[10:20],label = "Probabilistico 10 %")
ax1.plot(x2,Listavg[20:30],label = "Probabilistico 20 %")
ax1.plot(x2,Listavg[30:40],label = "Probabilistico 30 %")
ax1.plot(x2,Listavg[40:50],label = "Probabilistico 40 %")
ax1.plot(x2,Listavg[50:60],label = "Probabilistico 50 %")
ax1.plot(x2,Listavg[60:70],label = "Probabilistico 60 %")
ax1.plot(x2,Listavg[70:80],label = "Probabilistico 70 %")
ax1.plot(x2,Listavg[80:90],label = "Probabilistico 80 %")
ax1.plot(x2,Listavg[90:100],label = "Probabilistico 90 %")

ax1.plot(x2,Lista,label = "Deterministico")
# ax1.set_xlabel("1-Probabilita")
ax1.set_xticks(x2)
ax1.set_ylabel("TSS")
ax1.set_xlabel("Threshold")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.title("Probabilita Crescente Threshold crescente\nDataset:crescente_Political.csv")
plt.savefig(DIRECTORY+"Plot-Th-crescente-Pr-crescente_Political_csv.png")
plt.show()
# for i in LoadedGraph.Nodes():
#     print("Nodo: "+str(i.GetId()))
#     print((LoadedGraph.GetIntAttrDatN(i.GetId(), "Tr")))
#     print((i.GetDeg()*(i.GetDeg()+1)))
#     print((LoadedGraph.GetIntAttrDatN(i.GetId(), "Tr") /(i.GetDeg()*(i.GetDeg()+1))))
# for i in LoadedGraph.Nodes():
#     print("Nodo: "+str(i.GetId()))
#     print((LoadedGraph.GetIntAttrDatN(i.GetId(), "Tr")))
#     print((i.GetDeg()*(i.GetDeg()+1)))
#     print((LoadedGraph.GetIntAttrDatN(i.GetId(), "Tr") /(i.GetDeg()*(i.GetDeg()+1))))
