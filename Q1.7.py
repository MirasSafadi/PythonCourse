d = {
    "page": 1,
    "pageCount": 12,
    "pageSize": 25,
    "items": [
        {
            "id": 12,
            "active": True,
            "title": "The Trials and Tribulations of Tristram Shandy.",
            "date": {
                "start": "2004-09-16T23:59:58.75",
                "end": "2004-09-16T23:59:58.79"
            },
            "code": "12345"
        },
        {
            "id": 10,
            "active": True,
            "title": "The Life and Letters of Leonard Lego.",
            "date": {
                "start": "2004-09-16T23:59:58.75",
                "end": "2004-09-16T23:59:58.79"
            },
            "code": "66778"
        }
    ]
}
#setting the item with id=12 active field to False
d["items"][0]['active'] = False
print(d["items"][0]['active'])
dic = {
    "id": 15,
    "active": False,
    "title": "Steve Jobs Biography.",
    "date": {
        "start": "2010-09-16T23:59:58.75",
        "end": "2010-09-16T23:59:58.79"
    },
    "code": "123456"
}
d["items"].append(dic)
print(d["items"])
lst  = []
for dic in d["items"]:
    lst.append((dic["date"]["start"],dic["date"]["end"]))
print("-----------------------------------------")
print(lst)