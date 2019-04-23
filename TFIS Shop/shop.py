#!/usr/bin/env python
from json import load, dump, loads
from os import system
from sys import exit
from time import sleep, strftime
import datetime

class PriceError(Exception):
    """
    An error in the price per unit of total cost of a sale.
    """
    def __init__(self, message:str):
        self.message = message


class Item:
    """
    An item for the shop.
    """
    fullName = ""
    amount = 0
    minCost = 0
    def __init__(self, full_name:str = None, amount:int = None, min_cost:int = None):
        if(full_name == None):
            raise InputError("full_name is not defined!")
        else:
            self.fullName = full_name

        if(amount == None):
            raise InputError("amount is not defined!")
        else:
            self.amount = amount

        if(min_cost == None):
            raise InputError("min_cost is not defined!")
        else:
            self.minCost = min_cost

    def sellItem(self):
        """
        Sell one or more of the item.
        """
        if(self.amount == 0):
            print("There are none of this item left!")
        else:
            price = float(input("What was the price per unit? (In dollars)\n> "))
            if(price < self.minCost):
                raise PriceError("Price per unit is too low!")
            else:
                amount_sold = int(input("How many units did the customer buy?\n> "))
                total_cost = float(amount_sold * price)
                if(list(str(total_cost)).index(".") == (len(str(total_cost)) - 2)):
                    check = input("Total cost is ${0}0. Correct amount? [Y/n] ".format(str(total_cost)))
                    if(check == "y" or check == "Y" or check == ""):
                        self.amount -= amount_sold
                        return (total_cost, amount_sold, self.fullName)
                    else:
                        actual = float(input("What was the actual total cost? "))
                        self.amount -= amount_sold
                        return (actual, amount_sold, self.fullName)
                else:
                    check = input("Total cost is ${0}. Correct amount? [Y/n] ".format(str(total_cost)))
                    if(check == "y" or check == "Y" or check == ""):
                        self.amount -= amount_sold
                        return (total_cost, amount_sold, self.fullName)
                    else:
                        actual = float(input("What was the actual total cost? "))
                        self.amount -= amount_sold
                        return (actual, amount_sold, self.fullName)

