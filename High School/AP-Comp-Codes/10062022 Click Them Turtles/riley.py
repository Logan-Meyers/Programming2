player_score = "22"
leader_scores = ["50", "14", "15", "20", "51", "5342", "-1"]
scores = leader_scores
scores.append(player_score)
print(scores)
ordered_scores = []

for score in scores:
  # 0 if true -1 if false
  def result():
    # if the score is >= the score at the current spot in the list, 0 (insert), otherwise -1 (next index)
    try: return 0 if int(score) >= int(ordered_scores[index]) else -1
    # if the index reaches outside the bounds of the list (no more numbers to compare), 0 (insert number)
    except IndexError: 0

  # reset index to start of current ordered list
  index = 0
  # while the score is NOT >= the score at the current spot (index):
  while result() == -1:
    # print(result(), index)
    # move to next spot/index
    index += 1
  # print(result(), index)
  # insert (once loop stops; can insert score)
  ordered_scores.insert(index, int(score))
print(ordered_scores)

"""
# old code:
for score in scores:
  if (int(score) >= int(scores[index])):
    ordered_scores.insert(index, int(score))
  else:
    index += 1
print(ordered_scores)
"""