import time
start = time.time()

num_word_dict={0: 0, 1:len("one"),2:len("two"),3:len("three"),
4:len("four"),5:len("five"), 6:len("six"),7:len("seven"),
8:len("eight"),9:len("nine"),10:len("ten"),11:len("eleven"),
12:len("twelve"),13:len("thirteen"),14:len("fourteen"),
15:len("fifteen"),16:len("sixteen"),17:len("seventeen"),
18:len("eighteen"),19:len("nineteen"),20:len("twenty"),
30:len("thirty"),40:len("forty"),50:len("fifty"),
60:len("sixty"),70:len("seventy"),80:len("eighty"),
90:len("ninety"),100:len("onehundred"),200:len("twohundred"),
300:len("threehundred"),400:len("fourhundred"),
500:len("fivehundred"),600:len("sixhundred"),700:len("sevenhundred"),
800:len("eighthundred"),900:len("ninehundred"),1000:len("onethousand")}

def num_letter(num):
    if num == 1000: return num_word_dict[1000]
    num = str(num)
    sum_of_letters = 0
    if len(num) == 3:
        sum_of_letters += num_word_dict[int(num[0] + '00')] + len("and")
        if num[1:] == '00':
            sum_of_letters -= len("and")
        
        elif num[1] == '1':
            sum_of_letters += num_word_dict[int(num[1:])]
        
        else:
            sum_of_letters += num_word_dict[int(num[1] + '0')]
            sum_of_letters += num_word_dict[int(num[2])]
    
    elif len(num) == 2:
        if num[0] == '1':
            sum_of_letters += num_word_dict[int(num)]
        else:
            sum_of_letters += num_word_dict[int(num[0] + '0')]
            sum_of_letters += num_word_dict[int(num[1])]
    
    elif len(num) == 1:
        sum_of_letters += num_word_dict[int(num)]

    return sum_of_letters

sum_of_letters_of_all_numbers = 0

for i in range(1, 1001):
        sum_of_letters_of_all_numbers += num_letter(i)

print("sum: ", sum_of_letters_of_all_numbers)

end = time.time()
print("it took {} seconds".format(end - start))
