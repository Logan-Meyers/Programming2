string1 = "Hello Friends"
list1 = [1,2,3,4,5]
integer1 = 5

def small_changes():
    string1 = "Happy"
    list1 = [6,7,8,9]
    integer1 = 10
    print("\nafter small_changes inside Function\n")
    print(f"string1 = {string1}")
    print(f"list1 = {list1}")
    print(f"integer1 = {integer1}")

def more_small_changes(string1, list1, integer1):
    string1 = "Happyish"
    list1 = [10,11,12,13]
    integer1 = 25
    print("\nafter more_small_changes inside Function\n")
    print(f"string1 = {string1}")
    print(f"list1 = {list1}")
    print(f"integer1 = {integer1}")

print("\nBefore small_changes Unchanged \n")
print(f"string1 = {string1}")
print(f"list1 = {list1}")
print(f"integer1 = {integer1}")
small_changes()
more_small_changes(string1, list1, integer1)
print("\nOutside Function\n")
print(f"string1 = {string1}")
print(f"list1 = {list1}")
print(f"integer1 = {integer1}")