#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

#Example 1:

#Input: accounts = [[1,2,3],[3,2,1]]
#Output: 6
#Explanation:
#1st customer has wealth = 1 + 2 + 3 = 6
#2nd customer has wealth = 3 + 2 + 1 = 6
#Both customers are considered the richest with a wealth of 6 each, so return 6.


def maximumWealth(accounts):
        max_wealth = 0 #maximum wealth
        ind_wealth = 0 #each individual's total wealth
        
        for i in range(len(accounts)):
            #print(i)
            print (len(accounts))
            #print(sum(accounts[i]))
            ind_wealth = sum(accounts[i])
            #print(ind_wealth)
            if ind_wealth > max_wealth:
                max_wealth = ind_wealth
                #print('cats')
        return max_wealth 


print(maximumWealth([[1,2,3],[4,7,8],[4,5,6],[7,4,8]]))
print('show me the money')