from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime


reader = csv.DictReader(open(sys.argv[1], 'r'))
#McCain
obamadonations = defaultdict(lambda:0)
mccaindonations = defaultdict(lambda:1)

for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount = float(row['contb_receipt_amt'])
    date = datetime.datetime.strptime(datestr, '%d-%b-%y')

    if 'Obama' in name:
        obamadonations[date] += amount
    if 'McCain' in name:
        mccaindonations[date] += amount


    #dictionaries
sorted_by_date_0 = sorted(obamadonations.items(), key=lambda(key, val): key)
sorted_by_date_1 = sorted(mccaindonations.items(), key=lambda(key, val): key)
xs, ys0 = zip(*sorted_by_date_0)
plt.plot(xs, ys0, label='Obama')
#xs, ys1 = zip(*sorted_by_date_1)
xs, ys0 = zip(*sorted_by_date_1)

plt.plot(xs, ys0, label='McCain')
plt.legend(loc = 'upper center', ncol = 4)
plt.savefig('test.png', format='png')