class Shop:
    """
    A shop
    Attributes:
        name: The name of the shop
        items: A list of Items the shop can sell
        profit: The profit the shop has made
    
    Methods:
        Shop.loop()
            The method which collects and process commands
    """
    name = ""
    tb = ""
    items = []
    profit = 0.0
    
    def __init__(self, name:str = None, items:list = None, profit:float = 0):
        if(name == None):
            raise InputError("name is not defined!")
        elif(items == None):
            raise InputError("items is not defined!")
        else:
            self.profit = profit
            for i in items:
                self.items.append(i)
            self.name = name
            self.tb = self.name + " Shop\n" + "="*int(len(self.name) + 5)
            print(self.tb)
            if(list(str(self.profit)).index(".") == (len(str(self.profit)) - 2)):
                print("Profit: ${0}0\n".format(str(self.profit)))
            else:
                print("Profit: ${0}\n".format(str(self.profit)))
    
    def loop(self):
        """
        Collects and proccess commands
        Commands:
            sale = makes a sale
            items = lists all the items that the shop has
            profit = displays th profit the shop has made
            add = increases the number of a certain item
            save = saves the name, items and profit of a shop to a .shop file
            load = loads the name, items and profit of a shop from a .shop file
            close = saves the name, items and profit of a shop to a .shop file, then terminates the script
            clear = clears the console
            help = displays the help message
        """
        command = input("> ")
        
        if(command == "sale"):
            text = "Enter the number next to the item sold:\n"
            output = None
            for i in range(len(self.items)):
                if(self.items[i].amount == 0):
                    pass
                elif(i == len(self.items)-1):
                    text += "[%s] %s: %s" % (str(i), self.items[i].fullName, self.items[i].amount)
                else:
                    text += "[%s] %s: %s\n" % (str(i), self.items[i].fullName, self.items[i].amount)
            print(text)
            command = input("> ")
            try:
                output = self.items[int(command)].sellItem()
                self.profit += output[0]
                logfile = open("%s_log.txt" % self.name, "a+")
                logfile.write("%s\n==========================\nItem: %s\nAmount: %s\nCost: %s\n\n" % (datetime.datetime.now(), output[2], output[1], output[0]))
                logfile.close()
            except PriceError:
                if(list(str(self.items[int(command)]).index(".") == (len(str(self.items[int(command)])) - 2))):
                    print("Price error: Price per unit is too low. Minimum price per unit is {0}0".format(str(self.items[int(command)].minCost)))
                else:
                    print("Price error: Price per unit is too low. Minimum price per unit is {0}".format(str(self.items[int(command)].minCost)))
            except(IndexError, ValueError):
                print("Invalid number!  Sale canceled!")
            sleep(3)
        
        if(command == "save"):
            name = input("File name: ")
            file = open("{0}.shop".format(name), "w")
            item_json = []
            for i in self.items:
                item_json.append({"name": i.fullName, "amount": i.amount, "min_cost": i.minCost})
            text = {"name": self.name, "profit": self.profit, "items": item_json}
            dump(text, file, separators=(',', ':'), sort_keys=True, indent=4)
            file.close()
            print("File saved!")
            sleep(3)
        
        if(command == "load"):
            name = input("File name: ")
            try:
                file = open("{0}.shop".format(name), "r")
                json_obj = load(file)
                for i in range(len(json_obj["items"])):
                    try:
                        self.items[i].fullName = json_obj["items"][i]["name"]
                        self.items[i].amount = json_obj["items"][i]["amount"]
                        self.items[i].minCost = json_obj["items"][i]["min_cost"]
                    except IndexError:
                        self.items.append(Item(json_obj["items"][i]["name"], json_obj["items"][i]["amount"], json_obj["items"][i]["min_cost"]))
                self.name = json_obj["name"]
                self.tb = self.name + " Shop\n" + "="*int(len(self.name) + 5)
                file.close()
                print("File loaded!")
                sleep(1)
                system("cls")
                print(self.tb)
                if(list(str(self.profit)).index(".") == (len(str(self.profit)) - 2)):
                    print("Profit: ${0}0\n".format(str(self.profit)))
                else:
                    print("Profit: ${0}\n".format(str(self.profit)))
            except FileNotFoundError:
                print("File does not exist!")
                sleep(3)
        
        if(command == "close"):
            file_name = str(input("File name: "))
            file = open("{0}.shop".format(file_name), "w")
            item_json = []
            for i in self.items:
                item_json.append({"name": i.fullName, "amount": i.amount, "min_cost": i.minCost})
            text = {"name": self.name, "profit": self.profit, "items": item_json}
            dump(text, file, separators=(',', ':'), sort_keys=True, indent=4)
            file.close()
            if(list(str(self.profit)).index(".") == (len(str(self.profit)) - 2)):
                print("Final profit is ${0}0\n".format(str(self.profit)))
            else:
                print("Final profit is ${0}\n".format(str(self.profit)))
            system("pause")
            exit()
        
        if(command == "items"):
            text = ""
            for i in range(len(self.items)):
                text += "   [%s] %s: %s\n" % (str(i), self.items[i].fullName, self.items[i].amount)
            print(text)
            system("pause")
        
        if(command == "add"):
            text = "Select an item to add:\n"
            for i in range(len(self.items)):
                text += "   [%s] %s: %s\n" % (str(i), self.items[i].fullName, self.items[i].amount)
            print(text)
            command = int(input("> "))
            try:
                inp = input("Amount to add to {0}:".format(self.items[command].fullName))
                self.items[command].amount += int(inp)
            except IndexError:
                print("Incorrect value entered!")
            sleep(1)
        
        if(command == "profit"):
            if(list(str(self.profit)).index(".") == (len(str(self.profit)) - 2)):
                print("${0}0".format(str(self.profit)))
            else:
                print("${0}".format(str(self.profit)))
            sleep(3)

        if(command == "help"):
            msg = """
    sale = makes a sale
    items = lists all the items that the shop has
    profit = displays the profit the shop has made
    add = increases the number of a certain item
    save = saves the name, items and profit of a shop to a .shop file
    load = loads the name, items and profit of a shop from a .shop file
    close = saves the name, items and profit of a shop to a .shop file,\n   then terminates the script
    help = displays this message
            """
            print(msg)
            system("pause")

        if(command == "clear"):
            system("cls")
            print(self.tb)
            if(list(str(self.profit)).index(".") == (len(str(self.profit)) - 2)):
                print("Profit: ${0}0\n".format(str(self.profit)))
            else:
                print("Profit: ${0}\n".format(str(self.profit)))
            sleep(3)
        system("cls")
        print(self.tb)
        if(list(str(self.profit)).index(".") == (len(str(self.profit)) - 2)):
            print("Profit: ${0}0\n".format(str(self.profit)))
        else:
            print("Profit: ${0}\n".format(str(self.profit)))
