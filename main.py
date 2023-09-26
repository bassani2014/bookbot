def main():
    file_contents = get_string_from_file("books/frankenstein.txt")
    letter_dictionary = convert_string_to_dictionary(file_contents)
    letter_list = list(letter_dictionary.items())
    new_letter_list = return_alphabetic_list(letter_list)

    # Print out results
    for x in new_letter_list:
        print("The ", x[0], " character was found ", x[1] , " times")

def get_string_from_file(path):
    with open(path) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    return file_contents


def convert_string_to_dictionary(string_to_convert):
    letter_dictionary = {}
    for j in string_to_convert:
        if j in letter_dictionary:
            letter_dictionary[j] += 1
        else:
            letter_dictionary[j] = 1
    return letter_dictionary


def return_alphabetic_list(list_to_convert):
    new_letter_list = []
    for j in list_to_convert:
        if str(j[0]).isalpha():
            new_letter_list.append(j)

    new_letter_list.sort()
    return new_letter_list


main()
