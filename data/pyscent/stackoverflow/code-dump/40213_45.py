import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

rep = 5

timings = dict()

for n in range(7):
    print(f'N = 10^{n}')

    N = 10**n
    setup = f'''import numpy as np\nthe_list = np.random.random({N})*6+3\nhi = 9\nlo = 3\ndlt = hi - lo\nmid = (hi + lo) / 2\ndef return_the_num(l, lst, h):\n    return [l if abs(l-x) < abs(h-x) else h for x in lst]'''

    fct = 'np.round((the_list - lo)/dlt) * dlt + lo'
    t = timeit.Timer(fct, setup=setup)
    timings['SpghttCd_np'] = timings.get('SpghttCd_np', []) + [np.min(t.repeat(repeat=rep, number=1))]

    fct = 'return_the_num(3, the_list, 9)'
    t = timeit.Timer(fct, setup=setup)
    timings['Austin'] = timings.get('Austin', []) + [np.min(t.repeat(repeat=rep, number=1))]

    fct = '[(lo, hi)[mid < v] for v in the_list]'
    t = timeit.Timer(fct, setup=setup)
    timings['SpghttCd_lc'] = timings.get('SpghttCd_lc', []) + [np.min(t.repeat(repeat=rep, number=1))]

    setup += '\nround_the_num = lambda list, upper, lower: [upper if x > (upper + lower) / 2 else lower for x in list]'
    fct = 'round_the_num(the_list, 9, 3)'
    t = timeit.Timer(fct, setup=setup)
    timings['Carles Mitjans'] = timings.get('Carles Mitjans', []) + [np.min(t.repeat(repeat=rep, number=1))]

    setup += '\nupper_lower_bound_list=[3,9]'
    fct = '[min(upper_lower_bound_list, key=lambda x:abs(x-myNumber)) for myNumber in the_list]'
    t = timeit.Timer(fct, setup=setup)
    timings['mad_'] = timings.get('mad_', []) + [np.min(t.repeat(repeat=rep, number=1))]

    setup += '\ndef return_bound(x, l, h):\n    low = abs(x - l)\n    high = abs(x - h)\n    if low < high:\n        return l\n    else:\n        return h'
    fct = '[return_bound(x, 3, 9) for x in the_list]'
    t = timeit.Timer(fct, setup=setup)
    timings["Scratch'N'Purr"] = timings.get("Scratch'N'Purr", []) + [np.min(t.repeat(repeat=rep, number=1))]

    setup += '\ndef round_the_list(list, bound_1, bound_2):\n\tmid = (bound_1+bound_2)/2\n\tfor i in range(len(list)):\n\t\tif list[i] > mid:\n\t\t\tlist[i] = bound_2\n\t\telse:\n\t\t\tlist[i] = bound_1'
    fct = 'round_the_list(the_list, 3, 9)'
    t = timeit.Timer(fct, setup=setup)
    timings["Abhishek Patel"] = timings.get("Abhishek Patel", []) + [np.min(t.repeat(repeat=rep, number=1))]

    fct = 'dhi = 9 - the_list\ndlo = 3 - the_list\nidx = dhi + dlo < 0\nthe_list + np.where(idx, dhi, dlo)'
    t = timeit.Timer(fct, setup=setup)
    timings["SpghttCd_where"] = timings.get("SpghttCd_where", []) + [np.min(t.repeat(repeat=rep, number=1))]

print('done')

df = pd.DataFrame(timings, 10**np.arange(n+1))
ax = df.plot(logx=True, logy=True)
ax.set_xlabel('length of the list')
ax.set_ylabel('seconds to run')
ax.get_lines()[-1].set_c('g')
plt.legend()
print(df)
