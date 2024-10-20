player_score = "22"
leader_scores = ["50", "14", "15", "20", "51", "5342", "-1"]
scores = leader_scores
scores.append(player_score)
print(scores)
ordered_scores = []

for score in scores:
  def result():
    try: return 0 if int(score) >= int(ordered_scores[index]) else -1
    except IndexError: 0

  index = 0
  while result() == -1:
    index += 1
  ordered_scores.insert(index, int(score))
print(ordered_scores)