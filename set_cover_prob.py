import math
def get_set_cover(univ_set, subsets):
    merged_set, set_cover, tot_cost = set(), [], 0
    while merged_set != univ_set:
        next_subset, min_cost_eff, curr_cost = None, math.inf, None
        for subset, cost in subsets:
            cost_eff = cost / len(subset - merged_set) if len(subset - merged_set) > 0 else math.inf
            if cost_eff < min_cost_eff:
                min_cost_eff = cost_eff
                next_subset = subset
                curr_cost = cost
        merged_set |= next_subset
        set_cover.append(next_subset)
        tot_cost += curr_cost
    return (set_cover, tot_cost)

U = {1, 2, 3, 4, 5,6,7,8,9,10,11,12,13}
S = [({1,2},10),({2,3,4,5},10),({6,7,8,9,10,11,12,13},10),({1,3,5,7,9,11,13},10),({2,4,6,8,10,12,13},10)]

set_cover, tot_cost = get_set_cover(U, S)
print(set_cover)
print("tot cost: ", tot_cost)