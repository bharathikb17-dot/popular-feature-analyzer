from popular_features import popularFeatures

features = ["storage","space","memory","cpu"]

requests = [
"i wish i had more storage",
"it would be good to have more cpu",
"i wish i had more memory",
"memory and cpu should be more",
"i need more storage",
"i need more cpu",
"i wish i had more memory",
"i wish i had more space"
]

topN = 2

result = popularFeatures(features, requests, topN)

print("Top Requested Features:", result)
