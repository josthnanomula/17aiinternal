import math

def minimax(cur_depth, node_index, max_turn, scores, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]

    if max_turn:
        return max(minimax(cur_depth + 1, node_index * 2, False, scores, target_depth),
                   minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth))
    else:
        return min(minimax(cur_depth + 1, node_index * 2, True, scores, target_depth),
                   minimax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth))

scores = [14,3,5,2,9,17,24,16]
tree_depth = math.log(len(scores), 2)

print("The optimal value is:", minimax(0, 0, True, scores, int(tree_depth)))
