import functions.piglatin

if __name__ == "__main__":
    print(f"air == {functions.piglatin.pig_latin('air')}")
    print(f"eat == {functions.piglatin.pig_latin('eat')}")
    #print(functions.piglatin.pig_latin('python'))
    #print(functions.piglatin.pig_latin('computer'))

    print("Testing sentence")
    sentence = "this is a test translation"
    print(f"{sentence} ===>  {functions.piglatin.pig_latin_sentence(sentence)}")



