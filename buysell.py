class StockProfitCalculator:
    def __init__(self, prices):
        self.prices = prices

    def maxProfit(self):
        min_price = float('inf')
        max_profit = 0
        
        for price in self.prices:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            # Calculate the current profit and update the max profit if applicable
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    calculator = StockProfitCalculator(prices)
    print(f"The maximum profit is: {calculator.maxProfit()}")
