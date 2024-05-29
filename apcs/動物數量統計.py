# Content
# 在一齣電影裡你會陸續看到一些動物在某地方出現，請你統計某地方有幾隻某動物出現。

# Input
# 第一列有一個數字N (0<N<=1000)代表資料有幾組

# 接下來的N列每一列內部資料格式為:動物名稱 數量 地點，其中動物名稱與地點為中文字串(除了測試檔案內的名稱外，可能會有其他不同的名稱)，數量為不大於100的正整數。

# Output
# 地點 : 動物名稱 數量, 動物名稱 數量, …

# 請按照地點名稱出現順序輸出，一個地點一行，若同一地點有多種動物出現則按照動物名稱出現順序輸出

# Sample Input #1
# 7
# 猴子 2 樹上
# 蛇 1 地上
# 烏龜 2 水裡
# 熊 1 樹上
# 猴子 1 地上
# 蛇 3 樹上
# 猴子 3 樹上
# Sample Output #1
# 樹上:猴子 5,熊 1,蛇 3
# 地上:蛇 1,猴子 1
# 水裡:烏龜 2

def generate_animals_str(m):
	strs = []
	for name, count in m.items():
		strs.append(f"{name} {count}")
	return ",".join(strs)

def animal_counter():
	n = int(input())
	places_map = {}
	for _ in range(n):
		animal, count_str, place = input().split()
		animals_map = places_map.get(place, {})
		animals_map[animal] = animals_map.get(animal, 0) + int(count_str)
		places_map[place] = animals_map

	for place, animals_map in places_map.items():
		animals_str = generate_animals_str(animals_map)
		print(f"{place}:{animals_str}")

if __name__ == "__main__":
	animal_counter()
