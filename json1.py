#Convert from Python to JSON:
import json

data={
    "Python":90,
    "EMWTL":70,
    "DLD":80,
    "CS":90,
    "A.Cir":80,
    "AC":90
}

data1=json.dumps(data)

print(data1)