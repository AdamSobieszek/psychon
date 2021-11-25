import random
import numpy as np

def cycles(n_cond,n_stimuli):
    rng = [*range(n_cond)]
    random.shuffle(rng)
    cycle = []
    for n, item in enumerate(rng):
        cycle.append([int(rng[(n+i)%n_cond]) for i in range(n_cond)]*((n_stimuli)//n_cond))
    return cycle


def latin_square(n_cond, n_stimuli, participants =None, cond_per_person = 1,equal=True):
    cycle = cycles(n_cond,n_stimuli)
    conditions = np.zeros((n_stimuli*n_cond if not participants else (participants*cond_per_person//n_cond)*n_cond, n_stimuli))

    for j, col in enumerate(conditions): # fill conditions with cycles
        conditions[j] = cycle[j % n_cond]
    conditions = conditions.transpose()

    for i in range(conditions.shape[1]//n_cond):
        con = conditions[:, i * n_cond:i * n_cond + n_cond]
        con = list(con)
        random.shuffle(con)
        con = np.array(con)
        # print(con)
        conditions[:, i * n_cond:i * n_cond + n_cond] = con

    conditions = list(conditions)

    conditions = np.array(conditions)
    return np.vectorize(lambda x: int(x))(conditions.transpose())


order = [*range(50)]
square = latin_square(6,24, 500,2)
square_text = "\\n".join(','.join([str(mm) for mm in m]) for m in list(square))
print(square.shape)
import csv
# csv.writer(open("conditions.csv","w"), lineterminator="\n").writerows(square)
# csv.writer(open("dominance_orders.csv","w"),orders)
