def recursion(string):

        Odd, Even = funct(numbers[1:])

        if int(numbers[0]) % 2 == 0:
            Even += 1
        else:
            Odd += 1

        return Odd, Even

    Odd, Even = funct(string)

    if Even < Odd:
        return f'There are more odd numbers ({Odd}) or the same as even numbers ({Even}).'
        
    else:
        return f'There are more even numbers ({Even}) than odd ({Odd}).'

print(recursion("0987650"))