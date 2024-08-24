from argparse import ArgumentParser
from functions.image import encode, decode

parse = ArgumentParser()

parse.add_argument("-e", "--encrypt", action="store_true", help="Encrypt a message and encode the encrypted message into an image.")
parse.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the encoded message in an image with the correct key.")
parse.add_argument("-s", "--sample", action="store_true", help="Sample usage")

parse.add_argument("-c", "--current", help="Encrypt a message and encode the encrypted message into an image.")
parse.add_argument("-k", "--key", help="Encrypt a message and encode the encrypted message into an image.")
parse.add_argument("-m", "--message", help="Encrypt a message and encode the encrypted message into an image.")

args = parse.parse_args()

if args.encrypt:
    try:
        encode(args.current, args.key, args.message)
    except:
        print("An error has occured. Please type python main.py -h for help or type python main.py -s for sample usage.")
elif args.decrypt:
    try:
        print(decode("new_image.jpg", args.key))
    except:
        print("An error has occured. Please type python main.py -h for help")
elif args.sample:
    print("For encryption: python main.py -e -c <path_to_img> -k <encryption_key> -m <message>\nFor decryption: python main.py -d -k <encryption_key>\nNote that an encrypted image will pop up on the same directory with the name 'new_img.jpg', the decryption does not need a path as it will automatically attempt to decode the 'new_img.jpg' file.")
else:
    print("Unknown command, please type 'python main.py -h' for more information.")
