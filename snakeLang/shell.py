import snakeLang

print("Welcome to snakeLang, the language of the future.")

while True:
    text = input("snakeLang >>> ")
    
    res, err = snakeLang.run(text)

    if err:
        print(err.as_string())
    else:
        print(res)