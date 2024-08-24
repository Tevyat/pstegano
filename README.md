# PSteganography

This python-cli tool allows you to securely encode a message into an image by first using a key to generate a pad from a SHA-256 hash, then XORs each byte of the message with the corresponding byte of the pad to produce an encrypted message.

## Requirements

After installation and extraction:
```bash
$ cd pstegano
$ pip install -r requirements.txt
```


## Usage/Examples

```bash
$ python main.py -e -c "image.jpg" -k "key" -m "message here"
$ python main.py -d -k "key"
message here
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

