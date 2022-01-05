
import os
import csv, tabulate
import pandas as pd
class OFile:
    def __init__(self,path:str="./oscar_age_female.csv",fields=[]):

        self.path = path
        self.fields = fields

        self.manager_menu()


    def add(self):
        year = input("Please enter a year of the Oscar: ")
        age = input("Please enter the age of the winner: ")
        name = input("Please enter the name of the winner: ")
        movie = input("Please enter the movie name: ")
        df = pd.DataFrame({'Year':year,
                   'Age': age,
                   'Name': name,
                   'Movie':movie},index=[0])

        df.to_csv(self.path, mode='a', index=False, header=False)
        self.manager_menu()

    def update(self):

        df = pd.read_csv(self.path)
        index = input(f"Please enter the index of the row you want to update ( range 0-{len(df.index)-1} )")
        print(df.loc[int(index)].to_string())



        y_or_n = input(print("Is this the row you want to update? [y / N]"))
        if y_or_n == "y":
            year = input("Please enter a new year of the Oscar: ")
            age = input("Please enter the new age of the winner: ")
            name = input("Please enter the new name of the winner: ")
            movie = input("Please enter the new movie name: ")


            df.loc[int(index), 'Year'] = year
            df.loc[int(index), 'Age'] = age
            df.loc[int(index), 'Name'] = name
            df.loc[int(index), 'Movie'] = movie


            df.to_csv(self.path, index=False)

            print(df.to_string())
        elif y_or_n == "N":
            self.update()
        else:
            raise ValueError("Invalid choice")
    def delete(self):
        df = pd.read_csv(self.path)
        index = input(f"Please enter the index of the row you want to delete ( range 0-{len(df.index)-1} )")
        print(df.loc[int(index)].to_string())



        y_or_n = input(print("Is this the row you want to update? [y / N]"))
        if y_or_n == "y":

            df.drop(index=int(index))

            print(df.to_string())


        elif y_or_n == "N":
            self.delete()
        else:
            raise ValueError("Invalid choice")
    def print_file(self):


        df = pd.read_csv(self.path)

        print(df.to_string())

    def search_operation(self,item):
            items = ["year","age","name","movie"]
            search = input(f"Search with {items[item-1]}: ")
            reader = csv.reader(open(self.path, 'r'))
            for row in reader:
                    if row[item-1]==search:

                        print(row[0:])
    def search(self):


        print("""What title do you want to search by?
                    1- Year
                    2- Age
                    3- Name
                    4- Movie""")
        item = input()
        if int(item) > 0 and int(item) < 5:
            self.search_operation(int(item))

        else:
            print("WARNING: Your choice must be between 1 and 4 !")
            self.search()


    def run_selected_menu_item(self,item):
        if item == "1":
            self.search()

        elif item == "2":
            self.delete()

        elif item == "3":
            self.update()

        elif item == "4":
            self.add()
        elif item == "5":
            self.print_file()

        else:
            print("WARNING: Your choice must be between 1 and 5 !")
            self.manager_menu()

    def manager_menu(self):

        print ("""
            1.Search
            2.Delete
            3.Update
            4.Add
            5.Print File
        """)
        user_choice = input()


        self.run_selected_menu_item(user_choice)

def main():
    file_manager = OFile()



if __name__ == "__main__":
    main()
