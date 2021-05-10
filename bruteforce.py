import itertools
import csv
import time
# import timeit


def read_csv(file_name):
    actions = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        datas = csv.reader(csvfile, delimiter=',', quotechar="'")
        for i, data_action in enumerate(datas):
            data_dict = {}
            if i != 0:
                for data in data_action:
                    data_dict['name'] = data_action[0]
                    data_dict['price'] = float(data_action[1])
                    data_dict['profit'] = float(data_action[1])*float(data_action[2])/100
                actions.append(data_dict)
    return actions


# print(timeit.timeit("read_csv('actions.csv')", setup="from __main__ import read_csv", number=1000))


def data_action(name: str, info: str, actions_list: list):
    """ retourne l'info demandée ('price' ou 'profit') sur l'action dont le nom est passé en paramètre"""
    return list(filter(lambda actions_data: actions_data['name'] == name, actions_list))[0][info]


def main():
    start_time = time.time()
    # actions = read_csv('actions_test.csv')
    actions = read_csv('actions.csv')
    budget_max = 500
    best_combination = {'profit': 0}
    actions_name = []
    [actions_name.append(datas_action['name']) for datas_action in actions]
    for nb_actions in range(1, len(actions_name)+1):
        for combination in itertools.combinations(actions_name, nb_actions):
            total_price = 0
            total_profit = 0
            for action in combination:
                total_price = total_price + data_action(action, 'price', actions)
                total_profit = total_profit + data_action(action, 'profit', actions)
                if total_price > budget_max:
                    break
                if total_profit > best_combination['profit']:
                    best_combination['combination'] = combination
                    best_combination['profit'] = total_profit
                    best_combination['price'] = total_price

    print('Total cost:', best_combination['price'])
    print('Profit:', round(best_combination['profit'], 2))
    print('Combination:', best_combination['combination'])
    print("Execution time : %s seconds" % (time.time() - start_time))



if __name__ == "__main__":
    main()
