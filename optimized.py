import argparse
import csv
import time


def get_data_actions(file_name: str) -> list:
    """ retourne la liste des données des actions : nom, prix, profit, rentabilité """
    actions = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        datas = csv.reader(csvfile, delimiter=',', quotechar="'")
        for data_action in list(datas)[1:]:
            if not check_valid_data(data_action):
                continue
            else:
                valid_data = get_valid_data(data_action)
            actions.append(valid_data)
    return actions


def check_valid_data(data_action: list) -> bool:
    """ retourne faux s'il manque une donnée ou si le prix de l'action est <=0  """
    valid_data = True
    if not data_action[0] or not data_action[1] or not data_action[2]:
        return not valid_data
    elif float(data_action[1]) <= 0:
        return not valid_data
    return valid_data


def get_valid_data(data_action: list) -> dict:
    """ retourne les données des actions valides """
    data_dict = {}
    data_dict['name'] = data_action[0]
    data_dict['price'] = float(data_action[1])
    data_dict['profit'] = float(data_action[1])*float(data_action[2])/100
    data_dict['efficiency'] = data_dict['profit']/data_dict['price']
    return data_dict


def main():
    parser = argparse.ArgumentParser(description='Execute le programme optimized.py')
    parser.add_argument('file_name',
                        help="Entrez le nom du fichier csv contenant les données des actions",
                        type=str)
    start_time = time.time()
    budget_max = 500
    total_price = 0
    total_profit = 0
    best_combination = []
    actions = get_data_actions(parser.parse_args().file_name)
    actions = sorted(actions, key=lambda k: k['efficiency'], reverse=True)
    for action in actions:
        if action['efficiency'] <= 0:
            continue
        elif total_price + action['price'] <= budget_max:
            total_price = total_price + action['price']
            total_profit = total_profit + action['profit']
        else:
            continue
        best_combination.append(action['name'])

    print(f"Total cost: {round(total_price, 2)}")
    print(f"Profit: {round(total_profit, 2)}")
    print(f"Combination: {best_combination}")
    print(f"Execution time: {(time.time() - start_time)} seconds")


if __name__ == "__main__":
    main()
