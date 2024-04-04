def hello(name, lang,):
    greetings = {
        "English" : "Hello",
        "Spanish" : "Hola",
        "German"  : "Hallo"
    } 
    
    msg = f"{greetings[lang]}, {name}!"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="name of the person"
    )

    parser.add_argument(
        "-l", "--lang", metavar="Language",
        required=True, choices=["English", "Spanish", "German"], 
        help = "language of the greeting"
    )

    args = parser.parse_args()
    hello(args.name, args.lang)

