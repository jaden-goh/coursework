"""You are given an array of stock prices where 
prices [i] prices[i] is the price of a given stock on the ith ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Write a python program that will return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,6,4,3,1]
Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List

def buy_and_sell_stock(prices: List[int]) -> int:
    """Write your code here"""
    minPrice = float('inf')
    p = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        else:
            profit = price - minPrice
            p = max(p, profit) 

    return p