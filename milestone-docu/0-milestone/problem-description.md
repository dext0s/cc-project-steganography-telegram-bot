# Problem description

One of the reasons I've started a career inside computer science is due the fascination of how Cybersecurity works. And one of the fields that most appeal to me is encryption and transmision of secrets.

One of the methods used that appeals me the most is [steganography](https://www.kaspersky.com/resource-center/definitions/what-is-steganography), or the technics to encrypt messages inside images or other kind of documents.

I would like to have a way, on my phone, to check encryp and decrypt messages inside images I have or pictures I've taken. Also to have the basic tooling to check if an image is hidding anything.

# Proposed solution

The solution proposed will be a telegram bot that will be handling this request and a stenography server that will be doing the image processing.
If I have enough time I would like to have a proper persistence implemented on it. (To send several test in parallel without resending the image).

I must say, that there are several projects that attempted the same as I want to, but I'm mostly interested on learning how an application like this must be deployed, tested and the different techniques to hide, retrieve the data and analyse a suspicious file.
