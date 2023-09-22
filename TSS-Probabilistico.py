import snap
import random

random.seed(10)

SOGLIA = 0.40
PATH = "C:/Users/ilcai/Downloads/Progetto_RS/email-Eu-core.txt"
Lista = []

#LoadedGraph = snap.LoadEdgeList(snap.TNEANet, "CA-GrQc.txt", 0, 1,)
# LoadedGraph.Dump()

for j in range(1,10):
    S = snap.TNEANet.New()
    LoadedGraph = snap.LoadEdgeList(snap.TNEANet, PATH, 0, 1)
    for EI in LoadedGraph.Edges():
        #LoadedGraph.AddFltAttrDatE(EI.GetId(),0.4,"Pr")
        LoadedGraph.AddFltAttrDatE(EI.GetId(),1/(LoadedGraph.GetNI(EI.GetSrcNId()).GetDeg()+LoadedGraph.GetNI(EI.GetDstNId()).GetDeg()),"Pr")
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
        LoadedGraph.AddIntAttrDatN(NI.GetId(),j,"Tr")
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

# if len(Lista)>0:
#     avg = sum(Lista) / len(Lista)
#
# avg
# Lista
import matplotlib.pyplot as plt

x = [k for k in range(1,10)]
plt.plot(x, Lista)
plt.show()


# for i in LoadedGraph.Nodes():
#     print("Nodo: "+str(i.GetId()))
#     print((LoadedGraph.GetIntAttrDatN(i.GetId(), "Tr")))
#     print((i.GetDeg()*(i.GetDeg()+1)))
#     print((LoadedGraph.GetIntAttrDatN(i.GetId(), "Tr") /(i.GetDeg()*(i.GetDeg()+1))))
