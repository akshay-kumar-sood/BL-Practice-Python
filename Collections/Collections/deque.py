from collections import deque

d=deque([10,20,30,40])


print(f"original list : {d}")
d.append(50)
print(f"After adding ele : {d}")

d.appendleft(5)
print(f"After adding ele in front : {d}")

d.pop()
print(f"delete last ele : {d}")

d.popleft()
print(f"delete ele from front {d}")

print(f"original list : {d}")
d.rotate(2)
print(f"After rotating by 2 places : {d}")


# used to make dequeu. we can perform operation from both end front and end. 
# save shifting process used in list to do the same
# some method are appendLeft popLeft rotate
# all operation in 0(1)
# used in undo/redo , browser history