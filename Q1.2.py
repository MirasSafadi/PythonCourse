server={
    "host": "localhost",
    "port": 3030,
    "public": "../public/",
    "paginate": {
        "default": 10,
        "max": 50
    },
    "mongodb": "mongodb://127.0.0.1:27017/api"
}
print(server.get("paginate").get("max"))
str = server.get("mongodb")
L = str.split(":")
ip = L[1]
ip = ip[2:]
print(ip)