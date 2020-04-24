# lib import
import math
import os
import mne
import pandas as pd


# some useful functions
chan = 0
peaks_ind = []
for i in range(eeg.n_times-2):
    if  (eeg[chan,i+1][0][0][0] - eeg[chan,i][0][0][0])<0 and (eeg[chan,i+2][0][0][0]-eeg[chan,i+1][0][0][0])>0:
        peaks_ind.append(i+1)
ind_spikes  = []
for i in range(len(peaks_ind)):
    if (eeg[chan,peaks_ind[i]][0][0][0])<(-1e-2):
        ind_spikes.append(peaks_ind[i])
path = '/Users/ilamiheev/Downloads/Sat19540'
files = [f for f in sorted(os.listdir(path))]
m = 0
tasks = []
labels_letter = []
labels_type = []
labels_match = []
labels_order = []
for g, h in enumerate(files):
    task1 = []
    labels_letter1 = []
    labels_type1 = []
    labels_match1 = []
    labels_order1 = []
    path1 = path + '/{0}'.format(files[g])
    l = pd.read_csv(path1)
    col_one_list = l['TMS'].tolist()
    delays_list = l['SND_START'].tolist()
    list1 = l['TRUTH'].tolist()
    list2 = l['TYPE'].tolist()
    list3 = l['MATCH_WITH_LAST'].tolist()
    list4 = l['ORDER'].tolist()
    f = []
    for i in range(len(col_one_list)):
        f.append(int(col_one_list[i]))
    number_spikes = f.count(1)
    j1 = 0
    for i in range(len(col_one_list)):
        if (col_one_list[i] == 0 and i == 0) and (delays_list[i] != 'N/A' and delays_list[i + 1] != 'N/A') and \
                col_one_list[i + 1] == 1:
            task1.append(
                true_start_stim[m:m + number_spikes][0] + 200 - (delays_list[i + 1] * 2000 - delays_list[i] * 2000))
        elif (col_one_list[i] == 1) and (delays_list[i] != 'N/A'):
            l1 = true_start_stim[m:m + number_spikes][j1] + 200
            task1.append(l1)
            labels_letter1.append(list1[i])
            labels_type1.append(list2[i])
            labels_match1.append(list3[i])
            labels_order1.append(list4[i])
            l2 = delays_list[i]
            j1 = j1 + 1
        elif (col_one_list[i] == 0) and (delays_list[i] != 'N/A'):
            print(l1)
            print(l1 + (delays_list[i] * 2000 - l2 * 2000))
            task1.append(l1 + (delays_list[i] * 2000 - l2 * 2000))
            labels_letter1.append(list1[i])
            labels_type1.append(list2[i])
            labels_match1.append(list3[i])
            labels_order1.append(list4[i])
    m = number_spikes
    labels_letter.append(labels_letter1)
    labels_type.append(labels_type1)
    labels_match.append(labels_match1)
    labels_order.append(labels_order1)
    tasks.append(task1)


def func_a(k, llll, b, min_del):
    pp = k[0][:, 0][llll * 2:((b + 1) * 2)]
    mm, mm1 = [], []
    kk = [1, 2]
    for i in range(0, (len(pp) - 2), 2):
        if (min_del - 200) < (pp[i + 2] - pp[i]) < 2 * min_del - 1000:
            mm.append(kk[0])
            mm1.append(pp[i + 2] - pp[i])
        else:
            mm.extend([kk[0], kk[1]])
            mm1.append(pp[i + 2] - pp[i])
    return mm, mm1


def func_b(mm, f2, n, m):
    ind_f1, ind_f2 = [y for y, e in enumerate(f2) if e == 2], [y for y, e in enumerate(mm) if e == 2]
    print(n)
    #print(mm)
    #$print(f2)
    st1 = ((ind_f2[ind_f2.index(n) + 1] - ind_f2[ind_f2.index(n) - 1]) - 1)
    print('m =', m)
    print(len(ind_f1))
    print(len(list(filter(lambda a: a > m, ind_f1))))
    print(len(list(filter(lambda a: a < m, ind_f1))))
    print(ind_f1)
    st2 = (list(filter(lambda a: a > m, ind_f1)))[0] - (list(filter(lambda a: a < m, ind_f1)))[-1]
    return st1 - st2


def func_c(f):
    for i in range(len(f) - 1):
        if f[0] == 0:
            f[0] = 2
        elif f[i] == 1 and f[i + 1] == 0:
            f[i + 1] = 2
    ind = [i for i, e in enumerate(f) if e == 2]
    f2 = list(filter(lambda a: a != 0, f))
    return f2, ind


# find right order of spike pairs
def create_events(raw):
    return raw

