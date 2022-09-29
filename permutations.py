#List of permutations
#You are given an array of words. Your task is to check if a permutation of each word has occurred earlier in the list -- if so, remove that word from the array, if not, keep it in the array. #NOTE: A permutation is a word of the same length with the same characters -- they can be in any order (ie. "code" and "ocde")
#Example:
#words = ['code','doce','framer','frame','ocde']
#Output: ['code','framer','frame']
#Explained:
#'code' is the first element in the array, not preceded by any permutations, so keep it
#'doce' is a permutation of 'code', so remove it
#'framer' has no preceding permutations, keep it
#'frame' has no preceding permutations, keep it
#'ocde' is a permutation of 'code' remove it