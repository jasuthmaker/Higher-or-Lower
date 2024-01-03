import random
import art
import game_data
ran_num = random.randint(0, 51)
print(art.logo)

def account():
    ran_num = random.randint(0, 51)
    a = game_data.data[ran_num]
    return a
def a_data(account):
 ran_name = account['name']
 ran_role = account['description']
 ran_loc = account['country']
 res = print(f"Compare A: {ran_name}, {ran_role}, from {ran_loc}")
 return res

# print(f"Compare A: {ran_name}, {ran_role}, from {ran_loc}")
print(a_data(account()))
print(art.vs)