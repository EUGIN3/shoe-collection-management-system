# -------------- Imports -------------- #
import string, random, json

# -------------- Start Shoe Class -------------- #
class CollectableShoe:
    # --------- __init__ start --------- #
    def __init__(self, shoe_id, brand, quaitity, rarity_lvl, model, starting_price=0):
        self.__shoe_id = shoe_id.upper()
        self.__brand = brand.lower()
        self.__quantity = quaitity
        self.__rarity_lvl = rarity_lvl.lower()
        self.__model = model.lower()
        self.__starting_price = starting_price
    # --------- __init__ end --------- #

    # --------- get_shoe_id start --------- #
    def get_shoe_id(self):
        return self.__shoe_id
    # --------- get_shoe_id end --------- #

    # --------- get_brand start --------- #
    def get_brand(self):
        return self.__brand
    # --------- get_brand end --------- #

    # --------- get_quantity start --------- #
    def get_quantity(self):
        return self.__quantity
    # --------- get_quantity end --------- #

    # --------- get_rarity start --------- #
    def get_rarity(self):
        return self.__rarity_lvl
    # --------- get_rarity end --------- #

    # --------- get_price start --------- #
    def get_price(self):
        return self.__starting_price
    # --------- get_price end --------- #

    # --------- get_model start --------- #
    def get_model(self):
        return self.__model
    # --------- get_model end --------- #

    # --------- display_shoe_info start --------- #
    def display_shoe_info(self):
        message = f"\nID : {self.__shoe_id}\
                    \nBrand : {self.__brand}\
                    \nModel : {self.__model}\
                    \nQuantity : {self.__quantity}\
                    \nRarity : {self.__rarity_lvl}\
                    \nPrice : $ {self.__starting_price}"

        return message
    # --------- display_shoe_info end --------- #

    # --------- checking_admin_action start --------- #
    def checking_admin_action(self):
        deciding = True
        while deciding:
            decesion = input("\nContinue [Y/N] : ")

            if decesion.lower() == "y":
                return True

            elif decesion.lower() == "n":
                return False

            else:
                print("\n===== INVALID INPUT =====")
    # --------- checking_admin_action end --------- #

    # --------- change_brand start --------- #
    def change_brand(self):
        print(f"\nRegistered brand : {self.__brand}")
        
        print('\n>> Press \"q\" to back <<')

        new_brand = input("\nEnter new brand : ").lower().strip()


        if new_brand != 'q':
            admin_decision = self.checking_admin_action() 

            if admin_decision == True:
                self.__brand = new_brand
    # --------- change_brand end --------- #

    # --------- change_quantity start --------- #
    def change_quantity(self):
        print(f"\nCurrent quantity : {self.__quantity}")

        changing_quantity = True

        print('\n>> Press \"q\" to back <<')

        while changing_quantity:
            try:
                new_quantity = input("\nEnter new quantity : ")

                n_q = int(new_quantity)

                if new_quantity.lower() == 'q':
                    changing_quantity = False
                    break 

                elif self.checking_admin_action():

                    if n_q >= 0:
                        self.__quantity = n_q
                        changing_quantity = False
                        break

                    else:
                        print("\n===== You have entered invalid quantity =====")

                else:
                    changing_quantity = False
                    break

            except ValueError:
                print("\n-- You have entered invalid quantity --")
    # --------- change_quantity end --------- #

    # --------- change_rarity_lvl start --------- #
    def change_rarity_lvl(self):
        print(f"\nCurrent rarity : {self.__rarity_lvl}")
        changing_rarity = True

        print('\n>> Press \"q\" to back <<')

        while changing_rarity:
            print("\nChoose new rarity \n[1] - Common \n[2] - Uncommon \n[3] - Rare")

            new_rarity = input("\nEnter new rarity : ").lower().strip()

            if self.checking_admin_action():

                if new_rarity == "1":
                    self.__rarity_lvl = 'common'
                    changing_rarity = False
                    break

                elif new_rarity == "2":
                    self.__rarity_lvl = 'uncommon'
                    changing_rarity = False
                    break

                elif new_rarity == "3":
                    self.__rarity_lvl = 'rare'
                    changing_rarity = False
                    break

                elif new_rarity == 'q':
                    changing_rarity = False
                    break

                else:
                    print("\n===== INVALID INPUT =====")

            else:
                changing_rarity = False
                break
    # --------- change_rarity_lvl end --------- #

    # --------- change_model start --------- #
    def change_model(self):
        print(f"\nRegistered model : {self.__model}")

        print('\n>> Press \"q\" to back <<')

        new_model = input("\nEnter new model : ").lower().strip()


        if new_model != 'q':
            admin_decision = self.checking_admin_action()

            if admin_decision == True:
                self.__brand = new_model
    # --------- change_model end --------- #

    # --------- change_starting_price start --------- #
    def change_starting_price(self):
        print(f"\nCurrent starting price : {self.__starting_price}")

        changing_price = True

        print('\n>> Press \"q\" to back <<')

        while changing_price:
            try:
                new_price = input("\nEnter new starting_price : ").lower().strip()

                s_p = float(new_price)

                if new_price == 'q':
                    changing_price = False
                    break

                elif self.checking_admin_action():

                    if s_p >= 0:
                        self.__quantity = s_p
                        changing_price = False
                        break

                    else:
                        print("\n===== You have entered invalid amount =====")

                else:
                    changing_price = False
                    break

            except ValueError:
                print("\n===== You have entered invalid amount =====")
    # --------- change_starting_price end --------- #
    
    # --------- change_shoe_data start --------- #
    def change_shoe_data(self):
        changing_vintage = True

        while changing_vintage:
            print('\nSelect data want to change : \
                   \n[1] Shoe Brand\
                   \n[2] Quatity\
                   \n[3] Rarity\
                   \n[4] Model\
                   \n[5] Starting Price\
                   \n[0] Back')
            
            user_input = input("\n>> ").strip()

            if user_input == '1' or\
            user_input == '2' or\
            user_input == '3' or\
            user_input == '4' or\
            user_input == '5'or\
            user_input == '0':
                
                valid_input = True
                break
            
            else:
                print('\n===== INVALID INPUT =====')

        if user_input == '1' and valid_input:
            self.change_brand()

        elif user_input == '2' and valid_input:
            self.change_quantity()

        elif user_input == '3' and valid_input:
            self.change_rarity_lvl()

        elif user_input == '4' and valid_input:
            self.change_model()

        elif user_input == '5' and valid_input:
            self.change_starting_price()

        elif user_input == '0' and valid_input:
            return 'cancel'
    # --------- change_shoe_data end --------- #
