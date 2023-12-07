def get_hand(cards)
  [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5]
  ].index(cards.chars.tally.values.sort)
end

def get_label(cards)
  cards.chars.map{|card| %w(2 3 4 5 6 7 8 9 T J Q K A).index(card)}
end

p IO.readlines('./input.txt').map{|line|
  card, bit = line.chomp.split
  [card, bit.to_i]
}.sort_by{|(cards, bit)|
  [get_hand(cards), get_label(cards)]
}.each_with_index.sum{|(cards, bit), rank| 
  (rank+1)*bit
}