def find_false_spikes(path_to_eeg, path_tables):
    file = mne.io.read_raw_eeglab(path_to_eeg, preload=True)
    spikes_delays = mne.events_from_annotations(file)
    paths = [f for f in sorted(os.listdir(path_tables))]
    paths = paths[0:5]
    fin_list, llll, all_spikes = [], 0, 0
    for g, h in enumerate(paths):
        j, ind_1 = 0, 0
        path_to_table = path_tables + '/{0}'.format(paths[g])
        datafile = pd.read_csv(path_to_table)
        tms_sham_order = datafile['TMS'].tolist()
        delays_table = datafile['SND_START'].tolist()
        ind_stim = [i for i, e in enumerate(tms_sham_order) if e == 1 and math.isnan(delays_table[i]) == 0]
        new_l1 = [delays_table[index] for index in ind_stim]
        min_del = min(([round(new_l1[index + 1] * 2000 - new_l1[index] * 2000) for index in range(len(new_l1) - 1)]))
        f = []
        for i in range(len(tms_sham_order)):
            f.append(int(tms_sham_order[i]))
        number_spikes = f.count(1)
        all_spikes += number_spikes
        b = llll + number_spikes
        order_table, ind_st_sham = func_c(f)
        order_eeg, eeg_delays = func_a(spikes_delays, llll, b, min_del)
        fin_list_1 = []
        if len(order_eeg) < len(order_table):
            #and g < (len(paths) - 1):
            tau, _ = func_a(spikes_delays, b + 1, b + 2 + len(order_table) - len(order_eeg), min_del)
            order_eeg.extend(tau)
        #elif len(order_eeg) < len(order_table) and g == (len(paths) - 1):
            #order_eeg.append(1)
        ind_f = [y for y, e in enumerate(order_table) if e == 2]
        for i in range(len(order_table)):
            if order_eeg[i] == 1 and order_table[i - j] == 1:
                fin_list_1.append(1)
            # check this
            elif order_eeg[i] == 2 and order_table[i - j] == 1 and i == 1:
                del fin_list_1[-1:]
                fin_list_1.append(3)
                j += 2
            # new condition for false spike in group
            elif order_eeg[i] == 1 and order_table[i - j] == 2:
                hh = ind_f.index(i - j)
                if (i - j) == order_table.index(2):
                    a3 = order_table[:i - j].count(1)
                    if a3 != 0:
                        del fin_list_1[-a3:]
                    fin_list_1.extend([3] + [1] * a3)
                    j += 1
                else:
                    a1, a2 = ind_f[hh - 1], ind_f[hh]
                    del fin_list_1[-(a2 - a1 - 1):]
                    fin_list_1.extend([3] + [1] * (a2 - a1 - 1))
                    j += 1
                # if all(i < 2 * min_del - 1000 for i in delays_table[a1 + 1:a2 - 1]):
                # fin_list_1.extend([3] + [1] * (a2 - a1 - 2))
                # j += 1
                # else:
                # print('false')
            elif order_eeg[i] == 2 and order_table[i-j] == 1 and (0 == i):
                j += 1
            elif ((order_eeg[i] == 2 and order_eeg[i - 1] == 1) and (i != 0)) and (
                    (order_table[i - j] == 1) and func_b(order_eeg, order_table, i, i - j)) != 0:
                del fin_list_1[-1:]
                fin_list_1.append(3)
                j += 2
            # check number of stim between two sham, its important!
            elif ((order_eeg[i] == 2 and order_table[i - j] == 1) and (i != 0)) and (
                    order_table[i - j] == 1 and func_b(order_eeg, order_table, i, i - j) == 0):
                j += 1
            # as a replacement for a global variable
            ind_1 = i - j
        llll = b
        # we should add s1 instead of s!
        # should correct this statement
        if fin_list_1.count(1) != order_table.count(1):
            s = order_table.count(1) - fin_list_1.count(1)
            s1 = order_table[ind_1:].count(1) - order_eeg[ind_1 + j:].count(1)
            fin_list_1.extend([1] * s)
            llll += s1
        fin_list.extend(fin_list_1)
    ind_false_spikes = [i for i, e in enumerate(fin_list) if e == 3]
    true_start_stim = []
    ppf = spikes_delays[0][:, 0][0:]
    # h = 0
    # for i in range(1, (len(ppf)), 2):
    # if h not in ind_false_spikes:
    # true_start_stim.append(ppf[i])
    # h += 1
    return ind_false_spikes, true_start_stim


if __name__ == '__main__':
    path_1 = '/Users/ilyamikheev/Downloads/sub_8.set'
    path_2 = '/Users/ilyamikheev/Downloads/Sat19540'
    find_false_spikes(path_1, path_2)
