#These commands import the correct modules I'll be using to display/visualise data.
import sys
import pandas as pd
import matplotlib.pyplot as plt


#These are the headers, and these will be assigned to columns.
col = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","intrusion_type"]


#This code reads the CSV file, then assigns the header names.
df = pd.read_csv('kddcup_data.csv', names = col)


print ("Welcome to the KDD Cup Data Analysis Dashboard! Keep in mind, for this program to function, you must type each input exactly as listed. For example, for option 3, type the labels exactly how you see them in the dataframe. Thanks!")
print ("---------------------------------------------------------------------------------------------------------------------------------------------------------")


#This prints out the full dataframe for the user if they want to see it.
dataframe = input ("If you'd like to see the full dataframe, type 'yes', or 'no' if not.")
if dataframe == "yes":
        print(df)
    
elif dataframe == "no":
        print("No problem!")


#This code analyses the dataset and cleans it, using the df.head and df.tail commands.
def data_analysis():
    print(df.head(10))
    print (df.tail(5))
    print (df.describe)
    print (df.loc[0])
    print (df["duration"].mean)
    print (df["service"].unique())
    
def linechart():
    user_input = input ("Choose an X label:")
    plt.xlabel(user_input)
    second_input = input ("Choose a Y label:")
    plt.ylabel(second_input)
    plt.plot(linestyle = 'dotted')
    plt.show()
    
#This code is for displaying a bar chart that plots the data given below.
def barchart():
    x = df["duration"]
    y = df["protocol_type"]
    plt.title("KDD Cup Data - Duration against Protocol Type")
    plt.xlabel("Duration")
    plt.ylabel ("Protocol Type")
    plt.bar(x,y)
    plt.show()

#This code plots a piechart using the data given below.
def piechart():
    x = df["num_file_creations"]
    y = df ["count"]
    plt.title("KDD Cup Data - Number of File Creations Against Count")
    plt.pie(x,y)
    plt.show()


#This is the main menu of the program, the user can select various options of what they want to see using the console menu.
def main_menu():
    print ("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print ("Option 1 - Display bar chart that displays duration against protocol type.")
    print ("Option 2 - Display pie chart that displays number of file creations against count.")
    print ("Option 3 - Display line graph with custom filtering options.")
    print ("Option 4 - Display full data analysis of data set.")
    print ("Option 5 - Exit.")
    print ("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    option = input ("Pick an option from above.")
    
    if option == "Option 1":
        barchart()
        main_menu()
    
    elif option == "Option 2":
        piechart()
        main_menu()
      
    elif option == "Option 3":
           linechart()
           main_menu()
           
    elif option == "Option 4":
        data_analysis()
        main_menu()
        
    elif option == "Option 5":
        sys.exit()
           
    else:
        print("Restart the program and choose one of the selected options.")

main_menu()

