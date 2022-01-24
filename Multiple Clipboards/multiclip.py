import json
import clipboard




#the basics of how clipboards work
#data=clipboard.paste()
#print (data)
#clipboard.copy("PENTAKILL")
#can paste the above


#Can also be done in pandas with the following
#df=pd.DataFrame(['Text to copy'])
#df.to_clipboard(index=False,header=False)


####################The Multiclip Project##############################





#in the same directory as code so just put filename. 
Saved_Filepath = "Clip.json"

#Function to write data to json


def saves(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


#function to read data from json


def load(filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
        return {}



#Find out what the user is trying to do
User_Instructions =input("Please type an option: 'save' , 'load', or '*' to see all' ")


    
#run the load data function and save it in data
data = load(Saved_Filepath)



#what to do if the user types save
if User_Instructions == "save":

    title = input("What is the name of your clipboard entry: ")

    #put in an entry in the file(data) under the variable name(title)
    data[title] = clipboard.paste()
    
    
    #run the save function and print a confirmation.
    saves(Saved_Filepath, data)
    print( title +" saved to file")


#what to do if user types load
if User_Instructions == "load":


    title = input("What clipboard entry are you trying to load? ")

    if title in data:

        #copy title's data to clipboard
        clipboard.copy(data[title])

        print("The corresponding data for "+ title + " has been copied to clipboard.")

    else :
        print(title+ " does not exist")


#show everyything on the sheet
if User_Instructions == "*":
    print("The format is as follows: 'Name of item': 'Whatever is on it's clipboard'\n")
    print(data)

