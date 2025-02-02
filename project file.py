import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Fun():
        print(":)")
        print("#1. For checking the data.")
        print("#2. Reading complete file without index.")
        print("===================")
        print("Topic - Data Visualization")
        print(" ")
        print("#3. Line Chart")
        print("    Press 1 to print the data for Confirmed cases as per Districts.")
        print("    Press 2 to print the data for Recovered cases as per Districts.")
        print("    Press 3 to print the data for Death cases as per Districts.")
        print("    Press 4 to print the data for Active cases as per Districts.")
        print("    Press 5 to print All data.")
        print(" ")
        print("#4. Bar Graph")
        print("    Press 1 to print the data for Confirmed cases as per Districts.")
        print("    Press 2 to print the data for Recovered cases as per Districts.")
        print("    Press 3 to print the data for Death cases as per Districts.")
        print("    Press 4 to print the data for Active cases as per Districts.")
        print("    Press 5 to print the data in form of stack bar chart")
        print("    Press 6 to print the data in form of multi bar chart")
        print(" ")

        print("#5. For Exit")
        print("===============")


def Read_CSV():
    print("The Data")
    df=pd.read_csv("//Users//ritikaagrawal//Documents//my_project//Covid_data_Gujarat.csv")
    print(df)

def No_Index():
    print("Reading the file without index")
    df=pd.read_csv("//Users//ritikaagrawal//Documents//my_project//Covid_data_Gujarat.csv", index_col=0)
    print(df)


#FOR LINE CHART:)

def line_plot():
    df=pd.read_csv("//Users//ritikaagrawal//Documents//my_project//Covid_data_Gujarat.csv")
    df['Districts']=[' BRD',' CHR',' VYR',' SUR',' KMR','MHV','MND','MNG','UMP','OLD','PLS',' KDR',' SGD',' UDA']
    District=df["Districts"]
    Confirmed=df["Confirmed"]
    Recovered=df["Recovered"]
    Deaths=df["Deaths"]
    Active=df["Active"]
    plt.xlabel("Districts")

    
    YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
    
    if YC == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("Districts Wise Confirmed Cases")
        plt.plot(District, Confirmed, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Recovered Cases")
        plt.title("Districts Wise Recovered Cases")
        plt.plot(District, Recovered, color='g')
        plt.show()
    elif YC == 3:
        plt.ylabel("Death Cases")
        plt.title("Districts Wise Death Cases")
        plt.plot(District, Deaths, color='r')
        plt.show()
    elif YC == 4:
        plt.ylabel("Active Cases")
        plt.title("Districts Wise Active Cases")
        plt.plot(District, Active, color='c')
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of cases")
        plt.plot(District, Confirmed, color='b',label = "Districts Wise Confirmed Cases")
        plt.plot(District, Recovered, color='g', label = "Districts Wise Recovered Cases")
        plt.plot(District, Deaths, color='r', label = "Districts Wise Death Cases")
        plt.plot(District, Active, color='c',label = "Districts Wise Active Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        

#FOR BAR GRAPH:)

def bar_plot():
    df = pd.read_csv("//Users//ritikaagrawal//Documents//my_project//Covid_data_Gujarat.csv")
    df['Districts'] = [' BRD',' CHR',' VYR',' SUR',' KMR','MHV','MND','MNG','UMP','OLD','PLS',' KDR',' SGD',' UDA']
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]
    plt.xlabel("Districts")


    YC = int(input("Enter the number representing your preferred bar graph from the above choices:"))
    
    if YC == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("Districts Wise Confirmed Cases")
        plt.bar(District, Confirmed, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Recovered Cases")
        plt.title("Districts Wise Recovered Cases")
        plt.bar(District, Recovered, color='g',)
        plt.show()
    elif YC == 3:
        plt.ylabel("Death Cases")
        plt.title("Districts Wise Death Cases")
        plt.bar(District, Deaths, color='r')
        plt.show()
    elif YC == 4:
        
        plt.ylabel("Active Cases")
        plt.title("Districts Wise Active Cases")
        plt.bar(District, Active, color='c',)
        plt.show()
        
    elif YC == 5:
        
        plt.bar(District,Recovered,color='g', label = "Districts Wise Recovered Cases")
        plt.bar(District,Confirmed,color='b', label = "Districts Wise Confirmed Cases")
        plt.bar(District,Deaths,color='r',label = "Districts Wise Death Cases")
        plt.bar(District,Active,color='c',label = "Districts Wise Active Cases")
        plt.legend()
        plt.show()
    elif YC == 6:
        D=np.arange(len(District))
        width=0.30
        plt.bar(D,Confirmed, width, color='b', label = "Districts Wise Confirmed Cases")
        plt.bar(D+0.30, Recovered, width, color='g',label = "Districts Wise Recovered Cases")
        plt.bar(D+0.6, Deaths, width, color='r', label = "Districts Wise Death Cases")
        plt.bar(D+0.10, Active ,width, color='c', label = "Districts Wise Active Cases")
        plt.legend()
        plt.xticks(D,District)
        plt.show()
    else:
        print("Enter valid input")

Yc="y"
if  ((Yc=="Y")or(Yc=="y")):
    Fun()
    YC = int(input("Enter Your Choice: "))

    while YC == 1 or 2 or 3 or 4 or 5 or 6:
        if YC == 1:
            Read_CSV()
            break
        elif YC == 2:
            No_Index()
            break
        elif YC == 3:
            line_plot()
            break
        elif YC == 4:
            bar_plot()
            break
        elif YC == 5:
            print("Thank You for using...")
            break
        else:
            print("Enter valid input")
            break

    while Yc=="y":
        Yc=input("Do you want to see another result?[if yes enter 'y'] or [if no enter 'n']: ")
        if  ((Yc=="Y")or(Yc=="y")):
            Fun()
            YC = int(input("Enter Your Choice: "))

            while YC == 1 or 2 or 3 or 4 or 5 or 6:
                if YC == 1:
                    Read_CSV()
                    break
                elif YC == 2:
                    No_Index()
                    break
                elif YC == 3:
                    line_plot()
                    break
                elif YC == 4:
                    bar_plot()
                    break
                elif YC == 5:
                    print("Thank You for using...")
                    break
                else:
                    print("Enter valid input")
                    break
