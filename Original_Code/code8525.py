# put your python code here
alphabet = [(i) for i in input()]
code = [(i) for i in input()]
dictionary = {}
for i in range(len(alphabet)):
    dictionary[alphabet[i]] = code[i]

message_to_encode = [(i) for i in input()]
message_encoded = []
for i in message_to_encode:
    #j = dictionary[i]
    message_encoded.append(dictionary[i])

message_to_uncode = [(i) for i in input()]
message_uncoded = []
for i in message_to_uncode:
    for key, value in dictionary.items():
        if i == value:
            message_uncoded.append(key)
print(''.join(str(i) for i in message_encoded))
print(''.join(str(i) for i in message_uncoded))



 