from importlib.metadata import files
import os 
import time
import datetime

def sort(array): #This is a sort algorithm based on a Bubble Sort algorith modified for analyze creation date of the files insede the array 
    
  for i in range(len(array)):
        
    swapped = False
    
    for j in range(0, len(array) - i - 1):

      first_tuple = array[j]
      second_tuple = array[j + 1]

      temp_first_tuple = datetime.datetime(first_tuple[1][0], first_tuple[1][1], first_tuple[1][2])
      temp_second_tuple = datetime.datetime(second_tuple[1][0], second_tuple[1][1], second_tuple[1][2])

      if temp_first_tuple > temp_second_tuple:

        temporary = array[j]
        array[j] = array[j+1]
        array[j+1] = temporary

        swapped = True
          
    if not swapped:
      break
    

def run():

    path = r"C:\Users\gabri\Documents\Python_Scripts\backups" #This is the folder path

    final_files_list = [] #This is the list where is going to be saved the complete path of the files

    temporary_list = [] #This is the list where struct_time tuples are saved for sorting

    files_list = os.listdir(path) #This is the files names

    for i in range(0, len(files_list)): #This is where the complete paths are saved 
      final_files_list.append(path + "\\" + files_list[i])

    for i in range(0, len(files_list)): #This is where struc_time tuples are created and saved in a temporary list for sorting by date
      path = final_files_list[i]
      time_in_seconds = os.path.getctime(path)
      temp = time.gmtime(time_in_seconds)
      full_tuple = [path, temp]
      temporary_list.append(full_tuple)

    sort(temporary_list)

    for i in range(len(temporary_list)-5):
      os.remove(temporary_list[i][0])

if __name__ == "__main__":
    run()