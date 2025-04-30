coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    """
    Жадібний алгоритм для визначення кількості монет для видачі решти.
    
    Args:
        amount (int): Сума для видачі решти
        
    Returns:
        dict: Словник з номіналами монет та їх кількістю
    """
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
            
    return result

def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для визначення мінімальної кількості монет.
    
    Args:
        amount (int): Сума для видачі решти
        
    Returns:
        dict: Словник з номіналами монет та їх кількістю
    """

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    current_amount = amount
    
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin
        
    return result

if __name__ == "__main__":
    test_amount = 113
    print(f"Сума для видачі решти: {test_amount}")
    print(f"Жадібний алгоритм: {find_coins_greedy(test_amount)}")
    print(f"Динамічне програмування: {find_min_coins(test_amount)}")
