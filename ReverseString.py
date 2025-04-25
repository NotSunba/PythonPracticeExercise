text = input("Write something: ")
reversed_text = "" #use an empty string to be used for prepending
for txt in text:
    reversed_text = txt + reversed_text #prepending - makes the latest character to be always on the front
    # example : if txt = "hello" and reversed text is "" then it'll start with "o"
    #then "hell" +"o" = "lo" and it'll keep looping

print(f"the reversed text is {reversed_text}")
