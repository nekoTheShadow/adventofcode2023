def get_hand(cards)
  patterns = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5]
  ]

  return patterns.index(cards.chars.tally.values.sort) unless cards.include?('J')

  max_score = 0
  %w(2 3 4 5 6 7 8 9 T Q K A).repeated_combination(cards.count('J')) do |jokers|
    new_cards = jokers.reduce(cards){|s, joker| s.sub('J', joker)}
    score = patterns.index(new_cards.chars.tally.values.sort)
    max_score = [max_score, score].max
  end
  max_score
end

def get_label(cards)
  cards.chars.map{|card| %w(J 2 3 4 5 6 7 8 9 T Q K A).index(card)}
end

p IO.readlines('./input.txt').map{|line|
  card, bit = line.chomp.split
  [card, bit.to_i]
}.sort_by{|(cards, bit)|
  [get_hand(cards), get_label(cards)]
}.each_with_index.sum{|(cards, bit), rank| 
  (rank+1)*bit
}