# -------------- End Shoe Class -------------- #


# -------------- Start Vintage Class -------------- #
class Vintage(CollectableShoe):
    # --------- __init__ start --------- #
    def __init__(self, shoe_id, brand, quaitity, rarity_lvl, model, year, starting_price=0):
        super().__init__(shoe_id, brand, quaitity, rarity_lvl, model, starting_price)
        self.__year = year
        self.shoe_type = 'vintage'
    # --------- __init__ end --------- #

    # --------- get_year start --------- #
    def get_year(self):
        return self.__year
    # --------- get_year end --------- #

    # --------- display_shoe_info start --------- #
    def display_shoe_info(self):
        message = f"\nYear :{self.__year}"

        return super().display_shoe_info() + message
    # --------- display_shoe_info end --------- #

    # --------- change_year start --------- #
    def change_year(self):
        print(f"\nCurrent year : {self.__year}")

        print('\n>> Press \"q\" to back <<')

        new_year = input("\nEnter new year : ").lower().strip()

        if self.checking_admin_action() and new_year != 'q':
            self.__year = new_year
    # --------- change_year end --------- #
    
    # --------- change_shoe_data start --------- #
    def change_shoe_data(self):
            changing_vintage = True

            while changing_vintage:
                print('\nSelect data want to change : \
                    \n[1] Shoe Brand\
                    \n[2] Quatity\
                    \n[3] Rarity\
                    \n[4] Model\
                    \n[5] Year\
                    \n[6] Starting Price\
                    \n[0] Back')
                
                user_input = input("\n>> ").strip()
                if user_input == '1' or\
                user_input == '2' or\
                user_input == '3' or\
                user_input == '4' or\
                user_input == '5' or\
                user_input == '6' or\
                user_input == '0':
                    
                    valid_input = True
                    break
                
                else:
                    print('\n===== INVALID INPUT =====')

            if user_input == '1' and valid_input:
                self.change_brand()

            elif user_input == '2' and valid_input:
                self.change_quantity()

            elif user_input == '3' and valid_input:
                self.change_rarity_lvl()

            elif user_input == '4' and valid_input:
                self.change_model()

            elif user_input == '5' and valid_input:
                self.change_year()
            
            elif user_input == '6' and valid_input:
                self.change_starting_price()

            elif user_input == '0' and valid_input:
                return 'cancel'
    # --------- change_shoe_data end --------- #
# -------------- End Vintage Class -------------- #


