#!/usr/bin/python3
'''
    A module with a solution to lock boxes interview
    question
'''


def canUnlockAll(boxes):
    ''' Function that implements solution to lockboxes '''
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
