import numbers, operator, itertools, time
from random import randint
from fractions import Fraction
from colorama import Fore, Style

def generate_nums(high_nums, low_nums, high_nums_cnt):
    selected_nums = []
    for i in range(high_nums_cnt):
        elem = randint(0, len(high_nums) - 1)
        
        selected_nums.append(high_nums[elem])
        high_nums.remove(high_nums[elem])

    for i in range(6 - high_nums_cnt):
        elem = randint(0, len(low_nums) - 1)

        selected_nums.append(low_nums[elem])
        low_nums.remove(low_nums[elem])
    
    return selected_nums 

def get_solutions(target, numbers):
    numbers = [Fraction(num) for num in numbers]
    return solve_generator(target, numbers)

def solve_generator(target, numbers):
    if len(numbers) == 1:
        if numbers[0] == target:
            yield str(target)
        return

    for a,b in itertools.permutations(numbers, 2):
        for symbol, op in operators.items():
            try:
                product = op(a,b)
            except ZeroDivisionError:
                continue

            subnumbers = list(numbers)
            subnumbers.remove(a)
            subnumbers.remove(b)
            subnumbers.append(product)

            for solution in solve_generator(target, subnumbers):
                yield solution.replace(str(product), f"({a}{symbol}{b})")


high_nums = [num for num in range(1, 100+1) if num % 25 == 0]
low_nums = [num for num in range(1, 10+1)] * 2
operators = operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

high_nums_cnt = int(input("How many high numbers : "))

start_time = time.time()

numbers = generate_nums(high_nums, low_nums, high_nums_cnt)
target = randint(100, 1000)
sols = get_solutions(target, numbers)

print(f'Target: {Fore.YELLOW}{target}{Style.RESET_ALL}\n' + 
        f'Using: {Fore.YELLOW}{numbers}{Style.RESET_ALL}\n')

for i, sol in enumerate(sols):
    print(f"{i + 1}: {Fore.GREEN}{sol[1:-1]}{Style.RESET_ALL}")

    if time.time()-start_time > 30:
        print(f"\n\nFound {Fore.GREEN}{i + 1}{Style.RESET_ALL} solutions in 30 seconds!")
        break
