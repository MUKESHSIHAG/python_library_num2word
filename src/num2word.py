class digitToWord:
    def unit(self, num):
        word = ''
        if(num == "1"):
            word = 'One'
        if(num == "2"):
            word = 'Two'
        if(num == "3"):
            word = 'Three'
        if(num == "4"):
            word = 'Four'
        if(num == "5"):
            word = 'Five'
        if(num == "6"):
            word = 'Six'
        if(num == "7"):
            word = 'Seven'
        if(num == "8"):
            word = 'Eight'
        if(num == "9"):
            word = 'Nine'
        word.strip()
        return word
    
    def tens(self, num):
        word = ''
        if(num[0] == '1'):
            if(num[1] == '0'):
                word = 'Ten'
            if(num[1] == '1'):
                word = 'Eleven'
            if(num[1] == '2'):
                word = 'Twelve'
            if(num[1] == '3'):
                word = 'Thirteen'
            if(num[1] == '4'):
                word = 'Fourteen'
            if(num[1] == '5'):
                word = 'Fifteen'
            if(num[1] == '6'):
                word = 'Sixteen'
            if(num[1] == '7'):
                word = 'Seventeen'
            if(num[1] == '8'):
                word = 'Eighteen'
            if(num[1] == '9'):
                word = 'Nineteen'
        else:
            after = self.unit(num[1])
            if(num[0] == '2'):
                word = 'Twenty'
            if(num[0] == '3'):
                word = 'Thirty'
            if(num[0] == '4'):
                word = 'Fourty'
            if(num[0] == '5'):
                word = 'Fifty'
            if(num[0] == '6'):
                word = 'Sixty'
            if(num[0] == '7'):
                word = 'Seventy'
            if(num[0] == '8'):
                word = 'Eighty'
            if(num[0] == '9'):
                word = 'Ninety'
            word = word + " " + after
        word = word.strip()
        return word

    def hundreds(self, num):
        word = ''
        after = self.tens(num[1:])
        if(num[0] == "1"):
            word = 'One'
        if(num[0] == "2"):
            word = 'Two'
        if(num[0] == "3"):
            word = 'Three'
        if(num[0] == "4"):
            word = 'Four'
        if(num[0] == "5"):
            word = 'Five'
        if(num[0] == "6"):
            word = 'Six'
        if(num[0] == "7"):
            word = 'Seven'
        if(num[0] == "8"):
            word = 'Eight'
        if(num[0] == "9"):
            word = 'Nine'
        if(num[0] != '0'):
            word = word + ' Hundred '
        word = word + after
        word.strip()
        return word  

def seg(n):
    n = n[::-1]
    a = [n[i:i+3][::-1] for i in range(0,len(n),3)]
    return a

def word(digit):
    if(isinstance(digit, int)):digit=str(digit)
    if(digit.isdigit()):
        digit = digit.lstrip('0')
        word = digitToWord()
        bm = ["","thousand","million","billion","trillion"]
        segn = seg(digit)
        response = ''
        b = 0
        for i in range(len(segn)):
            if len(segn[i])==1:
                response = word.unit(segn[i]) + ' ' + bm[(i)%len(bm)] + ' ' + response
            if len(segn[i])==2:
                response = word.tens(segn[i]) + ' ' + bm[(i)%len(bm)] + ' ' + response
            if len(segn[i])==3:
                response = word.hundreds(segn[i]) + ' ' + bm[(i)%len(bm)] + ' ' + response
        return response.rstrip(" ")
    else:
        raise Exception('Make sure that, the number you passed "'+str(digit)+'" doesn\'t contain any alphabet or special symbol!')
