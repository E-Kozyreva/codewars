# Create a function that takes in a list of button inputs and returns the final state.

# Examples
# like_or_dislike([Dislike]) ➞ Dislike
# like_or_dislike([Like, Like]) ➞ Nothing
# like_or_dislike([Dislike, Like]) ➞ Like
# like_or_dislike([Like, Dislike, Dislike]) ➞ Nothing

def like_or_dislike(lst):
    if len(lst) == 0:
        return "Nothing"
    elif (len) == 1:
        return lst[0]
    else:
        reaction = lst[0]
        for i in range(1, len(lst)):
            if reaction == lst[i]:
                reaction = "Nothing"
            else:
                reaction = lst[i]
        return reaction
