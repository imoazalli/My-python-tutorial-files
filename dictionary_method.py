mydict={"fast":"in a quick manner",
        "harry":"a codder",
        "marks":[1,2,3,4],
        1:2
        }
#keys method
print(mydict.keys())
# values method
print(mydict.values())
# items in which both key& value
print(mydict.items())
#updated method
updatedict={
    "hammad":"brother",
    "haider":"brother"
}
mydict.update(updatedict)
print(mydict)
#get method & syntax method similarity
print(mydict.get("harry"))
print(mydict['harry'])
# difference between them
print(mydict.get("harry2"))# they run the programme
print(mydict['harry2'])# they dont run


