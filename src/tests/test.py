from imagededup.methods import PHash as Hash
import os
import json

_hash = Hash()

image_dir = r'e:/Pictures/'

if __name__ == '__main__':
    encodings = dict()
    for root in os.listdir(image_dir):
        img_dir = os.path.join(image_dir, root)
        if os.path.isdir(image_dir):
            result = _hash.encode_images(image_dir=img_dir)
            for k, v in result.items():
                encodings['%s/%s' % (root, k)] = v

    dedup_json = os.path.join(image_dir, 'dedup.json')
    duplicates = _hash.find_duplicates(encoding_map=encodings, outfile=dedup_json)

    cp = duplicates.copy()
    for k, v in duplicates.items():
        if len(v) != 0:
            if cp.__contains__(k):
                for i in v:
                    if cp.__contains__(i):
                        cp.pop(i)
        else:
            cp.pop(k)

    lis = list()
    for k, v in cp.items():
        d = dict(img=k, dedup=v)
        lis.append(d)

    print('result = %s' % len(lis))

    filter_json = os.path.join(image_dir, 'filter.json')

    with open(filter_json, 'w', encoding='utf-8', ) as f:
        json.dump(lis, f, indent=4, ensure_ascii=False)

    print('========================')
