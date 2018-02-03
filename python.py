def main():
    rank = range(0, 1010, 10)
    result = [[] for i in repeat(None, len(rank))]

    for i in range(0, len(rank)):
        for it in range(0, 8):
            result[i].append(0.0)

    for id in range(0, len(rank)):
        values = []
        for i in range(0, rank[id]):
            values.append(i)

        # CREO DUE ALBERI
        # per eseguire i test della lista ordinata
        br_tree = ABR()
        rn_tree = ARN()

        print " ("+str(rank[id])+" elements) "
        print "ORDERLY INSERTION"
        for i in range(0, len(values)):
            start = timer()
            br_tree.insert_ite(values[i])
            middle = timer()
            rn_tree.insert(values[i])
            end = timer()

            # confronto e aggiorno i calcoli sull'
            # Albero Binario di Ricerca
            if result[id][0] < (middle-start):
                result[id][0] = middle-start
            if result[id][1] < br_tree.h_ins:
                result[id][1] = br_tree.h_ins

            # confronto e aggiorno i calcoli sull'
            # Albero Rosso-Nero
            if result[id][2] < (end - middle):
                result[id][2] = end - middle
            if result[id][3] < rn_tree.h_ins:
                result[id][3] = rn_tree.h_ins

        # PERMUTO GLI ELEMENTI RANDOMICAMENTE
        random.shuffle(values)

        # CREO DUE NUOVI ALBERI
        br_tree = ABR()
        rn_tree = ARN()

        # ESEGUO GLI INSERIMENTI
        # nuovamente per la lista permutata

        # confronto e aggiorno i calcoli sull'ABR
        # confronto e aggiorno i calcoli sull'ARN
