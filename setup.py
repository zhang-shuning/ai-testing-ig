'''Script to get images'''
import pathlib
import shutil

images = pathlib.Path("images")


files = [item for item in images.iterdir() if item.is_file()]
name_dict = {'Abyssinian': 203, 'american_bulldog': 200, 'american_pit_bull_terrier': 200, 'basset_hound': 200, 'beagle': 200, 'Bengal': 200, 'Birman': 200, 'Bombay': 200, 'boxer': 200, 'British_Shorthair': 200, 'chihuahua': 200, 'Egyptian_Mau': 200, 'english_cocker_spaniel': 200, 'english_setter': 200, 'german_shorthaired': 200, 'great_pyrenees': 200, 'havanese': 200, 'japanese_chin': 200, 'keeshond': 200, 'leonberger': 200, 'Maine_Coon': 200, 'miniature_pinscher': 200, 'newfoundland': 200, 'Persian': 200, 'pomeranian': 200, 'pug': 200, 'Ragdoll': 200, 'Russian_Blue': 200, 'saint_bernard': 200, 'samoyed': 200, 'scottish_terrier': 199, 'shiba_inu': 200, 'Siamese': 200, 'Sphynx': 200, 'staffordshire_bull_terrier': 191, 'wheaten_terrier': 200, 'yorkshire_terrier': 200}
count_dict = {}
for i in name_dict:
    count_dict[i] = 25

for i in files:
    cur_name = i.name
    if i.suffix == ".mat":
        continue
    for j in range(len(cur_name)-1, -1, -1):
        if cur_name[j] == '_':
            cur_name = cur_name[0:j]
            break
    if count_dict[cur_name] != 0:
        count_dict[cur_name] -= 1
        shutil.copy2(i, "images_to_use")

print(count_dict)
