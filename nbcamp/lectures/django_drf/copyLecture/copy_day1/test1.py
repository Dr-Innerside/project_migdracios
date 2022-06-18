def test(*args, ** kwargs):
    print(args)
    return True

sample_list = [1,2,3,4,5]
sample_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
}
test(*sample_list)