# -------------- Start Athletic Class -------------- #
class Athletic(CollectableShoe):
    # --------- __init__ start --------- #
    def __init__(self, shoe_id, brand, quaitity, rarity_lvl, model, athlete_name, starting_price=0):
        super().__init__(shoe_id, brand, quaitity, rarity_lvl, model, starting_price)
        self.__athlete_name = athlete_name.lower()
        self.shoe_type = 'athletic'
    # --------- __init__ end --------- #

    # --------- get_owner start --------- #
    def get_owner(self):
        return self.__athlete_name
    # --------- get_owner end --------- #

    # --------- display_shoe_info start --------- #
    def display_shoe_info(self):
        message = f"\nShoe owner : {self.__athlete_name}"

        return super().display_shoe_info() + message
    # --------- display_shoe_info end --------- #

    # --------- change_owner start --------- #
    def change_owner(self):
        print(f"\nCurrent owner : {self.__year}")

        print('\n>> Press \"q\" to back <<')

        new_owner = input("\nEnter new owner : ").lower().strip()

        if self.checking_admin_action() and new_owner != 'q':
            self.__athlete_name = new_owner
    # --------- change_owner end --------- #

    # --------- change_shoe_data start --------- #
    def change_shoe_data(self):
            changing_vintage = True

            while changing_vintage:
                print('\nSelect data want to change : \
                    \n[1] Shoe Brand\
                    \n[2] Quatity\
                    \n[3] Rarity\
                    \n[4] Model\
                    \n[5] Owner\
                    \n[6] Starting Price\
                    \n[0] Back')
                
                user_input = input("\n>> ").strip()

                if user_input == '1' or\
                user_input == '2' or\
                user_input == '3' or\
                user_input == '4' or\
                user_input == '5' or\
                user_input == '6' or\
                user_input == '0':
                    
                    valid_input = True
                    break
                
                else:
                    print('\n===== INVALID INPUT =====')

            if user_input == '1' and valid_input:
                self.change_brand()

            elif user_input == '2' and valid_input:
                self.change_quantity()

            elif user_input == '3' and valid_input:
                self.change_rarity_lvl()

            elif user_input == '4' and valid_input:
                self.change_model()

            elif user_input == '5' and valid_input:
                self.change_owner()

            elif user_input == '6' and valid_input:
                self.change_starting_price()

            elif user_input == '0' and valid_input:
                return 'cancel'
    # --------- change_shoe_data end --------- #
# -------------- End Athletic Class -------------- #


# -------------- Start Designer Class -------------- #
class Designer(CollectableShoe):
    # --------- __init__ start --------- #
    def __init__(self, shoe_id, brand, quaitity, rarity_lvl, model, material, starting_price=0):
        super().__init__(shoe_id, brand, quaitity, rarity_lvl, model, starting_price)
        self.__material = material.lower()
        self.shoe_type = 'designer'
    # --------- __init__ end --------- #
    
    # --------- get_material start --------- #
    def get_material(self):
        return self.__material
    # --------- get_material start --------- #

    # --------- display_shoe_info start --------- #
    def display_shoe_info(self):
        message = f"\nMaterial Used : {self.__material}"

        return super().display_shoe_info() + message
    # --------- display_shoe_info start --------- #

    # --------- change_material start --------- #
    def change_material(self):
        print(f"\nCurrent material : {self.__material}")

        print('\n>> Press \"q\" to back <<')

        new_matrial = input("\nEnter material : ").lower().strip()

        if self.checking_admin_action() and new_matrial != 'q':
            self.__material = new_matrial
    # --------- change_material start --------- #    

    # --------- change_shoe_data start --------- #
    def change_shoe_data(self):
            changing_vintage = True

            while changing_vintage:
                print('\nSelect data want to change : \
                    \n[1] Shoe Brand\
                    \n[2] Quatity\
                    \n[3] Rarity\
                    \n[4] Model\
                    \n[5] Material\
                    \n[6] Starting Price\
                    \n[0] Back')
                
                user_input = input("\n>> ").strip()
                if user_input == '1' or\
                user_input == '2' or\
                user_input == '3' or\
                user_input == '4' or\
                user_input == '5' or\
                user_input == '6' or\
                user_input == '0':
                    
                    valid_input = True
                    break
                
                else:
                    print('\n===== INVALID INPUT =====')

            if user_input == '1' and valid_input:
                self.change_brand()

            elif user_input == '2' and valid_input:
                self.change_quantity()

            elif user_input == '3' and valid_input:
                self.change_rarity_lvl()

            elif user_input == '4' and valid_input:
                self.change_model()

            elif user_input == '5' and valid_input:
                self.change_material()
            
            elif user_input == '6' and valid_input:
                self.change_starting_price()

            elif user_input == '0' and valid_input:
                return 'cancel'
    # --------- change_shoe_data start --------- #
# -------------- End Designer Class -------------- #


