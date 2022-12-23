import streamlit as st

string1 = st.text_input("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
def convert_list(string):
    li = list(string.split(" "))
    return li
str1 = "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "

"""
This button return the list of words
"""
if st.button("Return List"):
    st.write(str1)
print(convert_list(str1))



def convert_lower(string):   
    str1_upper = [string.upper() for string in str1]
    print(str1_upper)
str1=["Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."]
"""
This button converts that list in upper case
"""
if st.button("upper"):
    st.write(convert_lower(string1))

convert_lower(string1)

def count(list):
    count = 0
    for element in list:
        count += 1
    return count
list = str1
"""This button counts the elements of the list
"""
if st.button("print_count"):
    st.write(list)

print(count(list))




