import itertools
import csv
import time


def get_data_actions(file_name: str) -> list:
    """ retourne la liste des données des actions : nom, prix, profit """
    actions = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        datas = csv.reader(csvfile, delimiter=',', quotechar="'")
        for data_action in list(datas)[1:]:
            data_dict = {}
            data_dict['name'] = data_action[0]
            data_dict['price'] = float(data_action[1])
            data_dict['profit'] = float(data_action[1])*float(data_action[2])/100
            actions.append(data_dict)
    return actions


def attribute_combination(combination: tuple) -> tuple:
    """ retourne le prix, le profit et les noms d'une combinaison d'actions """
    actions_name = []
    total_price = 0
    total_profit = 0
    for action in combination:
        total_price = total_price + action['price']
        total_profit = total_profit + action['profit']
        actions_name.append(action['name'])
    return total_price, total_profit, actions_name


def main():
    start_time = time.time()
    actions = get_data_actions('actions.csv')
    budget_max = 500
    best_combination = {'profit': 0}
    for nb_actions in range(1, len(actions)+1):
        for combination in itertools.combinations(actions, nb_actions):
            item_combination = attribute_combination(combination)
            total_price = item_combination[0]
            if total_price > budget_max:
                continue
            total_profit = item_combination[1]
            if total_profit > best_combination['profit']:
                best_combination['actions'] = item_combination[2]
                best_combination['profit'] = total_profit
                best_combination['price'] = total_price

    print(f"Total cost: {round(best_combination['price'], 2)}")
    print(f"Profit: {round(best_combination['profit'], 2)}")
    print(f"Combination: {best_combination['actions']}")
    print(f"Execution time: {(time.time() - start_time)} seconds")


if __name__ == "__main__":
    main()
