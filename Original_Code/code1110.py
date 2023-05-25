from queue import PriorityQueue


# fill in the queue with negative weights
# for sorting from maximum to minimum weights
# return q with added fruits
def putToBasket(q, fruits):
  for w in fruits:
    q.put(-w)
  return q


# fill in hand with fruits.
# given:
#   q - queue with fruit weights;
#   k - lifting capacity of Johnny
# return (hand, q):
#   hand - list of weights of taken fruits
#   q - new queue without taken fruits
def fillInHand(q, k):
  hand = [] # fruits to be bitten
  handWeight = 0 # total weight of fruits in the hand
  while not q.empty():
    w = -q.get()
    if handWeight + w > k:
      # return fruit to the basket
      q.put(-w)
      # a fruit can't weight more than k
      # so one first fruit we take anyway
      break
    handWeight += w
    hand.append(w)
  return hand, q


# bite the fruits
# hand - list of fruits weights to bite
# return iterator of bits of the fruits
def biteFruits(hand):
  bits = map(lambda w: w // 2, hand)
  return filter(lambda w: w > 0, bits)


# find how many times Johnhy eat fruits
# n - number of fruits in basket
# fruitsWeights - list of fruits weights
# k - lifting capacity of Johnny
def JohnnyBites(n, fruitsWeights, k):
  i = 0 # number of iterations
  q = PriorityQueue(n)
  # fill in the queue with negative weights
  # for sorting from maximum to minimum weights
  q = putToBasket(q, fruitsWeights)
  
  # eat cycle
  while not q.empty():
    i += 1
    # fill in hand with fruits
    hand, q = fillInHand(q, k)
    # bite the fruits
    bits = list(biteFruits(hand))
    # put bits to the basket
    q = putToBasket(q, bits)
  return i


n = int(input())
strFruits = input().strip()
fruits = map(int, strFruits.split())
k = int(input())
print(JohnnyBites(n, fruits, k)) 