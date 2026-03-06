from collections import Counter

def popularFeatures(features, requests, topN):

    count = Counter()

    for r in requests:
        words = set(r.lower().split())

        for f in features:
            if f in words:
                count[f] += 1

    sorted_features = sorted(
        count.items(),
        key=lambda x: (-x[1], x[0])
    )

    return [feature for feature, _ in sorted_features[:topN]]
