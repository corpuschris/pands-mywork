#This program  reads in a text file and outputs the number of e's it contains.

#Author: Christiano Ferreira

FILENAME = "moby-dick.txt"

def count_es_in_file(FILENAME):
    
    #Counts the number of e's in the given file.
    count = 0
    file = open (FILENAME, 'r')
    for line in file:
        count += line.lower().count('e')
    file.close()
    return count

if __name__ == "__main__":
    e_count = count_es_in_file(FILENAME)
    print(f"The file '{FILENAME}' contains {e_count} occurrences of the letter 'e'.")