# -------------- Start Shoe Management -------------- #
class ShoeManagement:
    # --------- __init__ start --------- #
    def __init__(self, filename_shoe='shoe_closet.json'):
        self.vintage_pairs = []
        self.athletic_pairs = []
        self.designer_pairs = []
        self.__password = '1'
        self.filename_shoe = filename_shoe
    # --------- __init__ end --------- #

    # --------- invalid_design start --------- #
    def invalid_design(self, invalid_msg):
        print()
        for i in range(10):
            print("=", end="")
            if i == 4:
                print(f"  {invalid_msg.upper()}  ", end="")
        print()
    # --------- invalid_design end --------- #
    
    # --------- heading_design start --------- #
    def heading_design(self, text):
        print()
        for i in range(20):
            print("=", end="")
            if i == 9:
                print(f"  {text.title()}  ", end="")
        print('')
    # --------- heading_design end --------- #

    # --------- random_id start --------- #
    def random_id(self):
        alphabet = string.ascii_uppercase
        random_index = random.randint(0, 3)
        random_id = ''

        for index in range(4):

            if random_index == index:
                random_id += random.choice(alphabet)

            else:
                random_id += str(random.randint(1, 9))
        
        return random_id
    # --------- random_id end --------- #

    # --------- check_password start --------- #
    def check_password(self):
        incorrect_password = True
        incorrect_count = 0

        while incorrect_password == True:
            
            entered_pass = input("Enter password : ")

            if entered_pass.lower() == "q" and incorrect_count >= 3:
                incorrect_password = False
                return False
            
            if entered_pass == self.__password:
                incorrect_password = False
                return True

            else:
                incorrect_count += 1
                self.invalid_design('invalid password')

                if incorrect_count >= 3:
                    print(">> Press \"q\" to quit <<")
    # --------- check_password end --------- #

    # --------- save_changes start --------- #
    def save_changes(self):
        sure = self.making_sure('Do you want to save changes permanently')

        if sure:
            self.save_json_shoe()
    # --------- save_changes end --------- #

    # --------- display_all_shoe start --------- #
    def display_all_shoe(self, user):
        self.error_load = "Try to load data."

        self.heading_design('vintage shoes')
        if not self.vintage_pairs:
            print('No Vintage pairs stored in closet.')
            if user == 'admin':
                print(self.error_load)
        else:
            for every_vin in self.vintage_pairs:
                print(every_vin.display_shoe_info())

        
        self.heading_design('athletic shoes')
        if not self.athletic_pairs:
            print('No Athletic pairs stored in closet.')
            if user == 'admin':
                print(self.error_load)
        else:
            for every_ath in self.athletic_pairs:
                print(every_ath.display_shoe_info())

        self.heading_design('designer shoes')
        if not self.designer_pairs:
            print('No Desinger pairs stored in closet.')
            if user == 'admin':
                print(self.error_load)
        else:
            for every_des in self.designer_pairs:
                print(every_des.display_shoe_info())

        self.display_shoe_menu(user)
    # --------- display_all_shoe end --------- #

    # --------- display_shoe start --------- #
    def display_shoe(self, shoe_type, user):
        self.error_load = "Try to load data."
        if shoe_type == 'vintage':
            self.invalid_design('vintage shoes')
            if not self.vintage_pairs:
                print('No Vintage pairs stored in closet.')
                if user == 'admin':
                    print(self.error_load)
            else:
                for every_vintage in self.vintage_pairs:
                    print(every_vintage.display_shoe_info())
        
        elif shoe_type == 'athletic':
            self.invalid_design('athletic shoes')
            if not self.athletic_pairs:
                print('No Athletic pairs stored in closet.')
                if user == 'admin':
                    print(self.error_load)
            else:
                for every_athletic in self.athletic_pairs:
                    print(every_athletic.display_shoe_info())

        elif shoe_type == 'designer':
            self.invalid_design('designer shoes')
            if not self.designer_pairs:
                print('No Designer pairs stored in closet.')
                if user == 'admin':
                    print(self.error_load)
            else:
                for every_designer in self.designer_pairs:
                    print(every_designer.display_shoe_info())
    # --------- display_shoe end --------- #

    # --------- display_shoe_menu start --------- #
    def display_shoe_menu(self, user):
        displaying_shoe = True

        while displaying_shoe:
            self.heading_design("Displaying shoe")
            print("\nSelect action :\
                  \n[1] - Display all shoe\
                  \n[2] - Display individual shoe type\
                  \n[0] - Back")
            
            user_input = input("\n>> ")
            
            if user_input == '1' or user_input == '2' or user_input == '0':
                valid_input = True
                break

            else:
                self.invalid_design('invalid input')

        if user_input == '1' and valid_input:
            self.display_all_shoe(user)

        elif user_input == '2' and valid_input:
            choosing_shoe_type = True

            while choosing_shoe_type:
                self.heading_design('DISPLAYING SHOE')
                print("\nSelect shoe type :\
                    \n[1] - Vintage\
                    \n[2] - Athletic\
                    \n[3] - Designer\
                    \n[0] - Back")

                user_input_shoe_t = input("\n>> ")

                if user_input_shoe_t == '1':
                    self.display_shoe('vintage', user)

                elif user_input_shoe_t == '2':
                    self.display_shoe('athletic', user)

                elif user_input_shoe_t == '3':
                    self.display_shoe('designer', user)

                elif user_input_shoe_t == '0':
                    choosing_shoe_type = False
                    displaying_shoe = True
                    self.display_shoe_menu(user)
                    break
                else:
                    self.invalid_design('invalid input')
                    
            
        elif user_input == '0' and valid_input and user == 'admin':
            self.admin_menu()

        elif user_input == '0' and valid_input and user == 'viewer':
            self.viewer_menu()
    # --------- display_shoe_menu end --------- #

    # --------- search_shoe start --------- #
    def search_shoe(self, shoe_id):
        for every_vintage in self.vintage_pairs:
            if every_vintage.get_shoe_id() == shoe_id:
                found_shoe_vin = every_vintage
                return found_shoe_vin
            
        for every_athletic in self.athletic_pairs:
            if every_athletic.get_shoe_id() == shoe_id:
                found_shoe_ath = every_athletic
                return found_shoe_ath
            
        for every_designer in self.designer_pairs:
            if every_designer.get_shoe_id() == shoe_id:
                found_shoe_dis = every_designer
                return found_shoe_dis

        self.invalid_design('Shoe not found')

        return "not_found"
    # --------- search_shoe end --------- #

    # --------- search_shoe_model start --------- #
    def search_shoe_model(self, model):
        for every_vintage in self.vintage_pairs:
            if every_vintage.get_model() == model:
                found_shoe_vin = every_vintage
                return found_shoe_vin
            
        for every_athletic in self.athletic_pairs:
            if every_athletic.get_model() == model:
                found_shoe_ath = every_athletic
                return found_shoe_ath
            
        for every_designer in self.designer_pairs:
            if every_designer.get_model() == model:
                found_shoe_dis = every_designer
                return found_shoe_dis

        return "not_found"
    # --------- search_shoe_model end --------- #

    # --------- search_shoe_menu start --------- #
    def search_shoe_menu(self):
        searching_shoe = True

        while searching_shoe:
            self.heading_design('Searching')
            print('\n>> Press \"q\" to back <<')
            
            shoe_id_inputed = input('Enter shoe id : ').upper().strip()
            
            if len(shoe_id_inputed) == 4:
                shoe = self.search_shoe(shoe_id_inputed)

                if shoe == 'not_found':
                    continue

                else:
                    return shoe

            elif shoe_id_inputed == "Q":
                searching_shoe = True
                return False

            else:
                self.invalid_design('invalid id')
    # --------- search_shoe_menu end --------- #

    # --------- rarity_level start --------- #
    def rarity_level(self):
        choosing_rarity = True

        while choosing_rarity:
            print("\n Choose rarity : \
                  \n[1] - Common \
                  \n[2] - Uncommon \
                  \n[3] - Rare")
            
            rarity = input("\n>> ").strip()
            
            if rarity == "1":
                return "common"
            
            elif rarity == "2":
                return "uncommon"
            
            elif rarity == "3":
                return "rare"
            
            elif rarity == "q":
                return 'q'
            
            else:
                self.invalid_design('invalid input')
    # --------- rarity_level end --------- #

    # --------- making_sure start --------- #
    def making_sure(self, text):
        making_sure = True

        while making_sure:
            sure = input(f"\n{text} [Y/N]? : ").lower().strip()

            if sure == 'y' or sure == "yes":
                making_sure = False
                return True
            elif sure == "n" or sure == "no":
                making_sure = False
                self.invalid_design('Action canceled!')
            else:
                self.invalid_design('invalid input')
    # --------- making_sure end --------- #

    # --------- add_shoe_menu start --------- #
    def add_shoe_menu(self):
        adding_shoe = True

        while adding_shoe:
            self.heading_design('adding shoe')
            print("\nSelect shoe type :\
                   \n[1] - Vintage\
                   \n[2] - Athletic\
                   \n[3] - Designer\
                   \n[0] - Back")

            shoe_type = input("\n>> ").strip()

            if shoe_type == '1' or \
                shoe_type == '2' or \
                shoe_type == '3' or \
                shoe_type == '0':

                valid_input = True
                break

            else:
                self.invalid_design('invalid input')

        if shoe_type == "1" and valid_input == True:
            self.add_vintage_pair()

        elif shoe_type == "2" and valid_input:
            self.add_athletic_pair()

        elif shoe_type == "3" and valid_input:
            self.add_designer_shoe()

        elif shoe_type == "0" and valid_input:
            self.admin_menu()
    # --------- add_shoe_menu end --------- #

    # --------- q_is_press start --------- #
    def q_is_press(self, _input):
        if _input.lower() == 'q':
            return True
        else:
            return False
    # --------- q_is_press end --------- #

    # --------- add_vintage_pair start --------- #
    def add_vintage_pair(self):
        self.heading_design('Adding Vintage Pair')
        quited = False

        print(">> Press \"q\" to back <<")
        adding_vintage = True
        wrong_quan = True
        wrong_price = True
        while adding_vintage:
            shoe_id = self.random_id()
            shoe_brand = input("\nEnter brand name : ").strip().lower()

            if self.q_is_press(shoe_brand):
                quited = True
                wrong_quan = False
                wrong_price = False
                break

            shoe_rarity = self.rarity_level()

            if self.q_is_press(shoe_rarity):
                quited = True
                wrong_quan = False
                wrong_price = False
                break
            
            model = input("Enter shoe model : ").strip().lower()

            if self.q_is_press(model):
                quited = True
                wrong_quan = False
                wrong_price = False
                break
            
            search_model = self.search_shoe_model(model)

            if search_model == "not_found":
                year = input("Enter year released : ").strip().lower()

                if self.q_is_press(year):
                    quited = True
                    wrong_quan = False
                    wrong_price = False
                    break
                break
            else:
                self.invalid_design("model already existed")

        while wrong_quan: 
            try:
                s_q = input("Enter the qauntity : ")
                
                if self.q_is_press(s_q):
                    quited = True
                    wrong_quan = False
                    wrong_price = False
                    break
                
                shoe_quantity = int(s_q)
                break

            except ValueError:
                self.invalid_design('you entered invalid quantity')

        while wrong_price:
            try: 
                s_p = input("Enter the starting price : ").lower()

                if self.q_is_press(s_p):
                    quited = True
                    wrong_price = False
                    break

                shoe_price = float(s_p)
                break

            except ValueError:
                self.invalid_design('you entered invalid amount')

        if quited == False:
            text = "Adding shoe"
            sure = self.making_sure(text)
            if sure:
                adding_shoe = "vintage"

                vintage_shoe_obj = Vintage(shoe_id, shoe_brand, shoe_quantity, shoe_rarity, model, year, shoe_price)

                self.add_shoe(adding_shoe, vintage_shoe_obj)
                self.add_shoe_menu()

            else:
                self.add_shoe_menu()

        else:
            self.add_shoe_menu()
    # --------- add_vintage_pair end --------- #
            
    # --------- add_athletic_pair start --------- #
    def add_athletic_pair(self):
        self.heading_design('Adding Athletic Pair')
        print(">> Press \"q\" to back <<")
        quited = False
        wrong_quan = True
        wrong_price = True

        adding_athletic = True

        while adding_athletic:
            shoe_id = self.random_id()
            shoe_brand = input("\nEnter brand name : ").strip().lower()

            if self.q_is_press(shoe_brand):
                quited = True
                wrong_quan = False
                wrong_price = False
                break

            shoe_rarity = self.rarity_level()
            
            if self.q_is_press(shoe_rarity):
                quited = True
                wrong_quan = False
                wrong_price = False
                break

            model = input("Enter shoe model : ").strip().lower()

            if self.q_is_press(model):
                quited = True
                wrong_quan = False
                wrong_price = False
                break

            search_model = self.search_shoe_model(model)

            if search_model == "not_found":
                athletic_name = input("Enter shoe owner : ").strip().lower()

                if self.q_is_press(athletic_name):
                    quited = True
                    wrong_quan = False
                    wrong_price = False
                    break

                break

        while wrong_quan: 
            try:
                s_q = input("Enter the qauntity : ")
                
                if self.q_is_press(s_q):
                    quited = True
                    wrong_quan = False
                    wrong_price = False
                    break
                
                shoe_quantity = int(s_q)
                break

            except ValueError:
                self.invalid_design('you entered invalid quantity')

        while wrong_price:
            try: 
                s_p = input("Enter the starting price : ").lower()

                if self.q_is_press(s_p):
                    quited = True
                    wrong_price = False
                    break

                shoe_price = float(s_p)
                break

            except ValueError:
                self.invalid_design('you entered invalid amount')

        if quited == False:
            text = "Adding shoe"
            sure = self.making_sure(text)
            if sure:
                adding_shoe = "athletic"

                athletic_shoe_obj = Athletic(shoe_id, shoe_brand, shoe_quantity, shoe_rarity, model, athletic_name, shoe_price)

                self.add_shoe(adding_shoe, athletic_shoe_obj)
                self.add_shoe_menu()

            else:
                self.add_shoe_menu()
        else:
            self.add_shoe_menu()
    # --------- add_athletic_pair end --------- #

    # --------- add_designer_shoe start --------- #
    def add_designer_shoe(self):
        self.heading_design('Adding Designer Pair')
        print(">> Press \"q\" to back <<")
        quited = False
        wrong_quan = True
        wrong_price = True

        adding_designer = True
        while adding_designer:
            shoe_id = self.random_id()
            shoe_brand = input("\nEnter brand name : ").strip().lower()

            if self.q_is_press(shoe_brand):
                quited = True
                wrong_quan = False
                wrong_price = False
                break

            shoe_rarity = self.rarity_level()
            
            if self.q_is_press(shoe_rarity):
                quited = True
                wrong_quan = False
                wrong_price = False
                break

            model = input("Enter shoe model : ").strip().lower()

            if self.q_is_press(model):
                quited = True
                wrong_quan = False
                wrong_price = False
                break

            search_model = self.search_shoe_model(model)

            if search_model == "not_found":
                shoe_material = input("Enter shoe material : ").strip().lower()

                if self.q_is_press(shoe_material):
                    quited = True
                    wrong_quan = False
                    wrong_price = False
                    break

                break

        while wrong_quan: 
            try:
                s_q = input("Enter the qauntity : ")
                
                if self.q_is_press(s_q):
                    quited = True
                    wrong_quan = False
                    wrong_price = False
                    break
                
                shoe_quantity = int(s_q)
                break

            except ValueError:
                self.invalid_design('you entered invalid quantity')

        while wrong_price:
            try: 
                s_p = input("Enter the starting price : ").lower()

                if self.q_is_press(s_p):
                    quited = True
                    wrong_price = False
                    break

                shoe_price = float(s_p)
                break

            except ValueError:
                self.invalid_design('you entered invalid amount')

        if quited == False:
            text = "Adding shoe"
            sure = self.making_sure(text)
            if sure:
                adding_shoe = "designer"

                designer_shoe_obj = Designer(shoe_id, shoe_brand, shoe_quantity, shoe_rarity, model, shoe_material, shoe_price)

                self.add_shoe(adding_shoe, designer_shoe_obj)
                self.add_shoe_menu()

            else:
                self.add_shoe_menu()
        else:
            self.add_shoe_menu()
    # --------- add_designer_shoe end --------- #

    # --------- add_shoe start --------- #
    def add_shoe(self, shoe_type, shoe):
        text = "Shoe added successfully added!"

        if shoe_type == "vintage":
            self.vintage_pairs.append(shoe)
            self.heading_design(text)

        elif shoe_type == "athletic":
            self.athletic_pairs.append(shoe)
            self.heading_design(text)

        elif shoe_type == "designer":
            self.designer_pairs.append(shoe)
            self.heading_design(text)
        
        self.save_changes()
    # --------- add_shoe end --------- #

    # --------- remove_shoe_menu start --------- #
    def remove_shoe_menu(self):
        if not self.athletic_pairs and not self.vintage_pairs and not self.designer_pairs:
            self.invalid_design('no shoes in recorded')
            print("Make sure to load data first!")
            self.admin_menu()
        else:
            removing_shoe = True

            self.heading_design('removing shoe from')
            found = self.search_shoe_menu()

            if found != False:
                while removing_shoe:
                    text = f"Deleting {found.get_shoe_id()}"
                    sure = self.making_sure(text)

                    if sure:
                        shoe_t = found.shoe_type
                        self.remove_shoe(shoe_t, found) 

                        self.invalid_design('Shoe successesfully deleted')
                        self.admin_menu()
                        break

                    else:
                        removing_shoe = False
                        self.admin_menu()
                        break

            elif found == False:
                self.admin_menu()
    # --------- remove_shoe_menu end --------- #

    # --------- remove_shoe start --------- #
    def remove_shoe(self, shoe_type, shoe):
        if shoe_type == "vintage":
            self.vintage_pairs.remove(shoe)

        elif shoe_type == "athletic":
            self.athletic_pairs.remove(shoe)

        elif shoe_type == "designer":
            self.designer_pairs.remove(shoe)
        
        self.save_changes()
    # --------- remove_shoe end --------- #

    # --------- change_shoe_data_menu start --------- #
    def change_shoe_data_menu(self):
        if not self.athletic_pairs and not self.vintage_pairs and not self.designer_pairs:
            self.invalid_design('no shoes in recorded')
            print("Make sure to load data first!")
            self.admin_menu()
        else:
            self.heading_design('changing shoe data')

            found_shoe = self.search_shoe_menu()     
            
            if found_shoe != False:
                self.change_shoe_details(found_shoe)

            else:
                self.admin_menu()
    # --------- change_shoe_data_menu end --------- #

    # --------- change_shoe_details start --------- #
    def change_shoe_details(self, shoe):
        c_d = shoe.change_shoe_data()
        if not c_d:
            self.save_changes()

        self.admin_menu()

    # --------- change_shoe_details end --------- #
        
    # --------- save_json_shoe start --------- #
    def save_json_shoe(self):
        shoe_list = {
            'vintage' : [{'shoe_id' : every_vintage.get_shoe_id(),'brand' : every_vintage.get_brand(),  'quantity' : every_vintage.get_quantity(),
              'rarity' : every_vintage.get_rarity(), 'model' : every_vintage.get_model(),'year_released' : every_vintage.get_year(),
              'price' : every_vintage.get_price()} for every_vintage in self.vintage_pairs],

            'athletic' : [{'shoe_id' : every_athletic.get_shoe_id(),'brand' : every_athletic.get_brand(),'quantity' : every_athletic.get_quantity(),
              'rarity' : every_athletic.get_rarity(),'model' : every_athletic.get_model() ,'owner' : every_athletic.get_owner(),
              'price' : every_athletic.get_price()} for every_athletic in self.athletic_pairs],

            'designer' : [{'shoe_id' : every_designer.get_shoe_id(),'brand' : every_designer.get_brand(),'quantity' : every_designer.get_quantity(),
              'rarity' : every_designer.get_rarity(),'model' : every_designer.get_model() ,'material' : every_designer.get_material(),
              'price' : every_designer.get_price()} for every_designer in self.designer_pairs]
        }

        with open(file=self.filename_shoe, mode='w') as j_f:
            json.dump({'vintage' : shoe_list.get('vintage'), 'athletic' : shoe_list.get('athletic'), 'designer' : shoe_list.get('designer')}, j_f, indent=2)

        self.invalid_design(f"Data successfully saved to {self.filename_shoe}")
    # --------- save_json_shoe end --------- #

    # --------- load_json_shoe start --------- #
    def load_json_shoe(self, user):
        try:
            with open(file=self.filename_shoe, mode='r') as j_f:
                shoes_in_json = json.load(j_f)

                self.vintage_pairs = [Vintage(every_shoe['shoe_id'], every_shoe['brand'], every_shoe['quantity'], 
                                            every_shoe['rarity'],every_shoe['model'] , every_shoe['year_released'], 
                                            every_shoe['price']) for every_shoe in shoes_in_json.get('vintage')]

                self.athletic_pairs = [Athletic(every_shoe['shoe_id'], every_shoe['brand'], every_shoe['quantity'], 
                                                every_shoe['rarity'],every_shoe['model'], every_shoe['owner'], 
                                                every_shoe['price']) for every_shoe in shoes_in_json.get('athletic')]

                self.designer_pairs = [Designer(every_shoe['shoe_id'], every_shoe['brand'], every_shoe['quantity'], 
                                                every_shoe['rarity'],every_shoe['model'], every_shoe['material'], 
                                                every_shoe['price']) for every_shoe in shoes_in_json.get('designer')]
            
            if user == 'admin':
                self.invalid_design(f"Data successfully loaded from {self.filename_shoe}")
        except FileNotFoundError:
            self.save_json_shoe()

    # --------- load_json_shoe end --------- #

    # --------- admin_menu start --------- #
    def admin_menu(self):
        admin_continuing = True

        while admin_continuing:
            self.heading_design('admin')
            print("\nSelect action:\
                   \n[1] - Display Shoes\
                   \n[2] - Add Shoes\
                   \n[3] - Remove Shoes\
                   \n[4] - Change Shoe Details\
                   \n[5] - Save to JSON\
                   \n[6] - Load JSON\
                   \n[0] - Back")

            admin_choice = input("\n>> ").strip()

            if admin_choice == '1' or admin_choice == '2' or \
                admin_choice == '3' or admin_choice == '4' or \
                admin_choice == '0':

                valid_choice = True
                break

            elif admin_choice == "5":
                self.save_json_shoe()

            elif admin_choice == "6":
                self.load_json_shoe('admin')

            else:
                self.invalid_design('invalid input')

        if admin_choice == "1" and valid_choice:
            self.display_shoe_menu('admin')

        elif admin_choice == "2" and valid_choice:
            self.add_shoe_menu()

        elif admin_choice == "3" and valid_choice:
            self.remove_shoe_menu()

        elif admin_choice == "4" and valid_choice:
            self.change_shoe_data_menu()

        elif admin_choice == "0" and valid_choice:
            self.heading_design('exiting')
            self.vintage_pairs = []
            self.athletic_pairs = []
            self.designer_pairs = []
            self.main_menu()
    # --------- admin_menu end --------- #

    # --------- viewer_menu start --------- #
    def viewer_menu(self):
        self.heading_design("welcome viewer")
        self.load_json_shoe('viewer')
        viewer_continuing = True

        while viewer_continuing:
            self.heading_design('viewer')
            print("\nSelect action:\
                   \n[1] - Display Shoes\
                   \n[0] - Back")

            viewer_choice = input("\n>> ").strip()

            if viewer_choice == '1'or viewer_choice == '0':

                valid_input = True
                break

            else:
                self.invalid_design('invalid input')

        if viewer_choice == "1" and valid_input:
            self.display_shoe_menu('viewer')

        elif viewer_choice == "0" and valid_input:
            self.main_menu()
    # --------- viewer_menu end --------- #

    # --------- main_menu start --------- #
    def main_menu(self):
        continuing_one = True

        while continuing_one:
            self.heading_design('Shoe Collection Information System')
            print("\nSelect profile type:\
                   \n[1] - Admin\
                   \n[2] - Viewer\
                   \n[0] - Exit")

            choose_one = input("\n>> ").strip()
            if choose_one == '1' or choose_one == '2':
                valid_choice = True
                break

            elif choose_one == '0':
                continuing_one = False
                break
        
            else:
                self.invalid_design('invalid input')

        if choose_one == "1" and valid_choice:
            if self.check_password():
                self.heading_design("welcome admin")

                sure = self.making_sure('Do you want to load the data')

                if sure:
                    self.load_json_shoe('admin')
                else:
                    print("\nOk, but to avoid lost of data enter '6' to load data.")

                self.admin_menu()

        elif choose_one == "2" and valid_choice:
            self.viewer_menu()
    # --------- main_menu end --------- #
# -------------- End Shoe Management -------------- #
            

one = ShoeManagement()
one.main_menu()