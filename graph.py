# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:33:57 2018

@author: Simon
"""

table=dict(A='0',C='1',G='2',T='3')
mapp='ACGT'.maketrans(table)                                                 

def convert_quad2(string):
    """
    Converti une string composé de l'alphabet 'ACTG' en sa repésentation polynomiale en base 4
    """
    hashed_to =int(string.translate(mapp),4)
    return (hashed_to)               #Nombre premier proche la taile désirée de notre table

def hash_Function(to_hash,modulo):
    "Effectue le hâchage"
    #return hash(to_hash) % modulo

     #Avec to_hash a string:
    return convert_quad2(to_hash) % modulo
    
        
class DeBrujinGraph:
    """
    Graphe de Brujin pour l'alphabet 'TACG'. N'accepte aucun autre alphabet.
    
    """
    def __init__(self, Iterable, k=21):
        # initialise la structure de données
        self._alphabet='ATGC'
        self._size = 0         #Nombre de noeuds dans notre graphe
        
        # Taille de la table :
        # On se laisse une marge de manoeuvre à l'initialisation
        try:
            self._load = int(((len(Iterable)*(len(Iterable[0])-k+1) /1.68) *4) //2)    # Choisi selon l'exemple,
        except IndexError:                                                  #selon les répétitions attendues
            self._load = 10000                                          # Taille minimale de la table
            
        self._HashTable = [[] for i in range(self._load)]  #Initiation de la table
        
        for seq in Iterable:                             # On remplit la table
            for i in range(len(seq)-k+1):
                N = seq[i:k+i]
                if N not in self._HashTable[hash_Function(N,self._load)]:
                    self._HashTable[hash_Function(N,self._load)].append(N)
                    self._size += 1
                    
        if self.load_factor()>0.75:                  #On s'assure que la capacité est bonne
            self.reHash()
                    
        
        
    def __contains__(self, N):
        # détermine si le graphe de Brujin contient le noeud N
        return (N in self._HashTable[hash_Function(N,self._load)])
        
    def __iter__(self): # -> Iterable[str]:
        return self.nodes() # retourne un itérable sur les noeuds du graphe
    
    def load_factor(self):
        # calcule le facteur de charge de la table de hachage sous-jacente
        return (self._size/self._load)
        
    def add(self, N):
        # ajoute le noeud N au graphe
        if N not in self:
            self._size += 1
            self._HashTable[hash_Function(N,self._load)].append(N)
            
        # réhâchage si on dépasse une capacité de charge de 0.75
        if self.load_factor()>0.75:
            self.reHash()        
            
            
    def remove(self, N):
        # enlève le noeud N du graphe
        self._HashTable[hash_Function(N,self._load)].remove(N)
        self._size -= 1
        
        # Doit implémenter le réhâchage!!!
        
    
    def reHash(self):
        """
        Fonction implémentant le réhâchage lorsqu'on dépasse la capacité de la table
        """
        new_load = self._load * 2
        new_table = [[] for i in range(new_load)]
        for N in self.nodes():
            new_table[hash_Function(N,new_load)].append(N)
        
        self._load = new_load
        self._HashTable = new_table
        
    def nodes(self): # -> Iterable[str]:
        if self._size <1 : pass
        else:
            for j in range(self._load):
                if len(self._HashTable[j])>0:
                    for N in self._HashTable[j]:
                        yield N
        
    def predecessors(self, N): # -> Iterable[str]:
        # retourne tous les prédécesseur du noeud N
        parents =[]
        for letter in self._alphabet:
            if (letter + N[:-1]) in self:
                parents.append(letter + N[:-1])
        return parents
        
    def successors(self, N): # -> Iterable[str]:
        # retourne tous les successeurs du noeud N
        childrens =[]
        for letter in self._alphabet:
            if (N[1:] + letter) in self:
                childrens.append(N[1:] + letter)
        return childrens
    
    def find_roots(self):
        roots=[]
        for N in self.nodes():
            if len(self.predecessors(N))<1 : roots.append(N)
        return roots
    
    
    def walk_all(self,roots):
        """
        Fonction utlisant une pile pour effectuer une marche à travers les noeuds en ignorant les cycles.
        À partir d'un noeud identifié comme une racine, on utilise un set pour ne pas retourner à un noeud qui a déjà 
        été visité
        
        Retourne une liste de segments contigüs
        
        (NOTE : Pourrait utiliser un dictionnaire avec comme valeur le nombre de passage pour permettre un certain
        nombre de cycles)
        """
        contig=[]
        for root in roots:
            pile =[(root,0)]
            traveled=[]
            traveled_set=set()
            while len(pile)!= 0 :
                N,lenght = pile.pop()
                traveled = traveled[:lenght]
                traveled.append(N)
                traveled_set.add(N)

                
                if len(self.successors(N)) == 0 : #Fin, ajoute à contig
                    seq=traveled[0]
                    for next_in_seq in traveled[1:]:
                        seq += next_in_seq[-1]
                    contig.append(seq)
                for children in self.successors(N):
                    if children in traveled_set:          #Détection d'une boucle, arrêt
                        seq=traveled[0]
                        for next_in_seq in traveled[1:]:
                            seq += next_in_seq[-1]
                        contig.append(seq)

                    else:
                        pile.append((children,lenght+1))
                
        return contig