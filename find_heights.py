"""
@author: Juan Francisco Javier Perez Rivero
"""
import requests
def pairsNBASumEqualTo(array: list, sum_to: int) -> list:
    """
    Given an array of NBAs players, find the number of pairs of players
    whose sum of heights is equal to the given sum_to.
    :param array: list of NBAs players
    :param sum_to: int of the sum ti find pairs of players
    :return: list of pairs of players whose sum of heights is equal to the given sum_to
    """
    heights_map = {}
    results = []
    for element in array:
        element_height = int(element["h_in"])
        sum_to_diff = sum_to - element_height
        if sum_to_diff in heights_map:
            for i in heights_map[sum_to_diff]:
                results.append((i, element))
            
        if element_height in heights_map:
            heights_map[element_height].append(element)
        else:
            heights_map[element_height] = [element]
    return results


respose_raw_data = requests.get('https://mach-eight.uc.r.appspot.com')
resposen_json_data = respose_raw_data.json()
players = resposen_json_data['values']
inches_input = int(input("Heights: "))
result = pairsNBASumEqualTo(players, inches_input)
if(len(result)):
    for pair in result:
        print(pair[0]["first_name"], pair[0]["last_name"], pair[1]["first_name"], pair[1]["last_name"])
else:
    print("No matches found")